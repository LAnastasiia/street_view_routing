import sqlite3
from sqlite3 import Error


def create_db():
    try:
        conn = sqlite3.connect("index.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS streets
                     (begin int, end int, time int, len int)''')
        c.execute('''CREATE TABLE IF NOT EXISTS junctions (id int,latitude real, longitude real, degree int)''')
        conn.commit()
    except Error as e:
        print(e)
    finally:
        conn.close()


def read_from_txt():
    id = 0
    f = open("input_data.txt", "r")
    first_line = f.readline().split()
    num_of_junctions = int(first_line[0])
    num_of_streets = int(first_line[1])
    for i in range(num_of_junctions):
        write_junction(id, f.readline())
        id += 1
    for i in range(num_of_streets):
        write_street(f.readline())


def write_junction(id, text):
    conn = sqlite3.connect("index.db")
    c = conn.cursor()
    c.execute("INSERT INTO junctions VALUES ({},{},{},{})".format(id, text.split()[0], text.split()[1], 0))
    conn.commit()
    conn.close()


def write_street(text):
    conn = sqlite3.connect("index.db")
    c = conn.cursor()
    if int(text.split()[2]) == 1:
        c.execute("INSERT INTO streets VALUES ({},{},{},{})".format(text.split()[0], text.split()[1],
                                                                    text.split()[3], text.split()[4]))
    else:
        c.execute("INSERT INTO streets VALUES ({},{},{},{})".format(text.split()[0], text.split()[1],
                                                                    text.split()[3], text.split()[4]))
        c.execute("INSERT INTO streets VALUES ({},{},{},{})".format(text.split()[1], text.split()[0],
                                                                    text.split()[3], text.split()[4]))
    conn.commit()
    conn.close()


create_db()
read_from_txt()
