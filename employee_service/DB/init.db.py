import sqlite3

connection = sqlite3.connect('employee_services.db')
with open('employee_service/DB/schema.sql') as f:
    connection.executescript(f.read())


cursor = connection.cursor()

cursor.execute ("INSERT INTO department (deptName,deptId) VALUES (?,?)",
("HR",1)
)
cursor.execute ("INSERT INTO department (deptName,deptId) VALUES (?,?)",
("DEVELOPEMENT",2)
)
cursor.execute ("INSERT INTO department (deptName,deptId) VALUES (?,?)",
("FINANCE",3)
)
cursor.execute ("INSERT INTO department (deptName,deptId) VALUES (?,?)",
("MARKETING",4)
)


connection.commit()
connection.close()