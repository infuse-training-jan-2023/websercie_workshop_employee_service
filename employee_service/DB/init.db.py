import sqlite3

connection = sqlite3.connect('employee_services.db')
with open('employee_service/DB/schema.sql') as f:
    connection.executescript(f.read())

cursor = connection.cursor()

cursor.execute ("INSERT INTO department (deptName) VALUES (?)",
("HR",)
)
cursor.execute ("INSERT INTO department (deptName) VALUES (?)",
("DEVELOPEMENT",)
)
cursor.execute ("INSERT INTO department (deptName) VALUES (?)",
("FINANCE",)
)
cursor.execute ("INSERT INTO department (deptName) VALUES (?)",
("MARKETING",)
)

connection.commit()
connection.close()