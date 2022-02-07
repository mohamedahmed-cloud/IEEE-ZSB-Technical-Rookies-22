def findDigits(n):
    # Write your code here
    count=0
    for i in range(t):
        for j in str(n):
            if int(j) ==0: #to prevent the operation of zero division 
                pass
            elif int(n) % int(j)==0:
                count+=1
        return count
        count=0   #very important ==> to reset counter after finish the enter loop
