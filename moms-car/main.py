
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
        return (str(self.low) + " to " + str(self.high))

class car:

    def __init__(self,make,model,trunk_space,reliability,price):
        self.make = make
        self.model = model
        self.trunk_space = Trunk_space(trunk_space[0],trunk_space[1])
        self.reliability = reliability 
        self.price = Price(price[0],price[1])

    def to_string(self):
        return (self.make + " " + self.model)

    def to_string_full(self):
        res = self.make + " " + self.model
        res += "\n\tPrice: " + self.price.to_string()
        res += "\n\tTrunk Space: " + self.trunk_space.to_string()
        res += "\n\tReliabiltiy: " + str(self.reliability) + "\n"
        return res

    def get_val(self,xval):
        if xval == "price":
            return self.price.to_string()
        if xval == "trunk_space":
            return self.trunk_space.to_string()
        if xval == "reliability":
            return str(self.reliability)
        return "ERROR"

        
cars = []
cars.append(car("Kia","Telluride",[21,87],85,[36,51]))
#trunk space - 21 - 87
#reliability score - 85
#price - 36 - 51
cars.append(car("Buick","Enclave",[24,97],85,[44,57]))
#trunk space - 24 - 97
#reliability score - 85
#price - 44 - 57
cars.append(car("Volkswagen","Atlas",[21,97],73,[38,51]))
#trunk space - 21 - 97
#reliability score - 73
#price - 38 - 51
cars.append(car("Honda","Pilot",[19,87],80,[40,54]))
#trunk space - 19 - 87
#reliability score - 80
#price - 40 - 54
cars.append(car("Honda","Passport",[51,101],85,[42,48]))
#trunk space - 51 - 101
#reliability score - 85
#price - 42 - 48
cars.append(car("Subaru","Ascent",[18,76],82,[34,42]))
#trunk space - 18 - 76
#reliability score - 82
#price - 34 - 42
cars.append(car("Toyota","Highlander",[16,84],79,[39,46]))
#trunk space - 16 - 84 
#reliability score - 79
#price - 39 - 46
cars.append(car("Acura","MDX",[18,95],79,[50,64]))
#trunk space - 18 - 95
#reliability score - 79
#price - 50 - 64
cars.append(car("Nissan","Armada",[17,92],79,[56,68]))
#trunk space - 17 - 92
#reliability score - 79
#price - 56 - 68
cars.append(car("Hyundai","Santa Fe",[15,80],83,[34,43]))
#trunk space - 15 - 80
#reliability score - 83
#price - 34 - 43
cars.append(car("GMC","Yukon XL",[42,155],80,[61,78]))
#trunk space - 42 - 144.7
#reliability score - 80
#price - 61 - 78
cars.append(car("GMC","Acadia",[23,98],84,[43,54]))
#trunk space - 23 - 98
#reliability score - 84
#price - 43 - 54
cars.append(car("Dodge","Durango",[17,85],-1,[40,52]))
#trunk space -  17 - 85
#reliability score - 0
#price - 40 - 52
cars.append(car("Infinity","QX60",[15,75],75,[50,63]))
#trunk space -  15-75
#reliability score - 75
#price - 50 - 63
cars.append(car("Ford","Explorer",[16,86],82,[37,55]))

cars_by_price = sorted(cars,key=lambda x: x.price.low)
cars_by_cargo = sorted(cars,key=lambda x: x.trunk_space.high,reverse=True)
cars_by_reliability = sorted(cars,key=lambda x: x.reliability,reverse=True)

json_string = "{\n\t\"array\":\n\t\t[";

def make_section(ol_id,car_list,xval):
    entry = "[\"" + ol_id + "\", ["
    for car in car_list:
        entry += "[\"" + car.to_string() + "\",\"" + car.get_val(xval) + "\"],"
    entry = entry[:-1] + "]],\n"
    return entry


json_string += make_section("price_list",cars_by_price,"price")
json_string += make_section("cargo_list",cars_by_cargo,"trunk_space")
json_string += make_section("reliabiliy_list",cars_by_reliability,"reliability")

json_string = json_string[:-2] + "]\n}"

data_file = open("data.json","w")
data_file.write(json_string)
data_file.close()





