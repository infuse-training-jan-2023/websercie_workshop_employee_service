import sqlite3

connection = sqlite3.connect('employee_services.db')
with open('employee_service/DB/schema.sql') as f:
    connection.executescript(f.read())