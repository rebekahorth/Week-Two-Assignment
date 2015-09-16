__author__ = 'Rebekah Orth'

# CIS 125 Fall 2015
# Temperature Table

def main():
    F=eval(input("Please enter a temperature in Fahrenheit:"))
    
    C= (F-32) * 5 / 9
    
    print("The temperature ", F , " in Fahrenheit is equal to ", C , " Celsius")
main()