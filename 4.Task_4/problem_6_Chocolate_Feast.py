#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chocolateFeast' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c
#  3. INTEGER m
#

def chocolateFeast(n, c, m):
    # Write your code here
    count=0 # global variable
    for i in range(t):
        first_n=int(n/c)
        count+=first_n
        while first_n>=m:  #undefined while loop because i don't know how many it will repeat
            count+=int(first_n/m)
            first_n=int(first_n/m)+int(first_n%m)  # to remember revision the example in problem and solve it in sheet
        # count=0
        return count
    count =0 # very important to reset counter ==>should reset it after printing not before
# end of my code
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        c = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
