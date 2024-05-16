class Price:

    def __init__(self,low,high):
        self.low = low
        self.high = high
    
    def to_string(self):
        return ("$" + str(self.low) + "k to $" + str(self.high) + "k")

class Trunk_space:

    def __init__(self,low,high):
        self.low = low
        self.high = high
    
    def to_string(self):
        return (str(self.low) + " | " + str(self.high))

class car:

    def __init__(self,make,model,trunk_space,reliability,price):
        self.make = make
        self.model = model
        self.trunk_space = Trunk_space(trunk_space[0],trunk_space[1])
        self.reliability = reliability
        self.price = Price(price[0],price[1])
        self.total = 0
    def to_string(self):
        return (self.make + " " + self.model)

    def get_val(self,xval):
        if xval == "price":
            return self.price.to_string()
        if xval == "trunk_space":
            return self.trunk_space.to_string()
        if xval == "reliability":
            return str(self.reliability)
        if xval == "total":
            return str(self.total)
        return "ERROR"

def calculate_total(value,car_list):
    cll = len(car_list)
    mx = cll / 10
    v = value * mx
    for i in range(cll):
        n = cll -i
        car_list[i].total += n * v

