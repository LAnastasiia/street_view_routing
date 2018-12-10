class Street:
    def __init__(self, lenght, time, junctions, is_visited):
        self.len = lenght
        self.time = time
        self.junctions = junctions
        self.is_visited = is_visited

    def set_is_visited(self, value):
        import sqlite3
        self.is_visited = 1
        con = sqlite3.connect("database/index.db")  # change to "../database/index.db" if running visual.py
        cursor = con.cursor()
        cursor.execute("UPDATE streets SET is_visited = 1 WHERE begin=? AND end=?",self.junctions)
        con.commit()
        con.close()

    def __repr__(self):
        return str(self.junctions) + "--" + str(self.is_visited)

def read_from_database(id):
    import sqlite3
    con = sqlite3.connect("database/index.db")
    cursor = con.cursor()
    lst = cursor.execute("SELECT * FROM streets WHERE begin='{}'".format(id)).fetchall()
    street_list = []
    for street in lst:
        s = Street(street[3], street[2], (street[0], street[1]), street[4])
        street_list.append(s)
    return street_list


def read_junc_coords(junct_index):
    import sqlite3
    con = sqlite3.connect("database/index.db")
    cursor = con.cursor()
    junct_coords = cursor.execute("SELECT * FROM junctions WHERE id='{}'".format(junct_index)).fetchall()[0]
    return junct_coords[1], junct_coords[2]


def reset_visited(value):
    import sqlite3
    con = sqlite3.connect("database/index.db")  # change to "../database/index.db" if running visual.py
    cursor = con.cursor()
    cursor.execute("UPDATE streets SET is_visited = 0 WHERE is_visited = 1")
    con.commit()
    con.close()
