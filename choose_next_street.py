def choose_next_len_time(street_list, time_left, car):
    # "Max_length_greedy"
    i = 0
    street_list_len = len(street_list)
    while i < street_list_len:                                      # Search for street of max len but suitable time.
        next_street = max(street_list, key=lambda x: x.len)
        if (next_street.time <= time_left) and (next_street.junctions[1] not in car.path):
            return next_street
        street_list.remove(next_street)
        i += 1
        continue

def choose_next_cost_time(street_list, time_left, car):
    # "Min_time_greedy"
    i = 0
    while i < len(street_list):                                      # Search for street of min suitable time.
        next_street = min(street_list, key=lambda x: x.time)
        if (next_street.time <= time_left) and (next_street.junctions[1] not in car.path):
            return next_street
        street_list.remove(next_street)
        i += 1
        continue
