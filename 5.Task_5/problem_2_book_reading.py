# input 
input_n_t=list(map(int,input().split()))
Working_time=list(map(int,input().split()))
count=0


#output operation 

t=input_n_t[1]
i=0
time_required=0
while(t>time_required):
    time_required +=86400-Working_time[i] #to calculate the time by substract the day's second from the time that she work 
    i+=1  # to increase the index by one every time
    count+=1  # number of days


print(count)