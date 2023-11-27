#1getting_started.py

# 1. Syntax

# 1.1 Insert the missing indentation to make the code correct:
# HINT: https://www.w3schools.com/python/python_syntax.asp

# TODO: update the code below
if 4 == 2:
  print("Four is equal to two!")


# 1.2 Variables
# HINT: https://www.w3schools.com/python/python_variables.asp

#1.2.1 Create a variable named fruit and assign the value Apple to it.
# TODO: Write your code below
fruit = "Apple"
print("The variable fruit is", fruit)

# 1.2.2 Create a variable called z, assign x + y to it, and display the result.
x = 10
y = 20

# TODO: Wrtie your code below
z = x + y
print("THe variable z is:", z)

# 1.2.3 Remove the illegal characters in the variable name:
# TODO: Update the code below
cityname = "London"

# 1.2.4 Insert the correct keyword to make the variable x belong to the global scope.
# HINT: https://www.w3schools.com/python/python_variables_global.asp
# TODO: Update the code below
def myfunc():
  global x
  x = "fantastic"

# 1.2.5 write a program that switches the values stored in variables a and b.
a = 5
b = 4
# TODO: Write your code below
x = a
a = b
b = x
print("After switching a =", a, "b =", b)

# 1.3. Data Types
# casting, numbers, booleans
# HINT: https://www.w3schools.com/python/python_datatypes.asp

# 1.3.1 Write a program that add the digits in a two digit number input.
# eg. if the input is 45. The the output should be 4+5=9

number = input("Enter a two digit number: ")

# TODO: Wrtie your code below
x=int(number[0])
y=int(number[1])
print("The sum of the digits is", x+y)