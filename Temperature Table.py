__author__ = 'Rebekah Orth'

# CIS 125 Fall 2015
# Temperature Table
#
# Outputs a table of Celsius and Fahrenheit temperatures in 10 degree increments.

def main():
    for C in range(0, 101, 10):
        F= 9/5 * C + 32
        print(C, F)
        
main()
