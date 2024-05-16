
class section:

    def __init__(self,car_list):
        self.car_list = car_list


class display:

    def __init__(self):
        self.json_string = "{\n\t\"array\":\n\t\t[";

    def add_section(self,car_list,xval):

        ol_id = xval = "_list"

        entry = "[\"" + ol_id + "\", ["
        for car in car_list:
            entry += "[\"" + car.to_string() + "\",\"" + car.data[xval] + "\"],"
        entry = entry[:-1] + "]],\n"
        self.json_string += entry

    def json(self):
        temp = self.json_string[:-2] + "]\n}"
        return temp
