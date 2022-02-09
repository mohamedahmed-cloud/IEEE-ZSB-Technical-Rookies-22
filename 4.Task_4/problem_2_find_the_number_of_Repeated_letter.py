# input
word=input("Enter Your Word: ")
number=int(input("Enter your Repeated Time: "))

# output
long=len(word)
new_list=word*int(number/long)+word[0:number%long] #using concatenation "+" to add to string 
print(new_list.count(word[0])) 


