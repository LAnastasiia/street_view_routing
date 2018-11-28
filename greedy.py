from classes.street import Street
from classes.car import Car
from classes.street import read_from_database
from visualization.read_coords import get_info
from choose_next_street import choose_next_len_time, choose_next_cost_time


input_file = "input_data.txt"
general_info = get_info(input_file)
# NUM_CARS = general_info["cars_num"]

NUM_CARS = 2   # to test two greedy functions
TIME_LEFT = [general_info["timespan"]] * NUM_CARS
LEN_VIEWED = 0
START = general_info["start_point"]
FLEET = [Car(START, i) for i in range(NUM_CARS)]


def write_results(total_time):
    """
    Write algorithm's steps into results.txt.
    """
    with open("results.txt", 'w') as results_file:
        results_file.write("{} cars in the freet \n".format(NUM_CARS))
        results_file.write("START at {}\n".format(START))
        stopped, j = 0, 0
        while stopped != NUM_CARS:
            for car in FLEET:
                if len(car.path) > j+1:
                    movement = "moves from junction {} to junction {}".format(car.path[j],
                                                                              car.path[j+1])
                else:
                    movement = "stays on {}".format(car.path[-1])
                    stopped += 1
                    FLEET.remove(car)
                results_file.write("Car #{} -- {}\n".format(str(car.id+1), movement))
            j += 1

# arr of functions available for different car indexes
choose_next = [choose_next_len_time, choose_next_cost_time]

# Move cars consequenly.
for c in range(NUM_CARS):
    CURR_POSITION = START
    car = FLEET[c]
    TL = TIME_LEFT[c]
    while TL > 0:
        street_list = read_from_database(CURR_POSITION)
        next_street = choose_next[c%2](street_list, TL, car)
        if (next_street) and next_street.junctions[1] not in car.path:
            next_point = next_street.junctions[1]
            print("-- Move car{} from {} to {}".format(c, CURR_POSITION, next_point))
            car.move(next_point)
            CURR_POSITION = next_point
            TL -= next_street.time
            if not next_street.is_visited:
                LEN_VIEWED += next_street.len
            next_street.set_is_visited(1)
        else:
            # if there is no way to move -- car stays on the it's last position and time runs out
            print("-- Stop |", TL)
            TL = 0

print('\n')
print("Total length of streets viewed:", LEN_VIEWED)
print("Street Viewing details stored in: results.txt")
write_results(TIME_LEFT[0])
