# input operation
Attendence_n,Topic_number = [int(x) for x in input().split()]
Max_number_of_topic = 0
number_of_group_known = 0
boolean_value_given = [input() for i in range(Attendence_n)] #to decrease execution time

# output operation 

for i in range(0,Attendence_n-1): 
    for j in range(i+1,Attendence_n):
        # make an OR to give the number of One's ==>already topic known
        topic_already_known = bin(int(boolean_value_given[i],2) | (int(boolean_value_given[j],2))).count("1")
        
        
        if topic_already_known>Max_number_of_topic:
            Max_number_of_topic = topic_already_known   #assign max number of topics
            number_of_group_known = 1 #reset number of groups after changing max_number_of_topic
            
        elif topic_already_known == Max_number_of_topic:
            number_of_group_known+=1
            
print(Max_number_of_topic)
print(number_of_group_known)
