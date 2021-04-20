import sys
import statistics
import data as data_lib


def print_stats(data):
    for feat in data:
        if feat == "is_holiday" or feat == "season":
            continue
        feat_list = data[feat]
        sum = statistics.sum(feat_list)
        mean = statistics.mean(feat_list)
        median = statistics.median(feat_list)
        print("{}: {}, {}, {}".format(feat, sum, mean, median))


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
    #print_stats(data1)

    data1, data2 = data_lib.filter_by_feature(data, "is_holiday", [1])
    print("Holiday:")
    data_lib.print_details(data1, ["hum", "t1", "cnt"], statistic_functions)
    #print_stats(data1)

    print("All:")
    data_lib.print_details(data, ["hum", "t1", "cnt"], statistic_functions)
    #print_stats(data)

    print("Question 2:")
    statistic_functions=[statistics.mean, statistics.median]
    print("If t1<=13.0, then:")

    data1, data2 = data_lib.filter_by_feature(data,"season",[3])
    data1, data2 = data_lib.filter_by_feature(data1, "is_holiday", [1])
    print("Winter holiday records:")
    statistics.population_statistics("Winter holiday records",data1,"t1","cnt",13,False,statistic_functions)
    print("Winter weekday records:")
    statistics.population_statistics("Winter weekday records", data2, "t1", "cnt", 13, False, statistic_functions)
    print("If t1>13.0, then:")
    print("Winter holiday records:")
    statistics.population_statistics("Winter holiday records", data1, "t1", "cnt", 13, True, statistic_functions)
    print("Winter weekday records:")
    statistics.population_statistics("Winter weekday records", data2, "t1", "cnt", 13, True, statistic_functions)


if __name__ == '__main__':
    main(sys.argv)