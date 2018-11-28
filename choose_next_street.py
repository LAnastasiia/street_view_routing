def choose_next_len_time(street_list, time_left, car):
    i = 0
    while i < len(street_list):                                      # Search for street of max len but suitable time.
        next_street = max(street_list, key=lambda x: x.len)
        # print(next_street)
        if (next_street.time <= time_left) and (next_street.junctions[1] not in car.path):
            return next_street
        i += 1


def choose_next_cost_time(street_list, time_left, car):
    i = 0
    while i < len(street_list):                                      # Search for street of max len but suitable time.
        next_street = min(street_list, key=lambda x: x.time)
        # print(next_street)
        if (next_street.time <= time_left) and (next_street.junctions[1] not in car.path):
            return next_street
        i += 1
