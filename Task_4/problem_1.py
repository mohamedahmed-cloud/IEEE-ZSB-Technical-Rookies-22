# input operation 
number = input("Enter the integere numbers: ")
list=number.split() #turn into list


# to turn string into integer number format
new_list=[]
for i in list:
    new_list.append(int(i))
print(new_list)


# to find the minimun distance between two numbers ==>output
second_list=[]
min_distance =1000 #any large number but should equal or greater than len(new_list)
for i in range(len(new_list)):
    for j in range(len(new_list)):
        if new_list[i]==new_list[j] and i!=j :
                if min_distance>abs(i-j):
                    min_distance=abs(i-j)
             

print(min_distance)
