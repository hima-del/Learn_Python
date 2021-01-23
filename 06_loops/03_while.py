i=1
while(i<6):
    print(i)
    if i==3:
#With the break statement we can stop the loop even if the while condition is true:
        break
    i=i+1
#With the continue statement we can stop the current iteration, and continue with the next:
j=0
while(j<6):
    j=j+1
    if j==3:
        continue
    print(j)           
