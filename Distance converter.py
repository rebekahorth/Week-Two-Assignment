__author__ = 'Rebekah Orth'

# CIS 125 Fall 2015
# Distance Converter
#
# Converts kilometers to miles.

def main():
    K=eval(input("Please enter a distance in Kilometers:"))
    M= K * .621371
    print("The distance ", K , " in Kilometers is equal to ", M , " Miles")
main()
