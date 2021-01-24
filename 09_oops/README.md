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
