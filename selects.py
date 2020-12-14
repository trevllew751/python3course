import sqlite3

conn = sqlite3.connect("my_friends.db")
c = conn.cursor()
c.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness")
# Iterate over a cursor
# for reslut in c:
#   print result

# fetch one result
print(c.fetchone())

#fetch all results as a list
print(c.fetchall())

conn.commit()
conn.close()