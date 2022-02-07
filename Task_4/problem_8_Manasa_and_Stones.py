# Note that I remove the function in the editor to be able to use print built in funciton

# first of my code ################################################################
# Our input ==>
t=int(input())
for i in range(t):
    n=int(input())
    a=int(input())
    b=int(input())
    list=[]   
#     operation on input ==>output
    for j in range(n):
        list.append((n-1)*min(a,b) + j*abs(a-b))   #you can get it by mathmetheical operation and your notice ==> This relation is alitte diffcult
    new_list=sorted(set(list))  #very important to make i sorted and unique value
    for k in new_list:  #To display it with square brackets and ","
        print(k,end='')
        print(" ",end='')
    print(" ")        # Make a new line after each operation
# End of my code ###############################################
