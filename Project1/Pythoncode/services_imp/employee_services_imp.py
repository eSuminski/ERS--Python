from typing import List

from daos.employee_dao import EmployeeDAO
from entities.employee import Employee
from services.employee_services import EmployeeServices


class EmployeeServicesImp(EmployeeServices):

    def __init__(self, employee_dao: EmployeeDAO):
        self.employee_dao = employee_dao

    def create_employee(self, employee: Employee) -> Employee:
        new_employee = self.employee_dao.create_employee(employee)
        return new_employee

    def get_employee_by_id(self, employee_id: int) -> Employee:
        returned_employee = self.employee_dao.get_employee_by_id(employee_id)
        return returned_employee

    def get_all_employees(self) -> List[Employee]:
        all_employees = self.employee_dao.get_all_employees()
        return all_employees

    def update_employee(self, employee: Employee) -> Employee:
        updated_employee = self.update_employee(employee)
        return updated_employee

    def delete_employee(self, employee_id: int) -> bool:
        result = self.delete_employee(employee_id)
        return result
