# 1)
# Program to find numbers between 1500 & 2700 which are divisible by 7 and multiples of 5
for i in range(1500,2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i,end=" ")

# 2)
# Temperature Conversions between Celcius and Fahrenheit
c = float(input("Enter the temperature in Celcius "))
f = 9 / 5 * c + 32
print(f"The temperature given in celcius is {c} and in Fahrenheit, it is {f}")
f = float(input("Enter the temperature in Fahernheit "))
c = ( 5 / 9 ) * ( f - 32 )
print(f"The temperature given in Faherheit is {f} and in Celcius, it is {c}")


# 3)
# Guessing Number from random generating inputs
import random
num = random.randint(0,9)
x = int(input("Guess a Number between 0-9: "))
while x != num:
    x = int(input("Guess a Number between 0-9: "))
else:
    print("Well Guessed")


# 4)
# Star Pattern
r = int(input("Enter the range for stars"))
for i in range(0,r+1):
    if i <= r:
        print('*'*i)
    if i == r:
        for j in range(r-1,0,-1):
            print('*'*j)


# 5)
# Reversing a number:
string = str(input("Enter the string"))
for i in range(len(string),0,-1):
    print(string[i-1],end="")


# 6)
# Count total even and odd numbers from 0 to given range
ran = int(input("Enter the range of Numbers"))
odd = 0
even = 0
for i in range(0,ran+1):
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print(f"Total even numbers are: {even}")
print(f"Total odd numbers are: {odd}")


# 7)
# Program that prints each item and its type from the colloction of list of elements of diferent datatypes:
listt = [1452,11.23,1+2j,True,'w3resource',(0,1),[5,12],{'class':"V","section":'A'}]
for i in listt:
    print(f"Item: {i}, Type: {type(i)}")


# 8)
# Program that prints all numbers except 3 and 6
for i in range(0,7):
    if i == 3 or i == 6:
        continue
    else:
        print(i,end=" ")


# 9)
# Fibonacci Series between 0-50
a, b = 0, 1
while a <= 50:
    print(a, end=", ")
    a, b = b, a + b

for i in range(0,51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        continue
    if i % 3 == 0:
        print("Fizz")
    if i % 5 == 0:
        print("Buzz")


# 10)
# Two-Dimensional Array:
rows = int(input("Enter the number of rows: "))
column = int(input("Enter the number of column: "))
result = [[i*j for j in range(column)] for i in range(rows)]
print(result)


# 11)
# TExt converted into lower text series
x = input("Enter the text and I will convert it into lower text: ")
y = x.lower()
print(y)


# 12)
# List of binary numbers and output is that binary number that is divisible by 5
res = 0
binary = ['0100','0011','1010','1001','1100','1001','101','1111','10100']
decimal = []
for i in binary:
    p = len(i)-1
    for j in i:
        k=int(j)
        if k == 1:
            res = res + (k*2**p)
        p = p - 1
    if res % 5 == 0:
        print(i,end=" ")
    res = 0
print()


# 13)
# This program will calculate the total digits and letters in the given string
x = input("Enter the string: ")
digit = 0
letter = 0
for i in x:
    if i.isdigit():
        digit += 1
    else:
        letter += 1
print(f"Total Digits are {digit}")
print(f"Total Letters are {letter}")


# 14)
# Check the Validity of the password
import re
def valid_password(password):

    if not (6 <= len(password) <=16):
        return False
    if not re.search(r"[a-z]",password):
        return False
    if not re.search(r"[A-Z]",password):
        return False
    if not re.search(r"\d",password):
        return False
    if not re.search(r"[$#@]",password):
        return False
    
    return True

password = input("Enter the password: ")
if valid_password(password):
    print("Valid Password")
else:
    print("InValid Password")