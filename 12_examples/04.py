# Python3 code to demonstrate working of  
# Append Dictionary Keys and Values ( In order ) in dictionary 
# Using values() + keys() + list() 
  
# initializing dictionary 
test_dict = {"Gfg" : 1, "is" :  3, "Best" : 2} 
  
# printing original dictionary 
print("The original dictionary is : " + str(test_dict)) 
  
# + operator is used to perform adding keys and values 
res = list(test_dict.keys()) + list(test_dict.values()) 
  
# printing result  
print("The ordered keys and values : " + str(res))  