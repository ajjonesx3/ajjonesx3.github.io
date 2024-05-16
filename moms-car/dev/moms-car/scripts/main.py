from car import Price, Trunk_space, car, calculate_total
from section import section, display
    

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
cars_by_cargo = sorted(cars,key=lambda x: x.cargo.high,reverse=True)
cars_by_reliability = sorted(cars,key=lambda x: x.reliability,reverse=True)
print("  Done")

print("Calculating totals...")

price_value = 6 
cargo_value = 7 
reliability_value = 4 


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

page_display = display()
page_display.add_section(cars_by_price,"price")
page_display.add_section(cars_by_cargo,"cargo")
page_display.add_section(cars_by_reliability,"reliability")

page_display.add_section("total_list",cars_by_total,"total")

print("  Done")

print("Writing json file...")

data_file = open("data/data.json","w")
data_file.write(page_display.json())
data_file.close()

print("  Done")
print("\n--- Data updated ---\n")

