#lambda_fun = lambda y : y*y*y
#print(lambda_fun(10))

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(filter(lambda x : (x%2!=0),li))
print(final_list)

ages = [13, 90, 17, 59, 21, 60, 5]
adults = list(filter(lambda x : x>18,ages))
print(adults)

li2 = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
my_list = list(map(lambda x : x*2,li2))
print(my_list)

animals = ['dog', 'cat', 'parrot', 'rabbit']
uppered_animals = list(map(lambda animal:str.upper(animal),animals))
print(uppered_animals)  