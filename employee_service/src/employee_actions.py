from employee_repository import EmpRepository

class EmpAction:
    def __init__(self)-> None:
        self.emp_repo = EmpRepository()
    
    def add_employee(self,empId,name,age,gender,status):
            try:
                item = self.emp_repo.add_item(empId,name,age,gender,status)
                return item
            except Exception as e:
                print(e)
            return {}    