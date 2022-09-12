# for taking input from user we can use Input
# = sign is the assigmnet operator for store some values
# name is acting as a variable

# name = input("what's your name? ");

# as other languages like C we can also show some msg to the user using Print keyword
# when we use + sign it will concatenate the string without a space that why we added a space inside the quotes

# print("hello, " + name)

# but notice when we add multiple arugments to the print function it will add a space between them

# print("hello", name)

# There's another way to print a varibale inside a string
# we can use f string formally known as formatted string literals
# its symbol is f and its a specially formated string

# print(f"hello, {name}")

# strings comes with alot of different functionalities
# for instance if the user intentionally or unintentionally add a space before or after the name
# it will still print the name with the space in it making it look abnormal
# to remove the space we can use strip() function

# name = name.strip()
# print(f"hello, {name}")

# now the output will be hello, name without any space

# we can use the same method within the string itself
# print(f"hello, {name.strip()}")

# we can also use the upper() function to convert the string to uppercase
# and lower() function to convert the string to lowercase
# and capitalize() function to capitalize the first letter of the string
# print(f"hello, {name.strip().capitalize()}")

# as we can see now no matter what the user type it will always print the name with the first letter capitalized and spaces will eb removed and its better
# there are alot of functionality on string that we can use
# now if we take above code it will only capitalize the first letter not the frist letter of every single word user typed
# to do that we can use title() function

# print(f"hello, {name.strip().title()}")
# now it will capitalize the first letter of every single word


# we can also split the name into first name and last name and assign it to two different variables
# first, last = name.split(" ")
# print(f"hello, {first.strip().title()} {last.strip().title()}")

# now in the above code we are splitting the name into two parts and assigning it to two different variables
# and then we are printing it with the first letter of every single word capitalized
# but if we add spaces now it will give errors because we are spliting it before we can remove spaces
# to fix the error we have to put the str methods on the input function not the print fuction
# so it will work properly

# name = input("what's your name? ").strip().title();
# first, last = name.split(" ")
# print(f"hello, {first}")

# now it will work properly and only print the first name with first


# integer in python ---- int

# python these symbols + - * / are used for arithmatic operations
# we can also use % for modulus

# int is a type but also act like a function
# we can use it to convert a string to integer

# x = input("x: ")
# y = input("y: ")

# z = int(x) + int(y)
# print(f"{z:,}")

#  :, will format the number with commas

# float

# x = float(input("x: "))
# y = float(input("y: "))

# z = round(x + y)
# print(f"{z:,}")
# round will round the number to the nearest integer

# division
# x = float(input("x: "))
# y = float(input("y: "))

# z = round(x + y)
# print(f"{z:.2f}")

# .2f will round the number to two decimal places


# Functions

# def - is the keyword for defining a function
# defining a function to say hello to the name as we did above hardcoded but now we can define our own function just like below

def say_hello(name):
    print(f"hello, {name}")

# now we can call the function by its name and pass name as its parameter
name = input("what's your name? ")
say_hello(name)