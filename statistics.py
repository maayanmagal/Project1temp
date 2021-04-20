import math
import data as data_lib


def sum(values):
    s = 0
    for num in values:
        s += num
    return s


def mean(values):
    s = sum(values)
    return s / len(values)


def sort(values):
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
    length = len(values)
    new_values = values.copy()
    sort(new_values)
    if len(new_values) % 2 == 0:
        return (new_values[length // 2 - 1] + new_values[length // 2]) / 2
    else:
        return new_values[math.ceil((length-1) / 2)]


def population_statistics(feature_description, data, treatment, target, threshold, is_above, statistic_functions):
    """prints the results of the statistics functions on the target parameter
    on a segment of the data where treatment is corelated to the therehold value"""
    new_values = data[treatment].copy()
    sort(new_values)
    min=(int)(new_values[0]*10)
    values = []
    for x in range(min, threshold * 10+1, 5):
        values.append(x/10.0)
    data1, data2 = data_lib.filter_by_feature(data, treatment, values)
    if is_above:
        data_lib.print_details(data2, {target}, statistic_functions)
    else:
        data_lib.print_details(data1, {target}, statistic_functions)