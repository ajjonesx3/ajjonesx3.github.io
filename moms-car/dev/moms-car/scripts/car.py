class Price:

    def __init__(self,low,high):
        self.low = low
        self.high = high
    
    def to_string(self):
        return ("$" + str(self.low) + "k to $" + str(self.high) + "k")

class Cargo:

    def __init__(self,low,high):
        self.low = low
        self.high = high
    
    def to_string(self):
        return (str(self.low) + " | " + str(self.high))

class car:

    def __init__(self,make,model,cargo,reliability,price):

        self.data = {}
        self.data["make"] = make
        self.data["model"] = model
        self.data["cargo"] = Cargo(cargo[0],cargo[1])
        self.data["reliability"] = reliability
        self.data["price"] = Price(price[0],price[1])
        self.data["total"] = 0

    def to_string(self):
        return (self.data["model"] + " " + self.data["make"])

def calculate_total(value,car_list):
    cll = len(car_list)
    mx = cll / 10
    v = value * mx
    for i in range(cll):
        n = cll -i
        car_list[i].total += n * v

