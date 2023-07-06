# Car.py

class Car:

    def __init__(self, make, model, year, price):
        self.make = make.upper()
        self.model = model.upper()
        self.year = year
        self.price = price

    def equalityChecker(self, rhs):
        if self.make < rhs.make:
            return "less"
        elif self.make > rhs.make:
            return "greater"

        if self.model < rhs.model:
            return "less"
        elif self.model > rhs.model:
            return "greater"

        if self.year < rhs.year:
            return "less"
        elif self.year > rhs.year:
            return "greater"

        if self.price < rhs.price:
            return "less"
        elif self.price > rhs.price:
            return "greater"
        else:
            return "same"
        
    def __gt__(self, rhs):
        return self.equalityChecker(rhs) == "greater"

    def __lt__(self, rhs):
        return self.equalityChecker(rhs) == "less"

    def __eq__(self, rhs):
        if rhs == None:
            return False
        return self.equalityChecker(rhs) == "same"

    def __str__(self):
        return "Make: {}, Model: {}, Year: {}, Price: ${}"\
               .format(self.make, self.model, self.year, self.price)



        



        
