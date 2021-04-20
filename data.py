import pandas
import sys


def load_data(path, features):
    df = pandas.read_csv(path)
    data = df.to_dict(orient="list")
    new_data = {}
    for feat in features:
        new_data[feat] = data[feat]
    return new_data


def filter_by_feature(data, feature, values):
    length = len(data[feature])
    data1 = {}
    data2 = {}
    for key in data:
        data1[key] = []
        data2[key] = []
    for i in range(length):
        for key in data:
            if data[feature][i] in values:
                data1[key].append(data[key][i])
            else:
                data2[key].append(data[key][i])
    return data1, data2


def print_details(data, features, statistic_functions):
    """prints the result of the statistic functions on a list of features."""
    for feature in features:
        print("{}: ".format(feature), end="")
        feat_list = data[feature]
        for x in range(len(statistic_functions)-1):
            print("{}, " .format(statistic_functions[x](feat_list)), end="")
        print("{} " .format((float)(statistic_functions[len(statistic_functions)-1](feat_list))))