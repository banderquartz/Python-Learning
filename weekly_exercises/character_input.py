'''
Created on Nov 18, 2014

@author: mike
'''
from datetime import datetime


name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

current_year = datetime.now().year
target_year = 100 - age + current_year

print("You, " + name + " will turn 100 years old in the year " + str(target_year))


