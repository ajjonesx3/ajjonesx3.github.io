

def calculate_total(cars,disp):

    #create normalized lists
    normalized = {}

    for sec in disp.sections:
        if sec.name == "total":
            break
        temp = [[car,car.data[sec.name].sort_variable] for car in cars]
        added = 0
        missing = 0
        for entry in temp:
            if entry[1] != -1:
                added += entry[1]
            else:
                missing += 1
        avg = added // (len(temp) - missing)
        for entry in temp:
            if entry[1] == -1:
                entry[1] = 10
            else:
                if avg != 0:
                    entry[1] /= avg
                    entry[1] *= 10
        normalized[sec.name] = temp

    return normalized

def make_readable(cars,normalized):
    for key in normalized:
        entry = normalized[key]
        for car_entry in entry:
            car_entry[0].data["total"].score += car_entry[1]

    avg_total = 0
    for car in cars:
        avg_total += car.data["total"].score
    mx = avg_total / 100
    for car in cars:
        car.data["total"].score *= mx
        car.data["total"].score = round(car.data["total"].score)
        car.data["total"].sort_variable = car.data["total"].score

