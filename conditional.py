# lets compare two numbers using if & elif statement

 x = int(input("Enter x? : "))
 y = int(input("Enter y? : "))

 if x < y:
     print("x is less than y")
 elif x > y:
     print("x is greater than y")
 else:
     print("x is equal to y")

# or

 x = int(input("Enter x? : "))
 y = int(input("Enter y? : "))

 if x < y or x > y:
     print("x is not equal to y")
 else:
     print("x is equal to y")

# !=

 x = int(input("Enter x? : "))
 y = int(input("Enter y? : "))

 if x != y:
     print("x is not equal to y")
 else:
     print("x is equal to y")

# and ---- both conditions must be true
# or ---- one of the conditions must be true


# match

from nis import match
from unittest import case


name = input("Enter your name? : ")

match name:
    case "John":
        print("Hello John")
    case "Mary":
        print("Hello Mary")
    case _:
        print("Hello Stranger")

# if name isn't specified in the match statement, so we will use _ and it will print "Hello Stranger"


