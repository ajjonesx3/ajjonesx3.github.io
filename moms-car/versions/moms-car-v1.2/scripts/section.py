
class section:

    def __init__(self,cars,xval):
        
        rev = True
        if xval=="price":
            rev = False

        self.car_list = sorted(cars,key=lambda x: x.data[xval].sort_variable, reverse=rev) 


class display:

    def __init__(self,cars):
        self.json_string = "{\n\t\"array\":\n\t\t[";
        self.cars = cars
        self.sections = []

    def add_section(self,xval):

        ol_id = xval +  "_list"
        cur_section = section(self.cars,xval)
        self.sections.append(cur_section)

        entry = "[\"" + ol_id + "\", ["
        for car in cur_section.car_list:
            entry += "[\"" + car.to_string() + "\",\"" + car.data[xval].to_string() + "\"],"
        entry = entry[:-1] + "]],\n"
        self.json_string += entry

    def json(self):
        temp = self.json_string[:-2] + "]\n}"
        return temp
