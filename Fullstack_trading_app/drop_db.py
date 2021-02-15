import sqlite3,config
connection=sqlite3.connect("app.db")
print("Successfully connected to Database")
cursor = connection.cursor()

cursor.execute(""" DROP TABLE stock_price """)
cursor.execute(""" DROP TABLE stock""")

connection.commit()
