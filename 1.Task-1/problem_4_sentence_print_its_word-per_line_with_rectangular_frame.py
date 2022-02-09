user_input = input("Enter your sentences ")
user = user_input.split() #the varible here is very important ==> without it we will print each letter in new line
# To bring the length of largest word
list=[]
for word in user:
     list.append(len(word))
my_longest_word=max(list)
# print(my_longest_word)

# To make the frame and display word
w=1
for word in user:
    
    if w==1:  #to prevent these stars from printing more one time 
        print("*"*(my_longest_word+4))     # make up,down of frame is equal and equal the largest word length
    w+=1             #to break the if in the next loop
    print("*", end=" ")
    print(word,end=" ")
    print(" "*(my_longest_word-len(word))+"*") # To justify the left star
print("*"*(my_longest_word+4))
