# testFile.py
from Car import Car
from CarInventoryNode import CarInventoryNode
from CarInventory import CarInventory


def test_getSuccessorNone():
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

    #doesn't exist
    bst.getSuccessor("Nissan", "Leaf") == None
    #doesn't exist
    bst.getSuccessor("Audi", "Leaf") == None
    # has no successor
    bst.getSuccessor("Audi", "A3") == None
    
    

def test_failedRemove():
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

    # doesnt exist
    assert bst.removeCar("BMW", "X5", 0, 0) == False
    
def test_InOrderRemoval():
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

    assert bst.removeCar("BMW", "X5", 2020, 58000) == True
    
    assert bst.inOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: BMW, Model: X5, Year: 2022, Price: $60000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""

    assert bst.removeCar("BMW", "X5", 2022, 60000) == True

    assert bst.inOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""

def test_PreOrderRemoval():
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

    bst.removeCar("BMW", "X5", 2020, 58000)

    assert bst.preOrder() == \
"""\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: BMW, Model: X5, Year: 2022, Price: $60000
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""

    bst.removeCar("BMW", "X5", 2022, 60000)
    assert bst.preOrder() == \
"""\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""

def test_PostOrderRemoval():
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

    bst.removeCar("BMW", "X5", 2020, 58000)

    assert bst.postOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: BMW, Model: X5, Year: 2022, Price: $60000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
"""

    bst.removeCar("BMW", "X5", 2022, 60000)

    assert bst.postOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
"""



def test_debuggingwtfiswrong():
    # just random debugging space

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
    tempCar = Car("BMW", "X5", 2020, 58000)
    print(bst.getCar(tempCar))

    
    
    

    
    
    
