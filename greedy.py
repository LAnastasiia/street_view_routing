from classes.street import Street
from classes.car import Car
from classes.street import read_from_database
from visualization.read_coords import get_info


input_file = "input_data.txt"
general_info = get_info(input_file)
NUM_CARS = general_info["cars_num"]
TIME_LEFT = [general_info["timespan"]] * NUM_CARS
print(TIME_LEFT)
CURR = general_info["start_point"]
print()
LEN_VIEWED = 0


for i in range(NUM_CARS):                                             # Move cars successively
    car = Car(CURR)
    TL = TIME_LEFT[i]
    while TL > 0:                                                     # Until time for this car runs out.
        street_list = read_from_database(CURR)
        i = 0
        while i < len(street_list):                                   # Search for street of max len but suitable time.
            next_point = max(street_list, key=lambda x: x.len)
            if (next_point.time <= TL):
                car.move(next_point)
                CURR = next_point
                TL -= next_point.time
                LEN_VIEWED += next_point.len
                break
            i += 1
            continue
        TL = 0
    print(LEN_VIEWED)

print(LEN_VIEWED)

