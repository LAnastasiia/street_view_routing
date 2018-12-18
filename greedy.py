from classes.street import Street
from classes.car import Car
from classes.street import read_from_database, reset_visited
from classes.street import read_junc_coords
from visualization.read_coords import get_info
from choose_next_street import choose_next_len_time, choose_next_cost_time, euler_path, choose_back

input_file = "input_data.txt"
general_info = get_info(input_file)
NUM_CARS = general_info["cars_num"]
NUM_CARS = 2


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



# arr of functions for cars with different indexes
choose_next = [choose_next_len_time, choose_next_cost_time, euler_path]


def greedy_routing(curr_pos, ind):
    NUM_CARS = 1
    VISITED = []
    routs_list = []
    reset_visited()
    LEN_VIEWED = 0

    for c in range(NUM_CARS):
        car = FLEET[c]
        TL = TIME_LEFT[c]
        CURR_POSITION = curr_pos

        while TL > 0:
            street_list = read_from_database(CURR_POSITION)
            # next_street = choose_next[c%2](street_list, TL, car)
            next_street = choose_next[ind](street_list, TL, car)

            if next_street and next_street not in VISITED:
                next_point = next_street.junctions[1]
                print("-- Move car{} from {} to {}".format(c, CURR_POSITION, next_point))
                CURR_POSITION = next_point
                TL -= next_street.time
                LEN_VIEWED += next_street.len
                next_street.set_is_visited()

            else:
                print("(backtracking) ", end='')
                back_streets = read_from_database(CURR_POSITION)
                new_streets = list(filter(lambda x: x.junctions not in VISITED, back_streets))
                if new_streets:
                    i = 0
                    while i < len(new_streets):
                        i += 1
                        next_street = new_streets[-1]
                        if next_street.time <= TL:
                            print("-- Move car{} from {} to {}".format(c, CURR_POSITION, next_street.junctions[1]))
                            CURR_POSITION = next_street.junctions[1]
                            car.move(CURR_POSITION)
                            if (not next_street.is_visited):
                                LEN_VIEWED += next_street.len
                            VISITED.append(next_street.junctions)
                            break
                        else:
                            new_streets.remove(next_street)
                else:
                    print("-- Stop |", TL)                # if there is no way to move -- car stops until time runs out
                    TL = 0

        reset_visited()
        routs_list.append(car.path)
    print(LEN_VIEWED)
    return car.path



    ###################  -- output
    #
    # print('\n')
    # print("Total length of streets viewed:", LEN_VIEWED)
    # print("Street Viewing details stored in: results.txt")
    # write_results(TIME_LEFT[0])
    #
    ###################

    ################### -- junction coordinates
    #
    # result_coords = []
    # for car_results in vis_junct_list:
    #     result_coords.append([read_junc_coords(j) for j in car_results])
    # return result_coords
    #
    ###################


if __name__ == "__main__":
    print(greedy_routing(START, 0))
    ################### -- to visualize streets viewed with different algorithms
    #
    # results = {"time": [], "len": []}
    # for START in range(0, general_info["junctions_num"], 1000):
    #     routing_len = greedy_routing(START)
    #     print("LEN", routing_len)
    #     results["len"].append(routing_len[0])
    #     results["time"].append(routing_len[1])
    #     print(results["time"], results["len"])
    #
    # import holoviews as hv
    # import hvplot
    # import hvplot.pandas
    # import pandas as pd
    # hv.extension('bokeh')
    #
    # print(results["time"], results["len"])
    #
    # df = pd.DataFrame({'Length':range(0, general_info["junctions_num"], 1000),
    #    ' ': results["len"],'  ':results["time"]})
    # hv.renderer('bokeh').save(df.hvplot.bar('Length', color=["#980f4d", "#e47127"]),'greedy_time_len_comparison')
    #
    ###################
