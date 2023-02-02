import sqlite3

class EmpRepository:
    DBPATH = './employee_services.db'
    @staticmethod
    def connect_db():
        return sqlite3.connect(EmpRepository.DBPATH)
    
    @staticmethod
    def add_employee(name,age,gender,status):
        try:
            conn = EmpRepository.connect_db()
            c = conn.cursor()
            insert_cursor = c.execute('insert into employee (name,age,gender,status) values(?,?,?,?)', (name,age,gender,status))
            conn.commit()
            return {
                'name': name,
                'age': age,
                'gender': gender,
                'status': status
            }
        except Exception as e:
            raise Exception('Error: ', e)

    @staticmethod
    def get_all_employees():
        try:
            conn = EmpRepository.connect_db()
            c = conn.cursor()
            rows = c.execute('select * from employee')
            return rows
        except Exception as e:
            raise Exception('Error: ', e)
    @staticmethod
    def get_employee(empid):
        try:
            conn = EmpRepository.connect_db()
            c = conn.cursor()
            row=c.execute('select * from employee where empId=?',(empid,))
            conn.commit()
            return row
        except Exception as e:
            raise Exception('Error: ', e)

    @staticmethod
    def update_emp_details(empid, name, age, gender):
        try:
            conn = EmpRepository.connect_db()
            c = conn.cursor()
            if name is not None:
                sqlupdate='update  employee set name=? where empId=?'
                result=c.execute(sqlupdate, (name,empid,))
            if  age is not None:
                result=c.execute('update  employee set age=? where empId=?', (age,empid,))
            if  gender is not None:
                result=c.execute('update  employee set gender=? where empId=?', (gender,empid,))
            conn.commit()
            if(result.rowcount >0):     
                return {'status': "details updated successfully"}
            return {'status': "details not updated "}
        except Exception as e:
            raise Exception('Error: ', e)
        
    @staticmethod
    def get_all_workingemployees():
        try:
            conn = EmpRepository.connect_db()
            c = conn.cursor()
            rows = c.execute('select * from employee where status=1')
            return rows
        except Exception as e:
            raise Exception('Error: ', e)    
    @staticmethod
    def add_to_dept(empid,deptName):
        print(empid,deptName)
        try:
            conn = EmpRepository.connect_db()
            c = conn.cursor()
            c.execute('UPDATE employee SET deptName =? WHERE empId = ?;',(deptName,empid))
            c.fetchall()
            conn.commit()
        except Exception as e:
            raise Exception('Error: ', e)

    @staticmethod
    def update_status(id,status):
        try:
            conn = EmpRepository.connect_db()
            c = conn.cursor()
            insert_cursor = c.execute('UPDATE employee SET status = ? WHERE empid = ?', (status,id))
            conn.commit()
            return {
                'id': id,
                'status': status
            }
        except Exception as e:
            raise Exception('Error: ', e)

    @staticmethod
    def check_department(dept):
            print(dept)
            try:
                conn = EmpRepository.connect_db()
                c = conn.cursor()
                insert_cursor = c.execute('SELECT * FROM employee WHERE deptName IN (SELECT deptName FROM department WHERE deptName= ? )', (dept,))
                conn.commit()
                return insert_cursor
            except Exception as e:
                raise Exception('Error: ', e)
    