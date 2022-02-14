# input operation
t=int(input())
for i in range(t):
    Number_of_friends,Wanted_deleted=list(map(int,input().split()))
    Her_freinds=list(map(int,input().split()))
   
#    output operation
    my_list = []                                                                  

    for i in Her_freinds:                                                      

       while Wanted_deleted and my_list and my_list[-1] < i:                      

           my_list.pop()                                                          

           Wanted_deleted -= 1                                                  

       my_list.append(i)                                                    

    print(' '.join(map(str, my_list)))
  
       
