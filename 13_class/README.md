**Instance, Class, and Static Methods — An Overview**

```
class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'
```

**Instance Methods**

* The first method on MyClass, called method, is a regular instance method. 
* You can see the method takes one parameter, self, which points to an instance of MyClass when the method is called (but of course instance methods can accept more than just one parameter).
* Through the self parameter, instance methods can freely access attributes and other methods on the same object. 
* This gives them a lot of power when it comes to modifying an object’s state.
* Not only can they modify object state, instance methods can also access the class itself through the self.__class__ attribute. 
* This means instance methods can also modify class state.
        
