* Using a class lets you bundle behavior and state together in an object.
* When you hear the word behavior, think function—that is, a chunk of code that does something
* When you hear the word state, think variables—that is, a place to store values within a class. 
* When we assert that a class bundles behavior and state together, we’re simply stating that a class packages functions and variables
* To use a class, you create an object from it 
* This is known as object instantiation.
* When you hear the word instantiate, think invoke; that is, you invoke a class to create an object.
*  creating an object from a class looks very much like calling a function: 
* We begin by creating an empty class called CountFromBy

```
>>> class CountFromBy:
 pass
 ```
 * let’s create two objects from it, one called a and another called b. 
 * Note how creating an object from a class looks very much like calling a function:
```
>>> a = CountFromBy()
>>> b = CountFromBy() 
```
* Classes start with the “class” keyword. 
* Create an object by appending parentheses to the class name, then assign the newly created object to a variable.
* When you create objects from a class, each object shares the class’s coded behaviors (the methods defined in the class), but maintains its own copy of any state (the            attributes):
* Behavior:  Methods (shared with all objects created from the same class)
* State : Attributes (*not* shared with other objects created from the same class)
* Each object created from the same class can access the class’s methods (the shared code). 
* However, each object maintains its own copy of the attributes.
* Class behavior is shared by each of its objects, whereas state is not. 
* Each object maintains its own state


* A class is a blueprint for how something should be defined. 
* It doesn’t actually contain any data. 
* The Dog class specifies that a name and an age are necessary for defining a dog, but it doesn’t contain the name or age of any specific dog.
* An instance is an object that is built from a class and contains real data. 
* An instance of the Dog class is not a blueprint anymore.
* It’s an actual dog with a name, like Miles, who’s four years old.
* Put another way, a class is like a form or questionnaire.
* An instance is like a form that has been filled out with information. 
* Just like many people can fill out the same form with their own unique information, many instances can be created from a single class.

* The properties that all Dog objects must have are defined in a method called `__init__()`
* Every time a new Dog object is created, `__init__()` sets the initial state of the object by assigning the values of the object’s properties. 
* `__init__()` initializes each new instance of the class.
* You can give `__init__()` any number of parameters, but the first parameter will always be a variable called `self`. 
* When a new class instance is created, the instance is automatically passed to the `self` parameter in `__init__()` so that new attributes can be defined on the object.
* Attributes created in `__init__()` are called instance attributes. 
* An instance attribute’s value is specific to a particular instance of the class.
* All Dog objects have a name and an age, but the values for the name and age attributes will vary depending on the Dog instance.
* Class attributes are attributes that have the same value for all class instances. 
* You can define a class attribute by assigning a value to a variable name outside of `__init__()`
