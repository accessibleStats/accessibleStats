"""
Univariate Descriptive Statistics Program

By: Jack Nickelson

This program is used to automate the calcualtion of univariate descriptive statistics. The user enters data separated by a space. 
The program then return useful univariate statistics and an explanation of each statistic. This program is an attempt at memory management.
"""
import statistics

def calc_mean(x):
    x_mean = None
    x_mean = int(sum(int(x) for x in x))/len(x)
    print("The mean or average is calcualted by summing all values, and then dividing the sum by the total number of values.")
    print("The mean is: {}".format(x_mean))

def sorted_list(x):
    x_sort = None
    x_sort = sorted(x)
    print("A sorted list can assist you in understanding the values within the variable. It is also important for identifying the median, percentiles, and quartiles, and also for identifying the mode.")
    print("The sorted list is: {}".format(x_sort))

def calc_median(x):
    x_sorted = None
    x_len = None
    midpoint = None
    x_median = None
    x_sorted = sorted(x)
    x_len = len(x_sorted)
    midpoint = (x_len -1) // 2
    if (x_len % 2):
        x_median = (x_sorted[midpoint])
    else:
        x_median = (x_sorted[midpoint] + x_sorted[midpoint] + 1)/2 
    print("The median is the halfway point in the values. Half of the values fall below the median, and half of the values fall above the median.")
    print("The median is: {}".format(x_median))

def calc_mode(x):
    x_mode = None
    x_mode = statistics.multimode(x)
    print("The mode is the value that occurs most frequently within the values. You may have more than one modal value")
    print("The mode is: {}".format(x_mode))

def calc_var(x):
    x_var = None 
    x_var = statistics.variance(x)
    print("The variance is used to understand the spread of the values within the variable. The sample variance is calculated by subtracting the mean of a variable from each observed value, squaring the difference, summing the squared differences, and then dividing by n-1.")
    print("The sample variance is: {}".format(x_var))

def calc_sd(x):
    x_sd = None 
    x_sd = statistics.stdev(x)
    print("The corrected sample standard deviation is the square root of the sample variance. Remember, for sample estimates, use n-1.")
    print("The sample standard deviation is: {}".format(x_sd))

def calc_quantiles(x):
    x_quantiles = None
    x_quantiles = tuple(statistics.quantiles(x, n=4, method='inclusive'))
    print("Quantiles or quartiles also assist is understanding the spread of data. You may use the IQR to identify outlier observations within the data.")
    print("The first quantile is: {0[0]}; the third quantile is: {0[2]}".format(x_quantiles))

def mainfunction():
    datalist = None
    datalist = [int(x) for x in input("Enter the values for the variable you wish to explore, seperate values with spacebar: ").split()]
    print("The values you entered are: {}".format(datalist))
    calc_mean(datalist)
    sorted_list(datalist)
    calc_median(datalist)
    calc_mode(datalist)
    calc_sd(datalist)
    calc_var(datalist)
    calc_quantiles(datalist)


mainfunction()