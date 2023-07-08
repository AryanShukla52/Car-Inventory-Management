# CarInventory.py

from Car import Car
from CarInventoryNode import CarInventoryNode

class CarInventory:

    def __init__(self):
        self.root = None
        self.size = 0


    def addCar(self, car):
        if self.root == None:
            self.root = CarInventoryNode(car)
        else:
            self._addCar(car, self.root)
        self.size = self.size + 1


    def _addCar(self, car, compareCar):
        if car.make == compareCar.make and car.model == compareCar.model:
            compareCar.cars.append(car)
            return
        if car < compareCar.cars[0]:
            if compareCar.getLeft():
                self._addCar(car, compareCar.getLeft())
            else:
                carNode = CarInventoryNode(car)
                compareCar.setLeft(carNode)
                carNode.setParent(compareCar)
        else:
            if compareCar.getRight():
                self._addCar(car, compareCar.getRight())
            else:
                carNode = CarInventoryNode(car)
                compareCar.setRight(carNode)
                carNode.setParent(compareCar)


    def doesCarExist(self, car):
        if self.root == None:
            return False
        else:
            return self._doesCarExist(car, self.root)


    def _doesCarExist(self, car, compareCar):
        if (compareCar == None):
            return False
        if car.make == compareCar.make and car.model == compareCar.model:
            return car in compareCar.cars
        else:
            if car < compareCar.cars[0]:
                return self._doesCarExist(car, compareCar.left)
            else:
                return self._doesCarExist(car, compareCar.right)


    def inOrder(self):
        carsList = []
        self._inOrder(self.root, carsList)
        s = ""
        for car in carsList:
            s += str(car) + "\n"
        return s


    def _inOrder(self, node, carsList):
        if(node == None):
            return
        self._inOrder(node.getLeft(), carsList)
        for car in node.cars:
            carsList.append(str(car))
        self._inOrder(node.getRight(), carsList)
        

    def preOrder(self):
        carsList1 = []
        self._preOrder(self.root, carsList1)
        s = ""
        for car in carsList1:
            s += str(car) + "\n"
        return s


    def _preOrder(self, node, carsList1):
        if (node == None):
            return
        for car in node.cars:
            carsList1.append(str(car))
        self._preOrder(node.getLeft(), carsList1)
        self._preOrder(node.getRight(), carsList1)


    def postOrder(self):
        carsList2 = []
        self._postOrder(self.root, carsList2)
        s = ""
        for car in carsList2:
            s += str(car) + "\n"
        return s


    def _postOrder(self, node, carsList2):
        if (node == None):
            return
        self._postOrder(node.getLeft(), carsList2)
        self._postOrder(node.getRight(), carsList2)
        for car in node.cars:
            carsList2.append(str(car))
        
        
    def getBestCar(self, make, model):
        tempCar = Car(make, model, 0, 0)
        return self._getBestCar(make.upper(), model.upper(), self.root, tempCar)


    def _getBestCar(self, make, model, car, tempCar):
        if car == None:
            return None
        if make == car.make and model == car.model:

            best = car.cars[0]
            for car in car.cars:
                if car.year > best.year:
                    best = car
                elif car.year == best.year and car.price > best.price:
                    best = car
            return best
        else:
            if tempCar < car.cars[0]:
                return self._getBestCar(make, model, car.getLeft(), tempCar)
            else:
                return self._getBestCar(make, model, car.getRight(), tempCar)

            
    def getWorstCar(self, make, model):
        tempCar = Car(make, model, 0, 0)
        return self._getWorstCar(make.upper(), model.upper(), self.root, tempCar)


    def _getWorstCar(self, make, model, car, tempCar):
        if car == None:
            return None
        if make == car.make and model == car.model:

            worst = car.cars[0]
            for car in car.cars:
                if car.year < worst.year:
                    worst = car
                elif car.year == worst.year and car.price < worst.price:
                    worst = car
            return worst
        else:
            if tempCar < car.cars[0]:
                return self._getWorstCar(make, model, car.getLeft(), tempCar)
            else:
                return self._getWorstCar(make, model, car.getRight(), tempCar)


    def getTotalInventoryPrice(self):
        return  self._getTotalInventoryPrice(self.root)


    def _getTotalInventoryPrice(self, node):
        if (node == None):
            return 0
        total = 0
        for car in node.cars:
            total += car.price
        return self._getTotalInventoryPrice(node.getLeft()) + total + self._getTotalInventoryPrice(node.getRight())







    # Implementation of the second part of the project begins here
    '''
    hasRightChild = getRight
    hasLeftChild = getLeft
    isLeftChild = isLeft
    isRightChild = isRight
    leftChild = left
    rightChild = right
    '''


    def carDetails(self):
        carsList3 = []
        nodeList = []
        self._carDetails(self.root, carsList3, nodeList)
        for node in nodeList:
            print("Node:")
            print(node)
            print("Left child:")
            print(node.left)
            print("Right child:")
            print(node.right)
            print("Parent:")
            print(node.parent)
            print("End of Node")
            print()


    def _carDetails(self, node, carsList3, nodeList):
        if (node == None):
            return
        for car in node.cars:
            carsList3.append(car)
            nodeList.append(node)
        self._carDetails(node.getLeft(), carsList3, nodeList)
        self._carDetails(node.getRight(), carsList3, nodeList)

        
    def getSuccessor(self, make, model):
        previous = self.getCarInventoryNode(make.upper(), model.upper(), self.root)
        if previous == None:
            return None
        return self._getSuccessor(previous)


    def _getSuccessor(self, previous):
        # code how to find the successor
        succ = None
        if previous.getRight():
            succ = self.findMin(previous.getRight())
        else:
            
            if previous.getParent():
                if previous.isLeft():
                    succ = previous.parent
                else:
                    parent = previous.getParent()
                    pre = previous
                    while (parent != None):
                        if not pre.isRight():
                            succ = parent
                            break
                        pre = parent
                        parent = parent.getParent()
            else:
                succ = None
        return succ


    def getCarInventoryNode(self, make, model, node):
        if node  ==  None:
            return None
        if node.make == make and node.model == model:
            return node
        else:
            if Car(make, model, 0, 0) < node.cars[0]:
                return self.getCarInventoryNode(make, model, node.left)
            else:
                return self.getCarInventoryNode(make, model, node.right)


    def getCar(self, car):
        if self.root == None:
            return False
        else:
            return self._getCar(car, self.root)


    def _getCar(self, car, compareCar):
        if (compareCar == None):
            return False
        if car.make == compareCar.make and car.model == compareCar.model:
            if car in compareCar.cars:
                return compareCar
        else:
            if car < compareCar.cars[0]:
                return self._getCar(car, compareCar.left)
            else:
                return self._getCar(car, compareCar.right)

                
    def findMin(self, previous):
        current = previous
        while current.getLeft():
            current = current.left
        return current


    def removeCar(self, make, model, year, price):
        currentNode = Car(make, model, year, price)
        if self.root:
            output = self._getCar(currentNode, self.root)
            if output:

                for car in output.cars:
                    if car == currentNode:
                        output.cars.remove(car)

                if len(output.cars) == 0:

                    if self.size == 1 and output.isRoot():
                        self.root = None

                    elif output.isLeaf():
                        if output == output.parent.left:
                            output.parent.left = None
                        else:
                            output.parent.right = None

                    elif output.hasBothChildren():
                        succ = self.getSuccessor(make, model)
                        succ.spliceOut()
                        output.make = succ.make
                        output.model = succ.model
                        output.cars = succ.cars

                    else:
                        if output.getLeft():
                            if output.isLeft():
                                output.left.parent = output.parent
                                output.parent.left = output.left
                            elif output.isRight():
                                output.left.parent = output.parent
                                output.parent.right = output.left
                            else:
                                output.replaceNodeData(output.left.make,
                                                       output.left.model,
                                                       output.left.cars,
                                                       output.left.left,
                                                       output.left.right)
                        else:
                            if output.getRight():
                                if output.isLeft():
                                    output.right.parent = output.parent
                                    output.parent.left = output.right
                                elif output.isRight():
                                    output.right.parent = output.parent
                                    output.parent.right = output.right
                                else:
                                    output.replaceNodeData(output.right.make,
                                                       output.right.model,
                                                       output.right.cars,
                                                       output.right.left,
                                                       output.right.right)
                    return True
                return True
            return False
  
        
      
