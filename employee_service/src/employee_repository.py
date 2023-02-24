import sqlite3

class EmpRepository:
    def __init__(self) -> None:   
        self.db_path = '../employee_services.db'
        self.connection = None
        
    def connect_db(self):
        if self.connection is None:
            self.connection =  sqlite3.connect(self.db_path, check_same_thread=False)    

    def add_employee(self,name,age,gender,status):
        try:
            self.connect_db()
            cursor = self.connection.cursor()
            cursor.execute('insert into employee (name,age,gender,status) values(?,?,?,?)', (name,age,gender,status))
            self.connection.commit()
            return {
                'name': name,
                'age': age,
                'gender': gender,
                'status': status
            }
        except Exception as e:
            raise Exception('Error: ', e)

    def get_all_employees(self):
        try:
            self.connect_db()
            cursor = self.connection.cursor()
            rows = cursor.execute('select * from employee')
            return rows
        except Exception as e:
            raise Exception('Error: ', e)

    def get_employee(self,emp_id):
        try:
            self.connect_db()
            cursor = self.connection.cursor()
            cursor.execute('select * from employee where emp_id=?',(emp_id,))
            row = cursor.fetchall()
            self.connection.commit()
            return row
        except Exception as e:
            raise Exception('Error: ', e)

    def update_emp_details(self,emp_id,update_item):
        try:
            self.connect_db()
            cursor = self.connection.cursor()
            for key in update_item.keys():
                result = cursor.execute(f'update  employee set {key}=? where emp_id=?', (update_item[key],emp_id,))
            self.connection.commit()     
            if(result.rowcount >0):     
                return {'status': "details updated successfully"}
            return {'status': "details not updated "}
        except Exception as e:
            raise Exception('Error: ', e)
        
    def get_all_workingemployees(self):
        try:
            self.connect_db()
            cursor = self.connection.cursor()
            cursor.execute('select * from employee where status = 1')
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            raise Exception('Error: ', e)    


    def add_to_dept(self,emp_id,deptName):
        try:
            self.connect_db()
            cursor = self.connection.cursor()
            cursor.execute('UPDATE employee SET dept_name =? WHERE emp_id = ?;',(deptName,emp_id))
            self.connection.commit()
        except Exception as e:
            raise Exception('Error: ', e)

    def update_status(self,id,status):
        try:
            self.connect_db()
            cursor = self.connection.cursor()
            cursor.execute('UPDATE employee SET status = ? WHERE emp_id = ?', (status,id))
            self.connection.commit()
            return {
                'id': id,
                'status': status
            }
        except Exception as e:
            raise Exception('Error: ', e)

    def check_department(self,dept):
            try:
                self.connect_db()
                cursor = self.connection.cursor()
                row = cursor.execute('SELECT * FROM employee WHERE dept_name IN (SELECT dept_name FROM department WHERE dept_name= ? )', (dept,))
                self.connection.commit()
                return row
            except Exception as e:
                raise Exception('Error: ', e)
    