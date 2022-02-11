# input operation
size_of_My_list,beautiful_difference = list(map(int,input().split()))
All_possible_tripels=list(map(int,input().split()))


# output operation
count=0
for i in range(len(All_possible_tripels)-2): #note that we make a minus of len(list)==> it end number by the number of loop under this loop
    for j in range(i+1,len(All_possible_tripels)-1):   #note that we make a minus of len(list)==> it end number by the number of loop under this loop
        #note we start our for loop by "i+1" to decrease the time executatin and it give the same value if we start from zero
        if All_possible_tripels[j]-All_possible_tripels[i]==beautiful_difference: #note that we don't make a minus on len(list) because there is no list under it
            #note we start our for loop by "j+1" to decrease the time executatin and it give the same value if we start from zero
            Triplets = False

            for k in range(j+1,len(All_possible_tripels)):
                if All_possible_tripels[k]-All_possible_tripels[j]==beautiful_difference:
                    count+=1
                    Triplets = True #to give the value true for "triplets " before make "break"
                    break
                
            if Triplets == True:
                break
print(count)
##########################################################################################################

# second solution

# This solution is run faster first solution and I recommand it 

# input operation
size_of_My_list,beautiful_difference = list(map(int,input().split()))
All_possible_tripels=list(map(int,input().split()))


# output operation
count=0
for i in range(len(All_possible_tripels)):
    if All_possible_tripels[i] +beautiful_difference in All_possible_tripels:
        if All_possible_tripels[i]+ 2*beautiful_difference in All_possible_tripels:
            count+=1
    
print(count)


