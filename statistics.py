import math
from data import filter_by_feature,print_details


def sum(values):
    """finds the sum of values"""
    s = 0
    for num in values:
        s += num
    return s


def mean(values):
    """finds the mean value of values"""
    s = sum(values)
    return s / len(values)


def sort(values):
    """sort values in ascending order"""
    length = len(values)
    for i in range(length):
        max_value = values[0]
        max_index = 0
        for j in range(length - i):
            if values[j] > max_value:
                max_value = values[j]
                max_index = j

        values[max_index] = values[length - i - 1]
        values[length - i - 1] = max_value


def median(values):
    """finds the median of values"""
    length = len(values)
    new_values = values.copy()
    sort(new_values)
    if len(new_values) % 2 == 0:
        return (new_values[length // 2 - 1] + new_values[length // 2]) / 2
    else:
        return new_values[math.ceil((length-1) / 2)]


def population_statistics(feature_description, data, treatment, target, threshold, is_above, statistic_functions):
    """
    prints the results of the statistics functions on the target parameter based on a split of the data

    the split is based on whether the treatment line in the data is higher then the threshold
    :param feature_description: title
    :param data: the data for analysis
    :param treatment: the field to sort the data by threshold
    :param target: the field to be used for the statistic functions
    :param threshold: the threshold for sorting the data on treatment by
    :param is_above: decides if the data used is above threshold or not
    :param statistic_functions: the functions to analise the filtered target data by
    :return:
    """

    values =[x for x in data[treatment] if (x<=threshold)]
    data1, data2 = filter_by_feature(data, treatment, values)
    print_details(data2,target,statistic_functions) if is_above else print_details(data1,target,statistic_functions)
