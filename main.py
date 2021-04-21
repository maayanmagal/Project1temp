import sys
import statistics
import data as data_lib


def main(argv):
    print("Question 1:")
    csv_path = argv[1]
    features = argv[2]
    features = list(features.split(", "))
    data = data_lib.load_data(csv_path, features)
    statistic_functions=[statistics.sum,statistics.mean, statistics.median]
    data1, data2 = data_lib.filter_by_feature(data, "season", [1])
    print("Summer:")
    data_lib.print_details(data1, ["hum", "t1", "cnt"], statistic_functions)

    data1, data2 = data_lib.filter_by_feature(data, "is_holiday", [1])
    print("Holiday:")
    data_lib.print_details(data1, ["hum", "t1", "cnt"], statistic_functions)

    print("All:")
    data_lib.print_details(data, ["hum", "t1", "cnt"], statistic_functions)

    print("Question 2:")
    T_THRESHOLD = 13
    statistic_func=[statistics.mean, statistics.median]
    print("If t1<=13.0, then:")

    data1, data2 = data_lib.filter_by_feature(data,"season",[3])
    data1, data2 = data_lib.filter_by_feature(data1, "is_holiday", [1])
    print("Winter holiday records:")
    statistics.population_statistics("Winter holiday records",data1,"t1",["cnt"],T_THRESHOLD,False,statistic_func)
    print("Winter weekday records:")
    statistics.population_statistics("Winter weekday records", data2, "t1", ["cnt"], T_THRESHOLD, False, statistic_func)
    print("If t1>13.0, then:")
    print("Winter holiday records:")
    statistics.population_statistics("Winter holiday records", data1, "t1", ["cnt"], T_THRESHOLD, True, statistic_func)
    print("Winter weekday records:")
    statistics.population_statistics("Winter weekday records", data2, "t1", ["cnt"], T_THRESHOLD, True, statistic_func)


if __name__ == '__main__':
    main(sys.argv)