  
for i in range(int(input())):
 
    s = sorted(input())
    t = sorted(input())
    # making a dictionary of data to count if there is a repeat letter in string
    S = {}
    T = {}
    # assign zero to all dictionary value
    for i in s:
       S[i] = 0
    # assign zero to all dictionary value
    for i in t:
      T[i]=0
    # compute the repeated of element ,inserting it in dictionary value
    for i in s:
       S[i] = S[i] + 1
    # compute the repeated of element ,inserting it in dictionary value
    for i in t:
       T[i] = T[i] + 1
    # operation of making conversion for number of  dictionary value 
    c = 0
    for i in S:
       if i not in T:
           c = c + S[i]  
       elif S[i]<T[i]:
           c = c + (T[i]-S[i])
       elif S[i]>T[i]:
           c = c + (S[i]-T[i])
    for i in T:
           if i not in S:
                c = c + T[i]
    print(c)
 