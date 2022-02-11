# prepration for my code 
my_list=list("hackerrank")
count=0

# input operation 
n=int(input())
for i in range(n):
    string_in=input()

# ouput operation

    for i in string_in:
        if count==len(my_list): 
            break
        if i==my_list[count]:
            count+=1
        

    if count==len(my_list):
            print("YES")
    else:
            print("NO")

    count=0  #reset count ===> important