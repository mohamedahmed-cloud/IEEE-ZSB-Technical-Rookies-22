#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    # First of my Code#################################################################################
    count=0
    if p < 4:  # it always equal "1"
        print(1, end='') #to print all of them in the same line
        print(' ',end='') #to make a space
    for i in range(p, q+1):
        if i>4:    # This code doesn't work when y not equal two number so we make it's begin from "4"
            x = i
            y = i**2
            # divided number into two numbers
            z = int(len(str(y))/2)
            first_half = int(str(y)[0:z])
            Second_half = (str(y)[z:])
            # result=int(first_half)+int(Second_half)
            a = int(Second_half)+int(first_half)
            # to give output
            if a == x:
                print(a, end='')
                print(" ", end='')
                count+=a
    if count==0:
                print("INVALID RANGE")


        # result=0 
        # final=0  


# End of my Code #############################################################################

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
