fruits=["apple","orange","banana"]
#break stmnt
for x in fruits:
    #print(x)
    if x=="orange":
        break
    print(x)
#looping through string
for x in "banana":
    print(x)  
#continue stmnt
veg=["carrot","potato","tomato"]
for x in veg:
    if x=="potato":
        continue
    print(x)
#range()
for x in range(10):
    print(x)    
for x in range(10,20):
    print(x)   
for x in range(1,10,2):
    print(x)       
#The else keyword in a for loop specifies a block of code to be executed when the loop is finished
for x in range(100):
    print(x)
else:
    print("printing finished!")     
#The else block will NOT be executed if the loop is stopped by a break statement.
for x in range(6):
    if x==3:
        break
    print(x)
else:
    print("printing finished")
#nested loop
# The "inner loop" will be executed one time for each iteration of the "outer loop":
x=["a","b","c","d"]
y=["p","q","r","s"]
for i in x:
    for j in y:
        print(i,j)       
  