# sum of natural numbers
num = int(input("enter the number : "))

sum = 0
while(num>0):
    sum+=num
    num-=1
print("the sum is : {}".format(sum))    