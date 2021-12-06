"""
Adding Program that Turns into a Learning Adventure
This program is a first attempt at learning how to define a function and call it within another function

By: Jack Nickelson

"""

 
import math
import datetime



def area_circle(x):
    radius = int(x **2 * math.pi)
    print("The area of the circle is with a radius of {} is {}. The area of a circle is calculated by squaring the radius and multiplying by pi".format(x, radius))

def addition():
    x_sum = int(sum(int(x) for x in input("Enter the numbers you wish to sum, seperate with spacebar: ").split()))
    print("The sum is: {}".format(x_sum))
    option1 = input("would you like to learn how to calculate the area of a circle and also calculate the area of a circle with a radius of {}? Enter Y or N:".format(x_sum))
    if option1 == "Y" or option1 == "y":
        area_circle(x_sum)
        option2 = input("Do you want to know the date and time? Enter Y or N: ")
        if option2 == "Y" or option2 == "y":
            return print("The current data and time is: ", datetime.datetime.now())
        else:
            print("You decided to leave the program without learning about the date and time. You must be near a clock! To play again, rerun the program.")
            return x_sum    
    else:
        return print("You decided to leave the program without learning how to calcualte the area of a circle. To play again, rerun the program.")

def main_function():
    addition()



main_function()