import sqlite3


def createtable():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE data(rollno INTEGER, name TEXT, marks REAL)")
    conn.commit()
    conn.close()

def insert(roll,nam,mark):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO data VALUES(?,?,?)",(roll,nam,mark))
    conn.commit()
    conn.close()

insert(4,'ppppp',100)