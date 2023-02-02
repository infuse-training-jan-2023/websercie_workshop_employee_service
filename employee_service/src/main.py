from flask import Flask, Response,request
import json
from employee_actions import EmpAction

app = Flask(__name__)
emp_action = EmpAction()

@app.route('/addemployee',methods=['POST'])
def add_data():
    request_data = request.get_json()
    name  = request_data['name']
    age   = request_data['age']
    gender = request_data['gender']
    status = request_data['status']
    added_employee = emp_action.add_employee(name,age,gender,status)
    if added_employee =={}:
        return Response("{'error': 'Erro addding the item'}", mimetype='application/json', status=500)
    return Response(json.dumps(added_employee), mimetype='application/json', status=201)
    return {"hello": "world"}


@app.route('/allemployees', methods = ['GET'])
def get_all_items():
        employees = emp_action.get_all_employees()
        return Response(json.dumps(employees), mimetype='application/json', status=200)
    
if __name__ == '__main__':
    app.run(debug=True, port=5000,host='0.0.0.0')
    
    
