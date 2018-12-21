from classes.street import Street
from classes.car import Car
from classes.street import read_from_database, reset_visited
from classes.street import read_junc_coords
from visualization.read_coords import get_info
from choose_next_street import choose_random

input_file = "input_data.txt"
general_info = get_info(input_file)
NUM_CARS = general_info["cars_num"]


TIME_LEFT = [general_info["timespan"]] * NUM_CARS
LEN_VIEWED = 0
START = general_info["start_point"]
FLEET = [Car(START, i) for i in range(NUM_CARS)]



curr = START
time_left = TIME_LEFT[0]
car = FLEET[0]

while time_left > 0:
    street_list = read_from_database(curr)
    next_street = choose_random(street_list, time_left)

    if next_street:
        next_point = next_street.junctions[1]

        print("-- Move car{} from {} to {}".format(car, curr, next_point))
        curr = next_point
        time_left -= next_street.time
        next_street.set_is_visited()

    else:
        print("-- Stop | time_left =", time_left)
        time_left = 0

reset_visited()
route = car.path
print(route)
print(list(filter(lambda x: route.count(x) > 1, route)))

