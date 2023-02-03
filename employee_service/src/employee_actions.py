from employee_repository import EmpRepository

import json

class EmpAction:
    def __init__(self)-> None:
        self.emp_repo = EmpRepository()
    
    def add_employee(self,name,age,gender,status):
            try:
                item = self.emp_repo.add_employee(name,age,gender,status)
                return item
            except Exception as e:
                print(e)
            return {}    
    
    def get_all_employees(self):
        try:
            items = self.emp_repo.get_all_employees()
            res = []
            for item in items:
                res.append({
                    'empid': item[0],
                    'name': item[1],
                    'age': item[2],
                    'gender': item[3],
                    'status': item[4]
                })
            return res
        except Exception as e:
            print(e)
        return {}


    def get_employee_by_id(self,id):
        try:
            item = self.emp_repo.get_employee(id)
            res = []
            for item in item:
                res.append({
                    'empid': item[0],
                    'name': item[1],
                    'age': item[2],
                    'gender': item[3],
                    'status': item[4]
                })
            return res
        except Exception as e:
            print(e)
            return {}

            
        
    def update_emp(self,empid, name, age, gender):
            try:
                update_item = self.emp_repo.update_emp_details(empid, name, age, gender)
                return update_item
            except Exception as e:
                print(e)
            return {}
        
    def get_all_workingemployees(self):
        try:
            items = self.emp_repo.get_all_workingemployees()
            res = []
            for item in items:
                res.append({
                    'empid': item[0],
                    'name': item[1],
                    'age': item[2],
                    'gender': item[3],
                    'status': item[4]
                })
            return res
        except Exception as e:
            print(e)
        return {}        
        
            

    def add_to_dept(self,empid,deptName):
        try:
            item = self.emp_repo.add_to_dept(empid,deptName)
            return {"status":"update successfull"}
        except Exception as e:
            print(e)
        return {}

    def get_all_depts(self):
        try:
            items = self.emp_repo.get_all_depts()
            return {"status":"update successfull"}
        except Exception as e:
            print(e)
        return {}

    def update_status(self,id,status):
        try:
            item = self.emp_repo.update_status(id,status)
            return item
        except Exception as e:
            print(e)
        return {}

    def check_department(self,dept):
        try:
            print(dept)
            items = self.emp_repo.check_department(dept)
            res = []
            for item in items:
                res.append({
                    'empid': item[0],
                    'name': item[1],
                    'age': item[2],
                    'gender': item[3],
                    'status': item[4]
                })
            return res
        except Exception as e:
            print(e)
        return {}