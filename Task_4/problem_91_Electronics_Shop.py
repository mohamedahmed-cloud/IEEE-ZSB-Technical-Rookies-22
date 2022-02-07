# that represent problem 10 but I name it as it's to take it's true place  on github 
#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    
    
#    Strat of my code ##########################################
    list_1=[]
    
    if b< ( min(keyboards)+min(drives)):
        return -1
        
    for i in keyboards:
        for j in drives:
            if  b>=i+j :   # To prevent adding any value bigger that my budget "b"
                list_1.append(i+j)
    return max(list_1)               # Our Output
    
# ENd of My Code #################################################


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
