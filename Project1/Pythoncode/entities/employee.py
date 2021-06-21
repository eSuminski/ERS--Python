class Employee:

    def __init__(self, employee_id: int, first_name: str, last_name: str):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"employee ID: {self.employee_id}, first name: {self.first_name}, last name: {self.last_name}"


    def as_json_dict(self):
        return {
            "employeeID": self.employee_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
        }