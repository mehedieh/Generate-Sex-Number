from random import *

print("Randomly Generate Sex Number")
print("(c) Mehedi Hasan 2020")
print("This program will generate random 6-digit numbers until it generates 696969")
print("To start, type y")

answer = input()

if answer == "y":
    trialnumber = 0
    number = 0

    while number != 696969:
        number = randint(100000, 999999)
        print(number)
        trialnumber = trialnumber + 1

    print("Done in " + str(trialnumber) + " tries")
