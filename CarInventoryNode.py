# CarInventoryNode.py
from Car import Car

class CarInventoryNode:

    def __init__(self, car):
        self.make = car.make
        self.model = car.model
        self.cars = [car]
        self.parent = None
        self.left = None
        self.right = None

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def getLeft(self): #hasLeftChild
        return self.left

    def isLeft(self): #isLeftChild
        return self.parent and self.parent.left == self

    def setLeft(self, left):
        self.left = left

    def getRight(self): #hasRightChild
        return self.right

    def isRight(self): #isRightChild
        return self.parent and self.parent.right == self
    
    def setRight(self, right):
        self.right = right

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.right or self.left)

    def hasAnyChildren(self):
        return self.right or self.left

    def hasBothChildren(self):
        return self.right and self.left

    def replaceNodeData(self, make, model, cars, left, right):
        self.make = make
        self.model = model
        self.cars = cars
        self.left = left
        self.right = right
        if self.getLeft():
            self.left.parent = self
        if self.getRight():
            self.right.parent = self
            
        
    def __str__(self):
        s = ""
        for car in self.cars:
            s += str(car) + "\n"
        return s


    def spliceOut(self):
        if self.isLeaf():
            if self.isLeft():
                self.parent.left = None
            else:
                self.parent.right = None   
        elif self.hasAnyChildren():
            if self.getLeft():
                if self.isLeft():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:
                if self.isLeft():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent


