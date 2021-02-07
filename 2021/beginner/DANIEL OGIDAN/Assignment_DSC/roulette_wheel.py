# On a roulette wheel, the pockets are numbered from 0 to 36. The colors of the pockets are as follows:
# Pocket 0 is green.
# For pockets 1 through 10, the odd-numbered pockets are red and the even-numbered pockets are black.
# For pockets 11 through 18, the odd-numbered pockets are black and the even-numbered pockets are red.
# For pockets 19 through 28, the odd-numbered pockets are red and the even-numbered pockets are black.
# For pockets 29 through 36 the odd-numbered pockets are black and the even-numbered pockets are red.
# Write a program that asks the user to enter a pocket number and displays whether the pocket is green, red, or black. The program should display an error message if the user enters a number that is outside the range of 0 through 36.


def roulette_wheel(value):
       
    checker = value%2
    if value>=1 and value<=10:
        if checker ==0:
            print("Your Pocket Is Black")
        if checker==1:
            print("Your Pocket Is Red")
    elif value >=11 and value <=18:
        if checker==0:
            print("Your Pocket Is Red")
        if checker==1:
            print("Your Pocket Is Black")
    elif value >=19 and value <=28:
        if checker==0:
            print("Your Pocket Is Black")
        if checker==1:
            print("Your Pocket Is Red")
    elif value >=29 and value <=36:
        if checker==0:
            print("Your Pocket Is Red")
        if checker==1:
            print("Your Pocket Is Black")
    elif value == 0:
        print("Your Pocket Is Green")
    else:
        print("Error,your number is outside the range of 0 through 36.")

roulette_wheel(int(input("Enter Your Pocket Number : ")))

