
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
        n = cll - i
        car_list[i].total += n * v

print("Creating cars...")        
cars = []
cars.append(car("Kia","Telluride",[21,87],85,[36,51]))
cars.append(car("Buick","Enclave",[24,97],85,[44,57]))
cars.append(car("Volkswagen","Atlas",[21,97],73,[38,51]))
cars.append(car("Honda","Pilot",[19,87],80,[40,54]))
cars.append(car("Honda","Passport",[51,101],85,[42,48]))
cars.append(car("Subaru","Ascent",[18,76],82,[34,42]))
cars.append(car("Toyota","Highlander",[16,84],79,[39,46]))
cars.append(car("Acura","MDX",[18,95],79,[50,64]))
cars.append(car("Nissan","Armada",[17,92],79,[56,68]))
cars.append(car("Hyundai","Santa Fe",[15,80],83,[34,43]))
cars.append(car("GMC","Yukon XL",[42,155],80,[61,78]))
cars.append(car("GMC","Acadia",[23,98],84,[43,54]))
cars.append(car("Dodge","Durango",[17,85],-1,[40,52]))
cars.append(car("Infinity","QX60",[15,75],75,[50,63]))
cars.append(car("Ford","Explorer",[16,86],82,[37,55]))
print("  Done")

print("Creating and sorting lists...")
cars_by_price = sorted(cars,key=lambda x: x.price.low)
cars_by_cargo = sorted(cars,key=lambda x: x.trunk_space.high,reverse=True)
cars_by_reliability = sorted(cars,key=lambda x: x.reliability,reverse=True)
print("  Done")

print("Calculating totals...")

price_value = 0
cargo_value = 0
reliability_value = 9


for car in cars_by_price:
    calculate_total(price_value,cars_by_price)
for car in cars_by_cargo:
    calculate_total(cargo_value,cars_by_cargo)
for car in cars_by_reliability:
    calculate_total(reliability_value,cars_by_reliability)

cars_by_total = sorted(cars,key=lambda x: x.total,reverse=True)
mx = cars_by_total[0].total / 100
for car in cars_by_total:
    car.total /= mx
    car.total = round(car.total)

print("  Done")

print("Creating json string...")

class display:

    def __init__(self):
        self.json_string = "{\n\t\"array\":\n\t\t[";

    def add_section(self,ol_id,car_list,xval):
        entry = "[\"" + ol_id + "\", ["
        for car in car_list:
            entry += "[\"" + car.to_string() + "\",\"" + car.get_val(xval) + "\"],"
        entry = entry[:-1] + "]],\n"
        self.json_string += entry

    def json(self):
        temp = self.json_string[:-2] + "]\n}"
        return temp

page_display = display()
page_display.add_section("price_list",cars_by_price,"price")
page_display.add_section("cargo_list",cars_by_cargo,"trunk_space")
page_display.add_section("reliability_list",cars_by_reliability,"reliability")

page_display.add_section("total_list",cars_by_total,"total")

print("  Done")

print("Writing json file...")

data_file = open("data.json","w")
data_file.write(page_display.json())
data_file.close()

print("  Done")
print("\n--- Data updated ---\n")

