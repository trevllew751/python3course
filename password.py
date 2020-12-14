import sqlite3
conn = sqlite3.connect("users.db")

c = conn.cursor()
un = input("Enter your username ")
pw = input("Enter your password ")
query = f"SELECT * FROM users WHERE username = ? AND password = ?"
c.execute(query, (un, pw))
result = c.fetchone()
if result:
    print("welcome back")
else:
    print("failed login")
conn.commit()
conn.close()