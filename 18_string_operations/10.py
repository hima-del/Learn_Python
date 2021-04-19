x = ("a","b","c")

my_dict = dict.fromkeys(x)
print(my_dict)

car = {
    "model" : "BMW",
    "color" : "black",
    "year" : 1990
}

x = car.get("year")
print(x)
print(car.items())
print(car.keys())
print(car.values())
