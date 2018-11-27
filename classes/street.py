class Street:
    def __init__(self, lenght, time, junctions, is_visited):
        self.len = lenght
        self.time = time
        self.junctions = junctions
        self.is_visited = is_visited


def read_from_database(id):
    import sqlite3
    con = sqlite3.connect("../database/index.db")
    cursor = con.cursor()
    lst = cursor.execute("SELECT * FROM streets WHERE begin={}".format(id)).fetchall()
    street_list = []
    for street in lst:
        s = Street(street[3], street[2], (street[0], street[1]), street[4])
        street_list.append(s)
    return street_list
