**Built-in Data Types**

```
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
```

**The range() Function**

* The `range()` function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

```
for x in range(6):
  print(x)
```  

**Iterators in Python**

* Iterator in Python is simply an object that can be iterated upon. 
* An object which will return data, one element at a time.
* Technically speaking, a Python iterator object must implement two special methods, `__iter__()` and `__next__()`, collectively called the iterator protocol.
* An object is called iterable if we can get an iterator from it. 
* Most built-in containers in Python like: list, tuple, string etc. are iterables.
* The `iter()` function (which in turn calls the `__iter__()` method) returns an iterator from them
  

**Python Collections (Arrays)**

* There are four collection data types in the Python programming language:
```
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered and changeable. No duplicate members.
```


**List Methods**

*Python has a set of built-in methods that you can use on lists.
```
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
```

**Tuple Methods**

* Python has two built-in methods that you can use on tuples.

```
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
```

**Set Methods**

* Python has a set of built-in methods that you can use on sets.

```
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others
```

**Dictionary Methods**

* Python has a set of built-in methods that you can use on dictionaries.

```
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
```

**Python break and continue statements**

* The Python break statement immediately terminates a loop entirely. 
* Program execution proceeds to the first statement following the loop body.

* The Python continue statement immediately terminates the current loop iteration.
* Execution jumps to the top of the loop, and the controlling expression is re-evaluated to determine whether the loop will execute again or terminate.

!(https://github.com/hima-del/Learn_Python/blob/master/06_loops/images/t.webp)


**What are lambda functions in Python?**

* Normal functions are defined using the def keyword in Python, anonymous functions are defined using the lambda keyword.
* Anonymous functions are also called lambda functions.

* Syntax of Lambda Function in python

```
lambda arguments: expression
```

**The try and except Block: Handling Exceptions**

* The try and except block in Python is used to catch and handle exceptions.
* Python executes code following the try statement as a “normal” part of the program.
* The code that follows the except statement is the program’s response to any exceptions in the preceding try clause.


```
try:
    <do something>
except Exception:
    <handle the error>
 ```
 
* try: the code with the exception(s) to catch. If an exception is raised, it jumps straight into the except block.
* except: this code is only executed if an exception occured in the try block. The except block is required with a try block, even if it contains only the pass statement.
* else: Code in the else block is only executed if no exceptions were raised in the try block.
* finally: The code in the finally block is always executed, regardless of if a an exception was raised or not
    
