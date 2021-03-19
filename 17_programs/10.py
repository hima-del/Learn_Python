# fibonacci series
number = int(input("enter the number : "))
temp = number
sum = 0

while(temp>0):
    digit = temp % 10
    sum +=digit**3
    temp//=10
if sum == number:    
    print("amstrong number")
else:
    print("not amstrong number")    