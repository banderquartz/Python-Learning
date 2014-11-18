'''
Created on Nov 18, 2014

@author: mike
'''
while True:
    try:
        num = int(input("Please enter an integer: "))
        if num % 2 == 0:
            print("The number " + str(num) + " is even.")
        else:
            print("The number " + str(num) + " is odd.")
        break
    except ValueError:
        print("Ooops! That wasn't an integer! Try again.\n")