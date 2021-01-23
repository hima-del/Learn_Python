#A tuple is a collection which is ordered and unchangeable.
thistuple=("apple","banana","orange")
print(thistuple)
#create tuple with one item
thetuple=("apple",)
print(type(thetuple))
#the tuple() constructor
mytuple=tuple(("a","b","c","d"))
print(mytuple)
#access tuple items
print(mytuple[0])
print(mytuple[-1])
#convert tuple to list to be able to change it
x=("carrot","potato","tomato")
y=list(x)
y[1]="onion"
x=tuple(y)
print(x)
#unpacking of tuple
(red,white,yellow)=x
print(red)
print(white)
print(yellow)
#using *
(green,*violet)=x
print(green)
print(violet)
#If the asterix is added to another variable name than the last,Python will assign values to the variable until the number of values left matches the number of variables left.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green,*yellow,orange)=fruits
print(green)
print(yellow)
print(orange)