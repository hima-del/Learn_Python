class Dog:
    species="canis familiaris"

    def __init__(self,name,age):
        self.name=name
        self.age=age
    #instance method
    def __repr__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self,sound):
        return f"{self.name} says {sound}"

miles=Dog("miles",4)
print(miles)
#print(miles.description())          
#print(miles.speak("woof woof"))  

