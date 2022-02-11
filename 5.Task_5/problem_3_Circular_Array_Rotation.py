# first solution by on it there was a problem in test 4
# input operation 
input_n_k_q=list(map(int,input().split()))
list_to_rotate=tuple(map(int,input().split()))


number_of_list_items=input_n_k_q[0]
number_of_rotaion=input_n_k_q[1]

# output operation 
list_of_index=[]
# to make a list of value I want to print the index for them
for i in range(int(input_n_k_q[2])):
    list_of_index.append(int(input()))

# To make a rotation operation
list_to_rotate=list_to_rotate[ -number_of_rotaion: ] + list_to_rotate[ : -number_of_rotaion]

# To access the value you want:
for i in list_of_index:
    print( list_to_rotate[i] )
    
# second solution
# Give me true value for all test case ###################
# input operation 
Len_of_our_list,Number_of_rotation,Index_number=list(map(int,input().split()))
list_to_rotate=list(map(int,input().split()))

# output operation 
# To make a rotation operation
for i in range(Index_number):
    print(list_to_rotate[(int(input())+Len_of_our_list-Number_of_rotation)%Len_of_our_list] )
    
