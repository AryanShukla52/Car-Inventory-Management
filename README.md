# Car-Inventory-Management

Skills practiced in this project:

* Defining and modifying classes in Python
* Overloading the `==`, `<`, and `>` operators in a Python class
* Implementing and applying the Binary Search Tree (BST) data structure, including support for removal functionality
* Writing functions that ensure Car objects are in sorted order
* Testing functionality with pytest

## Part 1 of this Project

### Introduction

The purpose of this project was to create a program that will manage cars for a used car dealership. All cars have a make, model, year, and price, which can be used to determine the value of cars in relation to each other. All cars will be managed by a Binary Search Tree (BST) where the nodes are sorted by make, then model in lexicographical order. Within each make/model node, the `Car` objects will be added to a Python List based on insertion order.

In order to manage the cars, I defined `Car`, `CarInventoryNode` and `CarInventory` classes that organize the Cars into a BST data structure. Cars with the same make/model are located in the same node, and appended to a list based on insertion order.

I also wrote pytests in `testFile.py` to illustrate that the behavior of the program is working as I anticipated.

### Components

This project comprises of four different files:
* `Car.py` - Defines a Car class. This class will assume all Cars have a `make`(str), `model`(str), `year`(int), and a `price`(int).
* `CarInventoryNode.py` - Defines a BST Node class containing all fields for a BST Node and a Python List collection of Car objects.
* `CarInventory.py` - Defines a CarInventory (BST) class that is an ordered collection of a Dealership's Cars.
* `testFile.py` - This file contains pytest functions that test the overall correctness of the class definitions.

### Car.py

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

### CarInventoryNode.py

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

### CarInventory.py

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

### testFile.py

This file tests all of the classes and required methods using pytest. 

## Part 2 of the Project

In this part of the project I tookthe  existing Used Car Lot program I wrote that manages cars for a second-hand car dealership, and I added support for removing Cars from the lot.

In order to remove the cars for this lab, I defined a `removeCar` method in the `CarInventory` class that removes Cars with the same `make`/`model`/`year`/`price` from a `CarInventoryNode`'s cars list. After removing a Car and no cars exist in the `CarInventoryNode`'s cars list, the node is removed from the BST while preserving the BST property.

### Updates made to CarInventory.py

In addition to the methods created before, the following methods were added:

* `getSuccessor(self, make, model)` - finds the `CarInventoryNode` with the `make` and `model`, and returns the CarInventoryNode with the next greatest value (using the same heirarchy of `make`, then `model`). Returns `None` if there is no `CarInventoryNode` with the specified `make` and `model`, or if the `CarInventoryNode` is the maximum and has no successor. **Note, this includes the successor of any `CarInventoryNode` in the BST if it exists, not just the successor used for BST maintenance.**
* `removeCar(self, make, model, year, price)` - attempts to find the `Car` with the specified `make`, `model`, `year`, and `price`, and removes it from the `CarInventoryNode`'s cars list. If the list is empty after removing the `Car`, then it removes the `CarInventoryNode` from the BST entirely. Returns `True` if the `Car` was successfully removed, and `False` if the `Car` is not present in the `CarInventory`. If there are duplicate cars within a `CarInventoryNode`'s car list that matches the specifications, it just removes the first matching `Car` object in the cars list.

### Examples

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

#### InOrder Traversal

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

#### PreOrder Traversal

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

#### PostOrder Traversal

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

These are just a few simple examples illustrating the functionality of removing a Car from the `CarInventory` cars list, and removing the `CarInventoryNode` from the `CarInventory`.
