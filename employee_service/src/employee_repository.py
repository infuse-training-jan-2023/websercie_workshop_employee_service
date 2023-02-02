import sqlite3

class EmpRepository:
    DBPATH = './employee_services.db'
    @staticmethod
    def connect_db():
        return sqlite3.connect(EmpRepository.DBPATH)
    
    @staticmethod
    def add_item(empId,name,age,gender,status):
        try:
            conn = EmpRepository.connect_db()
            c = conn.cursor()
            insert_cursor = c.execute('insert into employee (empId,name,age,gender,status) values(?,?,?,?,?)', (empId,name,age,gender,status,))
            conn.commit()
            return {
                'empId': insert_cursor.lastrowid,
                'name': name,
                'age': age,
                'gender': gender,
                'status': status
            }
        except Exception as e:
            raise Exception('Error: ', e)