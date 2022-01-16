# take user input
user_number = int(input("enter your interger number: "))

my_list=[] 
for i in range(2,user_number+1):#number to test 
    if user_number >=2:
        my_list.append(2)
    for j in range(2,i):#by this number "j"I can test
        if  i%j==0 :
            # my_list.remove(i)
            break
    else:
        my_list.append(i)
my_set=set(my_list)
# display our expected output
print(*my_set)
# count number of prime number
print(len(my_set))



