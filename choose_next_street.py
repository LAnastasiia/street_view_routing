def choose_next_len_time(street_list, time_left):
    i = 0
    while i < len(street_list):                                      # Search for street of max len but suitable time.
        next_street = max(street_list, key=lambda x: x.len)
        if (next_street.time <= time_left):
            return next_street
        i += 1


def choose_next_cost_time(street_list, time_left):
    i = 0
    while i < len(street_list):                                      # Search for street of max len but suitable time.
        next_street = min(street_list, key=lambda x: x.time)
        if (next_street.time <= time_left):
            return next_street
        i += 1
