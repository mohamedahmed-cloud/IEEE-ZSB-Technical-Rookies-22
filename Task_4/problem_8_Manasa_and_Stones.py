# Note that I remove the function in the editor to be able to use print built in funciton 
# first of my code ################################################################
t=int(input())
for i in range(t):
    n=int(input())
    a=int(input())
    b=int(input())
    list=[]   
    for j in range(n):
        list.append((n-1)*min(a,b) + j*abs(a-b))
    new_list=sorted(set(list))
    for k in new_list:
        print(k,end='')
        print(" ",end='')
    print(" ")
# End of my code ###############################################
