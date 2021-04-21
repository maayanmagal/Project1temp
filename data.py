import pandas
import sys


def load_data(path, features):
    """
        extracts data from csv file into dictionary.
        :param path: path to csv file.
        :param features: feats to extract from dictionary.
        :return: sub-dictionary whose keys are the feats from features.
    """
    df = pandas.read_csv(path)
    data = df.to_dict(orient="list")
    new_data = {}
    for feat in features:
        new_data[feat] = data[feat]
    return new_data


def filter_by_feature(data, feature, values):
    """
    splits the data into 2 dicts based on if feature gets a value in values in each entry.
    :param data: the inputed data
    :param feature: the feature to sort by
    :param values: which values should be put in which dict
    :return: 2 dicts
    """
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
    """
    prints the result of the statistic functions on a list of features.
    :param data: the inputed data
    :param features: the features to activated the functions on
    :param statistic_functions: the statistic analysis to do on the data
    :return:
    """
    for feature in features:
        print("{}: ".format(feature), end="")
        feat_list = data[feature]
        for x in range(len(statistic_functions)-1):
            print("{}, " .format(statistic_functions[x](feat_list)), end="")
        print("{} " .format((float)(statistic_functions[len(statistic_functions)-1](feat_list))))
