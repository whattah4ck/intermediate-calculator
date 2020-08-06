#!/usr/bin/python3
#advanced calculator
import math

print ("Welcome to the ADVANCED CALCULATOR")
print ("\nif you want to learn what this advanced calculator can do just type 'y'(yes) or if you want to quit just type 'q' \n")
process = input ()
if process == "y":
    print("\nWelcome!Welcome!")
    print ("\nwhat you can do?\n")
    print ("1. 4 işlem \n")
    print ("2. factorial\n")
    print ("3. ceiling\n")
    print ("4. flooring\n")
    print ("5. truncate\n")
    options = input() 
    if options=="1":
        number=input("number 1:")
        number2=input("number 2:")
        floatnumber=float(number)
        floatnumber2=float(number2)
        print ("choose the process")
        print (" addition = +\n subtract = -\n multiply = *\ndivide = /")
        işlem = input("process:")

        if işlem == "+":
            output=floatnumber+floatnumber2
        if işlem == "-":
            output=floatnumber-floatnumber2
        if işlem == "*":
            output=floatnumber*floatnumber2
        if işlem == "/":
            output=floatnumber/floatnumber2
        print ("that's it: "+str(output))    
    elif options=="2":       
        print("enter the number you want to learn factorial ")
        number = int(input())
        print (math.factorial(number)) 
    elif options=="3":
        print("enter the number you want to learn ceil ")
#ceil 
        ceilnumber = float(input())
        print (math.ceil(ceilnumber))       
    elif options=="4":
        print("enter the number you want to learn floor ")
#floor
        floornumber = float(input())
        print (math.floor(floornumber)) 
    elif options=="5":
        print ("enter the number you want to learn truncate")
#float 
        truncatenumber=float(input())
        print (math.trunc(truncatenumber))
"""    elif options=="6":
        print ("write 2 numbers to learn their closeness") 
        isclosenumber=input()
        print (math.isclose(isclosenumber))"""
    else:
        print("please log a current options")      
if process == "q":
    print("\nSee you in the next time!")    

