import math
import data as data_lib
WHOLE = 10
DECIMAL = 1.0
INCRAMENT = 0.5
TWO = 2
EDGE = 1


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
    """sort values in ascenting order"""
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
    if len(new_values) % TWO == 0:
        return (new_values[length // TWO - 1] + new_values[length // TWO]) / TWO
    else:
        return new_values[math.ceil((length-1) / TWO)]


def population_statistics(feature_description, data, treatment, target, threshold, is_above, statistic_functions):
    """
    prints the results of the statistics functions on the target parameter
    on a segment of the data by relation between treatment and threshold
    :param feature_description: title
    :param data: the data for analysis
    :param treatment: the field to sort the data by threshold
    :param target: the field to be used for the statistic functions
    :param threshold: the threshold for sorting the data on treatment by
    :param is_above: decides if the data used is above threshold or not
    :param statistic_functions: the functions to analise the filtered target data by
    :return:
    """

    #new_values = data[treatment].copy()
    #sort(new_values)
    #min=(int)(new_values[0]*WHOLE)
    values=[]
    #for x in range(min,threshold*WHOLE+EDGE,int(INCRAMENT*WHOLE)):
    for x in data[treatment]:
        if(x<=threshold): values.append(x)
            #values.append(x/(WHOLE*DECIMAL))
    data1, data2 = data_lib.filter_by_feature(data, treatment, values)
    data_lib.print_details(data2,{target},statistic_functions) if is_above else data_lib.print_details(data1,{target},statistic_functions)
    #if is_above:
    #    data_lib.print_details(data2,{target},statistic_functions)
    #else:
    #    data_lib.print_details(data1,{target},statistic_functions)