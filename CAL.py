import time as t
import math as m
from os import system, name

def clear():
    """Function For Clearing the Screen"""
    if name == "nt":
        _ = system('cls')

def Add():
    """This function Add Numbers"""
    First_number = eval(input('Enter First Number: '))
    i = "yes"
    Second_result = 0
    while i == 'yes':
        Second_Number = eval(input("Enter Next Number: "))
        Second_result += Second_Number 
        i = input("Want to add more Number(yes/no): ")
    result = First_number + Second_result
    print( "Answer = ",result )
    t.sleep(3)
    Welcome_scr()

def Sub():
    """Function to Substract Numbers"""
    First_Number = eval(input("Enter First Number: "))
    Second_Number = eval(input("Enter Second Number: "))
    result  = First_Number - Second_Number
    print("Answer = ", result)
    More = input("Want to substract More(new)(yes/no): ")
    if More == "yes":
        Sub()
    else:
        Welcome_scr()
def Mul():
    """Function for multiplication of numbers"""
    First_Number = eval(input("Enter First Number: "))
    i = 'yes'
    Second_result = 1
    while i == 'yes':
        Second_Number = eval(input("Enter Next Number: "))
        Second_result = Second_Number*Second_result
        i = input("Want to Multiplicat more(yes/n0): ")
    print("Answer = ", Second_result*First_Number)
    t.sleep(3)
    Welcome_scr() 
def Div():
    """Function for Division"""
    numerator = eval(input("Enter Numerator: "))
    denominator = eval(input("Enter Denominator: "))
    try:
        result = numerator/denominator
        print("Answer = ", result)
    except ZeroDivisionError as Infinite:
        print("1/0 = Infinite(ZeroDivisionError)")
    i = input("Want to Divide More(yes/no): ")
    if i == 'yes':
        Div()
    else:
        Welcome_scr()
def Rem():
    """Function For  Finding Remainder"""
    numerator = eval(input("Enter Numerator: "))
    denominator = eval(input("Enter Denominator: "))
    try:
        result = numerator%denominator
        print("Answer = ",result )
    except ZeroDivisionError as Error:
        print("You are Dividing 1 with 0!")
    i = input("Want to find more?(yes/no): ")
    if i == 'yes':
        Rem()
    else:
        Welcome_scr()
def square():
    Number = eval(input('Enter A Number: '))
    result = m.sqrt(Number)
    print("Answer = ",result)
    i = input("Want to find more?(yes/no): ")
    if i == 'yes':
        square()
    else:
        Welcome_scr()
def Welcome_scr():

    print("*************************** Welcome To The Calculator *******************************")
    print("1. Addition.\n2. Substraction.\n3. Multiplication\n4. Division\n5. Remainder\n6. Square Root\n7. Exit ")

    User_Choice = input("Enter Your Operation(1/2/3/4/5/6): ")     #Taking user input.

    """Calling methods according to user choice"""

    if User_Choice == '1':
        Add()
    elif User_Choice == '2':
        Sub()
    elif User_Choice == '3':
        Mul()
    elif User_Choice == '4':
        Div()
    elif User_Choice == '5':
        Rem()
    elif User_Choice == '6':
        square()
    elif User_Choice == '7':
        clear()
        print("\t\t\tTHANKS FOR USING\n\t\tCLOSING.....")
        t.sleep(2)
        exit(0)
    else:
        print("Wrong Input :-(")

Welcome_scr()
