class Dog:
    #class attribute
    species="Canis familiaris"
    def __init__(self,name,age):
        self.name=name
        self.age=age
budddy=Dog("buddy",9)
miles=Dog("miles",4)
print(budddy.name)
print(miles.age)
budddy.age=12
print(budddy.age)