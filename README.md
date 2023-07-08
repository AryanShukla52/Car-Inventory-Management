# CarInventoryManagement

This is a script


In this lab, you'll have the opportunity to practice:

* Defining classes in Python
* Overloading the `==`, `<`, and `>` operators in a Python class
* Implementing and applying the Binary Search Tree (BST) data structure
* Writing functions that ensure Car objects are in sorted order
* Testing your functionality with pytest

**Note:** This lab will be broken down into two separate labs. It is important that you start this lab early so you can utilize our office hours to seek assistance / ask clarifying questions during the weekdays before the deadline if needed as the first part will be used in the second part!

# Introduction

The purpose of this project was to create a program that will manage cars for a used car dealership. All cars have a make, model, year, and price, which can be used to determine the value of cars in relation to each other. All cars will be managed by a Binary Search Tree (BST) where the nodes are sorted by make, then model in lexicographical order. Within each make/model node, the `Car` objects will be added to a Python List based on insertion order.

In order to manage the cars, I defined `Car`, `CarInventoryNode` and `CarInventory` classes that organize the Cars into a BST data structure. Cars with the same make/model are located in the same node, and appended to a list based on insertion order.

I also wrote pytests in `testFile.py` to illustrate that the behavior of the program is working as anticipated.

# Components

This project comprises of four different files:
* `Car.py` - Defines a Car class. This class will assume all Cars have a `make`(str), `model`(str), `year`(int), and a `price`(int).
* `CarInventoryNode.py` - Defines a BST Node class containing all fields for a BST Node and a Python List collection of Car objects.
* `CarInventory.py` - Defines a CarInventory (BST) class that is an ordered collection of a Dealership's Cars.
* `testFile.py` - This file contains pytest functions that test the overall correctness of the class definitions.

# Car.py

The `Car.py` file contains the definition of a `Car` class. The `Car` class holds information about the cars (`make`, `model`, `year`, and `price`). The `Car` attributes are defined as follows:

* `make` - string value representing the brand of the car (eg. `Nissan`, `Tesla`, `Toyota`, `Ferrari`). The program stores this attribute in uppercase characters
* `model` - string value representing the model of the car (eg. `Electra`, `Model3`, `Prius`, `Portofino`). The program stores this attribute in uppercase characters
* `year` - integer value representing the year of the car (eg. 2010, 2000, 1963)
* `price` - integer value representing the price value of the car (eg. 20000, 30000, 25000)

I created a constructor that allows the user to construct a `Car` object by passing in values for the `make`, `model`, `year`, and `price`.

* `__init__(self, make, model, year, price)`

I also overloaded the operators to fit the purpose of this project:
* `__gt__(self, rhs)` - this comparator operator checks if a `Car` object is greater than another `Car` object. `Car` objects are first organized by the lexicographical/alphabetical order of their `make` attribute. If the `make` attribute is the same, then they'll be determined by the lexicographical/alphabetical order of their `model` attribute. If the `model` attribute is the same, then they are organized by the year (from least-to-greatest). If the year is the same, then the they are organized by their price (from least-to-greatest). For example, if both `Car2` and `Car1` have the same `make` and `model`, then `Car2 > Car1` if `Car2` is newer; if `Car2` and `Car1` have the same `year` as well, then `Car2 > Car1` if `Car2` is more expensive.
* `__lt__(self, rhs)` - this comparator operator checks that a `Car` object is less than another `Car` object via the operation `Car1 < Car2` according to the specifications above.
* `__eq__(self, rhs)` - this comparator operator checks that a `Car` object is equivalent to another `Car` (both cars have the same `make`, `model`, `year`, and `price`) via the operation `Car1 == Car2`.
* `__str__(self)` - this is an overload method that returns the details of a car via the operation `str(Car1)`. The string representation will appear in the following format: `"Make: [make], Model: [model], Year: [year], Price: $[price]"`. 

For example:

```
c = Car("Honda", "CRV", 2007, 8000)
print(c)
```
**Output:**
```
Make: HONDA, Model: CRV, Year: 2007, Price: $8000
```

# CarInventoryNode.py

The `CarInventoryNode.py` file contains the definition of a `CarInventoryNode` class, which is the node for a BST.

The `CarInventoryNode` class has the following attributes:

* `make` - string value that represents the make of the car.
* `model` - string value that represents the model of the car.
* `cars` - a Python List that contains `Car` objects that have the same `make` and `model`. `Car` objects are organized in insertion order (most recently inserted `Car` exists at the end of the Python List).
* `parent` - a reference to the parent of a `CarInventoryNode`, `None` if it has no parent (it is the root).
* `left` - a reference to the left child of a `CarInventoryNode`, `None` if it has no left child.
* `right` - a reference to the right child of a `CarInventoryNode`, `None` if it has no right child.

The `CarInventoryNode` class also defines the following methods:

* `__init__(self, car)` - the constructor for the `CarInventoryNode` takes in a `Car` object, and initializes all attributes in the `CarInventoryNode`. The constructor also appends the parameter `Car` object from the parameter into the list attribute `cars`.

Some other methods that were also implemented to facilitate the functionality of the BST:
* `getMake(self)` - returns a string containing the `make` of a `CarInventoryNode`.
* `getModel(self)` - returns a string containing the `model` of a `CarInventoryNode`.
* `getParent(self)` - returns the `parent` Node of the `CarInventoryNode`. If the parent does not exist, return `None`.
* `setParent(self, parent)` - sets the `parent` Node of the `CarInventoryNode`.
* `getLeft(self)` - returns the left child of the `CarInventoryNode`. If the left child does not exist, return `None`.
* `setLeft(self, left)` - sets the left child of the `CarInventoryNode`.
* `getRight(self)` - returns the right child of the `CarInventoryNode`. If the right child does not exist, return `None`.
* `setRight(self, right)` - sets the right child of the `CarInventoryNode`.
* `__str__(self)` - overloads the string operator to provide the details of all cars in the `CarInventoryNode` (eg, `str(CarNode1)`). The string representation contains all the `Car` objects in this `CarInventoryNode` in insertion order. Each car is separated with a newline character (`\n`) (including the last `Car` object in the cars Python List).

For example:

```
car1 = Car("Dodge", "dart", 2015, 6000)
car2 = Car("dodge", "DaRt", 2003, 5000)
carNode = CarInventoryNode(car1)
carNode.cars.append(car2)
print(carNode)
```
**Output:** (note the extra newline)
```
Make: DODGE, Model: DART, Year: 2015, Price: $6000
Make: DODGE, Model: DART, Year: 2003, Price: $5000

```

# CarInventory.py

The `CarInventory.py` file contains the definition of a `CarInventory` class. It manages the `CarInventoryNode`s and keeps track of all the cars a dealership has. The `CarInventory` is implemented as a BST. The `CarInventory` creates and manages `CarInventoryNode` objects based on a car's `make` and `model` attributes. When storing `Car` objects in the `CarInventory`, `Car` objects with the same `make` and `model` will be appended to a Python List based on insertion order within the `CarInventoryNode` object.

* `__init__(self)` - the constructor for the `CarInventory` initializes the empty BST. There is an attribute called `root` that represents the root node of the `CarInventory` BST.

Other methods that were implemented in this class include:

* `addCar(self, car)` - adds a `Car` object to the BST. If a `CarInventoryNode` with the same `make` and `model` exists, then it appends the car to the end of its car list.
* `doesCarExist(self, car)` - searches for a `Car` object in the `CarInventory` by traversing to the appropriate `CarInventoryNode` (if it exists), and checks the `cars` Python List to see if any `Car` object is equal to the parameter `car`. This method returns `True` if it does, and returns `False` otherwise (i.e. no `Car` object with the same `make`, `model`, `year`, and `price` exists).
* `inOrder(self)` - returns a string with the in-order traversal of the BST. Printing the in-order traversal should help check that the cars are in the correct order in the BST
* `preOrder(self)` - returns a string with the pre-order traversal of the BST. BSTs with the same structure should always have the same pre-order traversal, so this can be used to verify that everything was inserted correctly
* `postOrder(self)` - returns a string with the post-order traversal of the BST.
* `getBestCar(self, make, model)` - returns the `Car` with the newest year - and if multiple, then highest price - given the make and model. If the make and model doesn't exist, it returns None.
* `getWorstCar(self, make, model)` - returns the car with the oldest year - and if multiple, then lowest price - given the make and model. If the make and model doesn't exist, then it returns None.
* `getTotalInventoryPrice(self)` - returns an integer of the total price of all the cars in the dealership. 

Given an example BST:

```python
bst = CarInventory()

car1 = Car("Nissan", "Leaf", 2018, 18000)
car2 = Car("Tesla", "Model3", 2018, 50000)
car3 = Car("Mercedes", "Sprinter", 2022, 40000)
car4 = Car("Mercedes", "Sprinter", 2014, 25000)
car5 = Car("Ford", "Ranger", 2021, 25000)

bst.addCar(car1)
bst.addCar(car2)
bst.addCar(car3)
bst.addCar(car4)
bst.addCar(car5)
```

An example of the traversal functions is given below:
```python
assert bst.getBestCar("Nissan", "Leaf") == car1
assert bst.getBestCar("Mercedes", "Sprinter") == car3
assert bst.getBestCar("Honda", "Accord") == None

assert bst.getWorstCar("Nissan", "Leaf") == car1
assert bst.getWorstCar("Mercedes", "Sprinter") == car4
assert bst.getBestCar("Honda", "Accord") == None

assert bst.getTotalInventoryPrice() == 158000
```

An example of the `inOrder()` string format is given below:

```python
assert bst.inOrder() == \
"""\
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
```

An example of the `preOrder()` string format is given below:

```python
assert bst.preOrder() == \
"""\
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
```

An example of the `postOrder()` string format is given below:
```python
assert bst.postOrder() == \
"""\
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
"""
```

# testFile.py

This file tests all of the classes and required methods using pytest. 

# Next Part of the Lab

In this lab, you'll have the opportunity to practice:

* Modifying classes in Python
* Further implementing Binary Search Tree (BST) data structure supporting removal functionality
* Testing your functionality with pytest

**Note:** This lab will be dependent on your previous lab. Certain tests from the previous lab will be autograded in this week's lab. It is important that you start this lab early so you can utilize our office hours to seek assistance / ask clarifying questions during the weekdays before the deadline if needed!

# Introduction

The goal for this lab is to take your existing Used Car Lot program in Lab08 that will manage cars for a second-hand car dealership, and support removing Cars from the lot. As a reminder, all Cars have a `make`, `model`, `year`, and `price`, which can be used to determine the value of cars in relation to each other. All Cars will be managed with a Binary Search Tree (BST) where the BST nodes are sorted by `make`, then `model`.

In order to remove the cars for this lab, you will define a `removeCar` method in the `CarInventory` class that will remove Cars with the same `make`/`model`/`year`/`price` from a `CarInventoryNode`'s cars list. After removing a Car and no cars exist in the `CarInventoryNode`'s cars list, you will then need to remove the node from the BST while preserving the BST property.

You will also write pytests in `testFile.py` illustrating your behavior works correctly. This lab writeup will provide some test cases for clarity, but the Gradescope autograder will run different tests shown here. It's important to thoroughly test your program with various cases!

# Instructions

You will need to copy over all your files for Lab08 and modify two files:
* `CarInventory.py` - Defines a CarInventory (BST) class that is an ordered collection of a Dealership's Cars. You will be adding to your existing `CarInventory` class. 
* `testFile.py` - This file will contain your pytest functions that tests the overall correctness of your class definitions.

Your starter code for this assignment will be your program from Lab08, and you'll have to add the additional specifications defined below.

You should organize your lab work in its own directory. This way all files for a lab are located in a single folder. Also, this will be easy to import various files into your code using the `import / from` technique shown in lecture. 

# CarInventory.py

The `CarInventory.py` file will contain the definition of a `CarInventory` class. This will keep track of the cars a dealership has, implemented as a BST. The `CarInventory` will create `CarInventoryNode` objects using `Car` objects based on their `make` and `model`. `Car` objects with the same make and model will be appended to a list based on insertion order within the `CarInventoryNode` object. For further specifications regarding existing requirements, reference the Lab08 page.

In addition to the methods created before, the following methods are required to be implemented:

* `getSuccessor(self, make, model)` - attempts to finds the `CarInventoryNode` with the `make` and `model`, and returns the CarInventoryNode with the next greatest value (using the same heirarchy of `make`, then `model`). Returns `None` if there is no `CarInventoryNode` with the specified `make` and `model`, or if the `CarInventoryNode` is the maximum and has no successor. **Note, this includes the successor of any `CarInventoryNode` in the BST if it exists, not just the successor used for BST maintenance.**
* `removeCar(self, make, model, year, price)` - attempts to find the `Car` with the specified `make`, `model`, `year`, and `price`, and removes it the `CarInventoryNode`'s cars list. If the list is empty after removing the `Car`, remove the `CarInventoryNode` from the BST entirely. Returns `True` if the `Car` was successfully removed, and `False` if the `Car` is not present in the `CarInventory`. If there are duplicate cars within a `CarInventoryNode`'s car list that matches the specifications, you will just remove the first matching `Car` object in the cars list.

**A note if you have implemented `CarInventoryNode` comparators:** If you have implemented `CarInventoryNode` comparators in last week's lab, in your `__eq__` comparator overload, before you check for the `make` and the `model`, you should check if the right-hand-side is `None`. If it is `None`, you should return `False`. This is because of a quirk about how Python handles comparators between overloaded comparators and `None`.

# Examples

Given an example BST:

```python
bst = CarInventory()

car1 = Car("Mazda", "CX-5", 2022, 25000)
car2 = Car("Tesla", "Model3", 2018, 50000)
car3 = Car("BMW", "X5", 2022, 60000)
car4 = Car("BMW", "X5", 2020, 58000)
car5 = Car("Audi", "A3", 2021, 25000)

bst.addCar(car1)
bst.addCar(car2)
bst.addCar(car3)
bst.addCar(car4)
bst.addCar(car5)

#                                  Mazda,CX-5,[Car(Mazda,CX-5,2022,25000)]
#                                 /                                       \
#           BMW,X5,[Car(BMW,X5,2022,60000),Car(BMW,X5,2020,58000)]    Tesla,Model3,[Car(Tesla, Model3,2018,50000)]
#                   /
#  Audi,A3,[Car(Audi,A3,2021,25000)]
```

### InOrder Traversal

Using the `CarInventory` after the `addCar` methods above, an example of the `inOrder()` string format for removal is given below after removing the following Car:

```python

bst.removeCar("BMW", "X5", 2020, 58000)

#                                  Mazda,CX-5,[Car(Mazda,CX-5,2022,25000)]
#                                 /                                       \
#           BMW,X5,[Car(BMW,X5,2022,60000)]    Tesla,Model3,[Car(Tesla,Model3,2018,50000)]
#                   /
#  Audi,A3,[Car(Audi,A3,2021,25000)]

assert bst.inOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: BMW, Model: X5, Year: 2022, Price: $60000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
```

and if we then remove the following car, the `CarInventoryNode` will be removed from the BST. The `CarInventory` and `inOrder()` string format is given below in this case:

```python
bst.removeCar("BMW", "X5", 2022, 60000)

#                                  Mazda,CX-5,[Car(Mazda,CX-5,2022,25000)]
#                                 /                                       \
#           Audi,A3,[Car(Audi,A3,2021,25000)]    Tesla,Model3,[Car(Tesla,Model3,2018,50000)]


assert bst.inOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
```

### PreOrder Traversal

Using the `CarInventory` after the `addCar` methods above, an example of the `preOrder()` string format is given below after removing the following Cars:

```python

bst.removeCar("BMW", "X5", 2020, 58000)

#                                  Mazda,CX-5,[Car(Mazda,CX-5,2022,25000)]
#                                 /                                       \
#           BMW,X5,[Car(BMW,X5,2022,60000)]    Tesla,Model3,[Car(Tesla,Model3,2018,50000)]
#                   /
#  Audi,A3,[Car(Audi,A3,2021,25000)]

assert bst.preOrder() == \
"""\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: BMW, Model: X5, Year: 2022, Price: $60000
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""

bst.removeCar("BMW", "X5", 2022, 60000)

#                                  Mazda,CX-5,[Car(Mazda,CX-5,2022,25000)]
#                                 /                                       \
#           Audi,A3,[Car(Audi,A3,2021,25000)]    Tesla,Model3,[Car(Tesla,Model3,2018,50000)]


assert bst.preOrder() == \
"""\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
```

### PostOrder Traversal

Using the `CarInventory` after the `addCar` methods above, an example of the `postOrder()` string format is given below after removing the following Cars:

```python

bst.removeCar("BMW", "X5", 2020, 58000)

#                                  Mazda,CX-5,[Car(Mazda,CX-5,2022,25000)]
#                                 /                                       \
#           BMW,X5,[Car(BMW,X5,2022,60000)]    Tesla,Model3,[Car(Tesla,Model3,2018,50000)]
#                   /
#  Audi,A3,[Car(Audi,A3,2021,25000)]

assert bst.postOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: BMW, Model: X5, Year: 2022, Price: $60000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
"""

bst.removeCar("BMW", "X5", 2022, 60000)

#                                  Mazda,CX-5,[Car(Mazda,CX-5,2022,25000)]
#                                 /                                       \
#           Audi,A3,[Car(Audi,A3,2021,25000)]    Tesla,Model3,[Car(Tesla,Model3,2018,50000)]


assert bst.postOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
"""
```

These are just a few simple examples illustrating the functionality of removing a Car from the `CarInventory` cars list, and removing the `CarInventoryNode` from the `CarInventory`. Gradescope will thoroughly test various cases. As always, it's important to thoroughly test your own code with various possible cases.

Other than the required methods, feel free to implement any helper methods that you think are useful in your implementation. The automated tests will test only your implementation of the required methods and certain methods from last week by creating a `CarInventory` containing various `Cars` with different `make`, `model`, `year`, and `price` attributes. The `removeCar()` and `addCar()` methods will be run, with `getCar()`, `getSuccessor()`, `inOrder()`, `preOrder()`, and `postOrder()` being used to verify that the `CarInventory` is fully functional. You should be sure that Lab08 is working correctly, and write tests to confirm your program for this lab is working properly.

# testFile.py

This file should test all of the new methods in `CarInventory.py` using pytest. Think of various scenarios and edge cases when testing your code according to the given descriptions. For the `getSuccessor` method, your tests should test the general case and the case used for BST maintenance. For the `removeCar` method, you tests should cover Cases 1, 2, and 3 (as discussed in lecture) at a minimum, as well as only removing a Car from the `CarInventoryNode`'s cars list without removing the `CarInventoryNode`. Even though Gradescope will not use this file when running automated tests (Gradescope will use other tests), it is important to provide this file with various test cases (testing is important!!).

**A note about Gradescope tests:** Gradescope will use your functions to correctly check the state of your `Car`s and `CarInventory` with many scenarios. In order to test if everything is in the correct state, these tests use your CarInventory's `preOrder` / `inOrder` / `postOrder` traversals and `addCar` methods, as well as getting the string representation of your `Car`s and `CarInventoryNode`s to run other tests. It is important to ensure your `preOrder` / `inOrder` / `postOrder` traversals, your various string representations, and `CarInventory`'s `addCar` methods work correctly first or else many of the other tests may not pass.

Of course, feel free to reach out / post questions on Piazza as they come up!

# Submission

Once you're done with writing your class definitions and tests, submit the following files to Gradescope's Lab09 assignment:

* `Car.py` 
* `CarInventoryNode.py`
* `CarInventory.py`
* `testFile.py`

There will be various unit tests Gradescope will run to ensure your code is working correctly based on the specifications given in this lab.

If the tests don't pass, you may get some error message that may or may not be obvious at this point. Don't worry - take a minute to think about what may have caused the error. Try writing more test cases to see if you're able to reproduce the problem. If you're still not sure why you're getting the error, feel free to ask your TAs or Learning Assistants.

<sup>* Lab09 created by Priyanka Banerjee and Xingbu Qin, and adapted / updated by Richert Wang (S22)</sup>
