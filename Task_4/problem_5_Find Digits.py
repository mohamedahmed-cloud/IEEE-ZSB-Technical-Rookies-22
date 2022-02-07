#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # Write your code here
#     my_code#######################################################
    count=0
    for i in range(t):
        for j in str(n):
            if int(j) ==0: #to prevent the operation of zero division 
                pass
            elif int(n) % int(j)==0:
                count+=1
        return count
        count=0   #very important ==> to reset counter after finish the enter loop
# end of my code ##########################################################
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
