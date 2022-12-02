import sqlite3

con = sqlite3.connect("db.sqlite3")

# prinnt all tables
print(con.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall())
