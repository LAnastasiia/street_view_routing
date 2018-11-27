def get_lon_lat(filename):
    with open(str(filename), 'r') as f:
        points_num = int(f.readline().strip('\n').split(' ')[0])
        lon = [None] * points_num
        lat = [None] * points_num

        for i in range(points_num):
            coords = f.readline().strip('\n').split(' ')
            lat[i], lon[i] = (coords[0]), (coords[1])
    return lat, lon
