from math import *

print("This program counts the number of primes within a range.\n")
stop=True

while stop:
    primenum = 0
    checknum=True
    while checknum:
        num1 = input("Enter the start: ")
        num2 = input("Enter the end: ")
        if num1.isnumeric() and num2.isnumeric():
            checknum=False
            num1=int(num1)
            num2=int(num2)
        else:
            print("Invalid Input")
            checknum=True

    if num1<num2:

        for i in range(num1,num2+1):
            count = 0
            for j in range(1,i+1):
                if i % j == 0:
                    count += 1
            if count == 2:
                primenum += 1

        print ("Ther are " + str(primenum) + " prime numbers between " + str(num1) + " to " + str(num2))
        re=True
        while re:
            con=input("Continue? Y/N: ")
            if con.lower()=="y":
                stop=True
                re=False
            elif con.lower()=="n":
                stop=False
                re=False
                print("BYE BYE")
            else:
                print("Invalid Input")
                re=True
    else:
        print("Invalid Input")
        stop=True