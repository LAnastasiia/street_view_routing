import pandas


def get_lon_lat(filename):
    with open(str(filename), 'r') as f:
        points_num = int(f.readline().strip('\n').split(' ')[0])
        lon = [None] * points_num
        lat = [None] * points_num

        for i in range(points_num):
            coords = f.readline().strip('\n').split(' ')
            lat[i], lon[i] = (coords[0]), (coords[1])
    return lat, lon


def get_info(filename):
    """ Proxess the first line of the file and return dict with respective values. """
    with open(filename, 'r') as f:
        general_info = list(map(int, f.readline().strip('\n').split(' ')))
        info_labels = ["junctions_num", "streets_num", "timespan", "cars_num", "start_point"]
        info_dict = dict((info_labels[i], general_info[i]) for i in range(len(info_labels)))
        return info_dict


def read_point_coords_csv(filename, rows_num):
    """ Read junction data from file into a DataFrame. """
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        df = pandas.read_csv(filename,
                             sep=' ',
                             skiprows=[0],
                             nrows = rows_num,
                             names = ["Latitude", "Longitude"],
                             dtype={'Latitude': 'float64', 'Longitude': 'float64'})
    return df


def get_street_coords(filename, j_rows, s_rows):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:

        for _ in range(j_rows + 1):  # skip junctions' lines
            next(f)

        lon, lat = [], []
        j_df = read_point_coords_csv(filename, j_rows)

        for i in range(s_rows):
            j_indexes = list(map(int, f.readline().strip('\n').split(' ')[0:2]))
            for j in j_indexes:
                lat.append(j_df.iloc[j]["Latitude"])
                lon.append(j_df.iloc[j]["Longitude"])
        return lat, lon


if __name__ == "__main__":
    fname = "input_data.txt"
    num_info = get_info(fname)
    print(num_info)
    # data = get_point_coords_csv(fname, num_info["junctions_num"])
    # print(num_info)
    get_street_coords(fname, num_info["junctions_num"], num_info["streets_num"])


# def get_street_lon_lat(filename, database):
#     pass
# print(df.iloc[[2]])
