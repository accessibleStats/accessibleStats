"""
Multiple Regression Program with up to 5 independent variables

Jack Nickelson

"""


import numpy as np


# function for receiving user input for X variable
# the function will receive up to 5 independent X variables.
# if the user wishes to include n | n<5 variables, the function returns n variables
# the function takes user input as a list, converts to an numpy array, and then concatenates 
# the variables into columns.
def userinputx():
    respone = input("Enter a capital Y or lowercase y to input the values for the first X variable:  ")
    if respone == "Y" or respone == "y":
        x_1 = list(map(float, input("Enter the values for the first X variable you wish to upload, seperate values with spacebar: ").split()))
        x_1 = np.array(x_1)
        x_1 = x_1.astype(np.float64)
        x_1 = x_1[...,None]
        respone2 = input("Would you like to enter the values for the another x variable? enter a capital Y or lowercase y:  ")
        if respone2 == "Y" or respone2 == "y":
            x_2 = list(map(float, input("Enter the values for the second X variable you wish to upload, seperate values with spacebar: ").split()))
            x_2 = np.array(x_2)
            x_2 = x_2.astype(np.float64)
            x_2 = x_2[...,None]
            respone3 = input("Would you like to enter the values for the another x variable? enter a capital Y or lowercase y:  ")
            if respone3 == "Y" or respone3 == "y":
                x_3 = list(map(float, input("Enter the values for the third X variable you wish to upload, seperate values with spacebar: ").split()))
                x_3 = np.array(x_3)
                x_3 = x_3.astype(np.float64)
                x_3 = x_3[...,None]
                response4 = input("Would you like to enter the values for the another x variable? enter a capital Y or lowercase y:  ")
                if response4 == "Y" or response4 == "y":
                    x_4 = list(map(float, input("Enter the values for the fourth X variable you wish to upload, seperate values with spacebar: ").split()))
                    x_4 = np.array(x_4)
                    x_4 = x_4.astype(np.float64)    
                    x_4 = x_4[...,None]
                    response5 = input("Would you like to enter the values for the another x variable? enter a capital Y or lowercase y:  ")
                    if response5 == "Y" or response4 == "y": 
                        x_5 = list(map(float, input("Enter the values for the fifth X variable you wish to upload, seperate values with spacebar: ").split()))
                        x_5 = np.array(x_5)
                        x_5 = x_5.astype(np.float64)
                        x_5 = x_5[...,None]
                        return np.concatenate((x_1, x_2, x_3, x_4, x_5), axis=1)
                    else:
                        return np.concatenate((x_1, x_2, x_3, x_4), axis=1)
                else:
                    return np.concatenate((x_1, x_2, x_3), axis=1)
            else:
                return np.concatenate((x_1, x_2), axis=1)
        else:
            return x_1
    else:
        return

# function for receiving user input for Y variable
def userinputy():
        y = list(map(float, input("Enter the values for the Y variable you wish to upload, seperate values with spacebar: ").split()))
        y = np.array(y)
        y = y.astype(np.float16)
        y = y[...,None]
        return y
 
# function calls userinput function, transforms concatenated arrays into np.matrix
def xmatrix():
    xmatrix = userinputx()
    xmatrix = np.matrix(xmatrix)
    return xmatrix
# function calls userinput function, transforms concatenated arrays into np.matrix
def ymatrix():
    ymatrix = userinputy()
    ymatrix = np.matrix(ymatrix)
    return ymatrix
# main function calls x and y matrix functions, calculates the transpose of X matrix for linear algebra derrivation of predicted beta values
def mainfun():
    X = xmatrix()
    Y = ymatrix()
    X = np.insert(X, 0, 1, axis=1)
    xtranspose = X.getT()
    print(type(X))
    print(type(xtranspose))
    print(Y)
    beta_hat = np.linalg.inv(xtranspose.dot(X)).dot(xtranspose).dot(Y)
    print(beta_hat)

# call main function
mainfun()
