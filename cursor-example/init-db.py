import sqlite3
conn = sqlite3.connect('database.db')

with open('schema.sql') as f:
    conn.executescript(f.read())
cur = conn.cursor()
cur.execute("insert into user values('Edward','1234')")

conn.commit()
conn.close()