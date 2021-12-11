"""
Simple Linear Regression and Pearson's r

Input value for x and y variable; program calculates mean, sd, beta_0, beta_1, 
regression equation, and Pearson's correlation coefficient r

The program next asks the user for a value of x and calculates the corresponding value of y

Jack Nickelson
"""

import numpy as np



def userinput():
    x = [int(x) for x in input("Enter the values for the X variable you wish to upload, seperate values with spacebar: ").split()]
    y = [int(y) for y in input("Enter the values for the Y variable you wish to upload, seperate values with spacebar: ").split()]
    x_array = np.array([x])
    y_array = np.array([y])
    #x_t = x_array.T
    #y_t = y_array.T
    x_mean = x_array.mean()
    y_mean = y_array.mean()
    x_std = x_array.std()
    y_std = y_array.std()
    x_distfrommean = x_array - x_mean
    y_distfrommean = y_array - y_mean
    ssx = np.sum(np.power(x_distfrommean,2))
    ssy = np.sum(np.power(y_distfrommean,2))
    sumxyproducts = np.sum(x_distfrommean * y_distfrommean)    
    beta1 = sumxyproducts / ssx
    beta0 = y_mean - (beta1*x_mean)
    correlationcoefficient = sumxyproducts / np.sqrt(ssx*ssy)
    print("X_bar equals {}".format(x_mean))
    print("Y_bar equals {}".format(y_mean))
    print("X standadrd deviation equals {}".format(x_std))
    print("Y standard deviation equals {}".format(y_std))
    print("X_sub_i distance from mean equals {}".format(x_distfrommean))
    print("Y_sub_i distance from mean equals {}".format(y_distfrommean))
    print("The regression equation is y = {} + {}x + e".format(beta0,beta1)) 
    print("beta 1 is: {}".format(beta1))
    print("The y intercept (beta 0) is: {}".format(beta0))
    print("The Pearson's r correlation coefficient is: {}".format(correlationcoefficient))
    fx(beta1,beta0)

def fx(beta1,beta0):
    x_value = float(input("Input a value of x:"))
    y_value = x_value* float(beta1) + float(beta0)
    print("If x equals {}; Y equals {}".format(x_value,y_value))

userinput()

