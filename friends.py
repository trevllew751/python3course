import sqlite3
# create/connect to a database
conn = sqlite3.connect("my_friends.db")
# create cursor object
c = conn.cursor()
# execute some sql
# c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
insert_query = """INSERT INTO friends
                VALUES ('niglord', 'blackman', 78);"""
c.execute(insert_query)
# commit changes
conn.commit()
conn.close()