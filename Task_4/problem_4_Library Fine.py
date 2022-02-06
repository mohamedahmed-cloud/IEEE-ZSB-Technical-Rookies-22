# Write your code here
if y1 > y2:
    fine = 10000
elif m1 > m2 and y1 == y2:
    fine = 500 * (m1 - m2)
elif d1 > d2 and m1 == m2 and y1 == y2:
    fine = 15 * (d1 - d2)
else:
    fine=0   
return fine
