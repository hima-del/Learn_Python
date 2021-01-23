set1={"a","b","c"}
set2={1,2,3}
set3=set1.union(set2)
print(set3)
#Both union() and update() will exclude any duplicate items.
#The intersection_update() method will keep only the items that are present in both sets.
x={"apple","orange","banana"}
y={"apple","cherry","mango"}
#x.intersection_update(y)
#print(x)
#z=x.intersection(y)
#print(z)
#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x.symmetric_difference_update(y)
print(x)
