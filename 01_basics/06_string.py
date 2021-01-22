a="hello world"
print(a[1])
print(a[0])
for x in a:
    print(x)
print(len(a))    
text="fly like eagles"
print("like"in text)
if "fly" in text:
    print("yes, fly is present") 
if "from"not in text:
    print("yes, from is not present")  
print(text[2:5])      
#string format
age=36
txt="my name is john and I am {}"
print(txt.format(age))