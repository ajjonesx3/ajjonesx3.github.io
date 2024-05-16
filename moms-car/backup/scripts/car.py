class Price:

    def __init__(self,low,high):
        self.low = low
        self.high = high
        self.sort_variable = low
    
    def to_string(self):
        return ("$" + str(self.low) + "k to $" + str(self.high) + "k")
        return self.low

class Cargo:

    def __init__(self,low,high):
        self.low = low
        self.high = high
        self.sort_variable = high
    
    def to_string(self):
        return (str(self.low) + " | " + str(self.high))


class Reliability:

    def __init__(self,val):
        self.val = val
        self.sort_variable = val

    def to_string(self):
        return str(self.val)

class Total:

    def __init__(self):
        self.score = 0
        self.sort_variable = self.score 

        self.values = {}
        self.values["cargo"] = 8
        self.values["price"] = 7
        self.values["reliability"] = 4

    def to_string(self):
        return str(self.score)
    

class car:

    def __init__(self,make,model,cargo,reliability,price):

        self.data = {}
        self.data["make"] = make
        self.data["model"] = model
        self.data["cargo"] = Cargo(cargo[0],cargo[1])
        self.data["reliability"] = Reliability(reliability)
        self.data["price"] = Price(price[0],price[1])
        self.data["total"] = Total() 

    def to_string(self):
        return (self.data["make"] + " " + self.data["model"])
