import random
from classes.street import has_way_out

def choose_next_len_time(street_list, time_left, car, back=False):
    # "Max_length_greedy"
    i = 0
    street_list_len = len(street_list)
    while i < street_list_len:  # Search for street of max len but suitable time.
        next_street = max(street_list, key=lambda x: x.len)
        if (next_street.time <= time_left):
            if (not back and not next_street.is_visited) or (back):
                return next_street
        street_list.remove(next_street)
        i += 1
        continue


def choose_back(street_list, time_left, visited):
    i = 0
    while i < len(street_list):
        best_streets = list(filter(lambda x: x not in visited, street_list))
        if best_streets:
            next_street = best_streets[0]
            if (next_street.time <= time_left) and next_street not in visited:
                return next_street
            street_list.remove(next_street)
            i += 1
            continue


def choose_next_cost_time(street_list, time_left, car, back=False):
    # "Min_time_greedy"
    i = 0
    while i < len(street_list):  # Search for street of min suitable time.
        next_street = min(street_list, key=lambda x: x.time)

        if (next_street.time <= time_left):
            if (not back and not next_street.is_visited) or (back):
                return next_street
        street_list.remove(next_street)
        i += 1
        continue


def choose_random(street_list, time_left):
    res = list(filter(lambda x: x.time < time_left, street_list))
    next_street = random.choice(res)
    return next_street


def euler_path(street_list, time_left, car):
    # Euler path builder
    i = 0
    while i < len(street_list):
        next_street = max(street_list, key=lambda x: x.len * x[1].degree)
        if (next_street.time <= time_left) and (next_street.junctions[1] not in car.path):
            return next_street
        street_list.remove(next_street)
        i += 1
        continue


def choose_next_street_modificated(street_list,time_left,car):
    next_street = max(street_list,key= lambda x:x.len)
    while next_street:
        if has_way_out(next_street.junctions[1]) and (next_street.time <= time_left) and (next_street.junctions[1] not in car.path):
            return next_street
        else:
            street_list.remove(next_street)
