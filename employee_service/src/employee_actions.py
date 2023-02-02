from employee_repository import EmpRepository

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