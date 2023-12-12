import sqlite3
# from sqlite3 import f



conn=sqlite3.connect("database.sqlite")

cursor=conn.cursor()
print(type(cursor))

for row in cursor.execute("SELECT name FROM sqlite_master"):
    print(row)

cursor.execute("SELECT name FROM sqlite_master").fetchall()


print(cursor.execute("SELECT name FROM sqlite_master").fetchall())



sample_data=cursor.execute("SELECT * FROM Iris LIMIT 3").fetchall()
for item in sample_data:
    print(item)

print("22222222222222")

print([row[0] for row in cursor.description])





import pandas as pd

df=pd.read_sql_query("SELECT * FROM Iris",conn)

print(df.head(5))


print(df.dtypes)
print(df.shape)
print(df.columns)
