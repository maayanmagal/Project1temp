import math
from data import filter_by_feature as filter
from data import print_details as print_dt


def sum(values):
    """
    the numbers to use for calculations
    :param values: the numbers to use for calculations
    :return: the sum
    """
    s = 0
    for num in values:
        s += num
    return s


def mean(values):
    """
    finds the mean value of values
    :param values: the numbers to use for calculations
    :return: the mean
    """
    s = sum(values)
    return s / len(values)


def sort(values):
    """
    sort values in ascenting order
    :param values: the numbers to use for calculations
    :return: a sorted list
    """
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
    """
    finds the median of values
    :param values: the numbers to use for calculations
    :return: the median
    """

    length = len(values)
    new_values = values.copy()
    sort(new_values)
    if len(new_values) % 2 == 0:
        return (new_values[length // 2 - 1] + new_values[length // 2]) / 2
    else:
        return new_values[math.ceil((length-1) / 2)]


def population_statistics(feature_description, data, treatment, target, threshold, is_above, statistic_functions):
    """
    prints the results of the statistics functions on the target parameter based on a split of the data.

    the split is based on whether the treatment line in the data is higher then the threshold.
    note: filter_by_feature has been defined as filter,
    and print details has been defined as print_dt to reduce line length.
    :param feature_description: title
    :param data: the data for analysis
    :param treatment: the field to sort the data by threshold
    :param target: the field to be used for the statistic functions
    :param threshold: the threshold for sorting the data on treatment by
    :param is_above: decides if the data used is above threshold or not
    :param statistic_functions: the functions to analise the filtered target data by
    :return:
    """
    print_dt(filter(data,treatment,[x for x in data[treatment]if(x<=threshold)^is_above])[0],target,statistic_functions)