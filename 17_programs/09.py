# fibonacci series
number = int(input("enter the number"))
n1,n2 = 0,1
count = 1

if number<=0:
    print("enter a positive number")
elif number == 1:
    print("fibonacci series upto ",number,":")
    print(n1)
elif number == 2:
    print("fibonacci series upto ",number,":")
    print(n2)
else:
   # print("fibonacci series upto ",number,":")
    while(count<=number):
        #print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count +=1    
print(nth)    