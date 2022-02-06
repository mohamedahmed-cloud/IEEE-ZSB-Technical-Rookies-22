# Write your code here
if y1 > y2:
    fine = 10000 #given in the problem 
elif m1 > m2 and y1 == y2:
    fine = 500 * (m1 - m2) #it's given in the problem 
elif d1 > d2 and m1 == m2 and y1 == y2:
    fine = 15 * (d1 - d2) #given in the problem 
else:
    fine=0   
return fine
