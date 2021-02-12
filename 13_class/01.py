class Dog:
    species="canis familiaris"

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self,sound):
        return f"{self.name} saying {sound}"

class Bulldog(Dog):
    pass

jack=Bulldog("jack",9)
print(jack)
print(jack.speak("bow bow"))

#print(isinstance(jack,Dog))

class JackRussellTerrier(Dog):
    def speak(self,sound="arf"):
        return f"{self.name} says {sound}"
                    
miles=JackRussellTerrier("miles",9)
print(miles)
print(miles.speak())

class NewDog(Dog):
    def speak(self,sound="aoww"):
        return super().speak(sound)

jenn=NewDog("jenn",10)
print(jenn)
print(jenn.speak())