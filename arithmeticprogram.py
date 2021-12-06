"""
Multiplication, Division, Addition, and Subtraction Program - with simple input validation

*** inspired by the simple, two digit addition program exercise found throughout the internet

By: Jack Nickelson
"""

print("This is a multiplication, division, addition, and subtraction program!")
while True:
    decision = str(input("Would you like to M, D, A, or S?"))
    print("Type M for multiplication, D for division, A for addition, or S for subtraction: ")
    try:
        if decision == "A" or decision == "a":
            first_number=int(input("Addend 1:"))
            second_number=int(input("Addend 2:"))
            sum=first_number+second_number
            print("Enter your numbers separated by a comma")
            print('The sum of {} and {} is: {}'.format(first_number,second_number,sum))
            break
        elif decision == "S" or decision == "s":
            first_number=int(input("Minuend:"))
            second_number=int(input("Subtrahend:"))
            difference=first_number-second_number
            print('The difference of {} and {} is: {}'.format(first_number,second_number,difference)) 
            break  
        elif decision == "M" or decision == "m":
            first_number=int(input("Factor_1:"))
            second_number=int(input("Factor_2:"))
            product=first_number*second_number
            print('The product of {} and {} is: {}'.format(first_number,second_number,product))
            break  
        elif decision == "D" or decision == "d":
            first_number=int(input("Dividend:"))
            second_number=int(input("Divisor:"))
            quotient=first_number/second_number
            print('The quotient of {} and {} is: {}'.format(first_number,second_number,quotient))
            break   
        elif decision == "q":
            break
        elif decision == "quit":
            break
        elif decision == "exit":
            break
        elif decision == "no":
            break
        elif decision == "No":
            break
    except:
        print('This is not a valid selection. Please input a capital letter of M, D, A, or S:')

