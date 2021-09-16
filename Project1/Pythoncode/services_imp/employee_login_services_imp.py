from typing import List

from dao_imp.employee_login_dao_imp import EmployeeLoginDAOImp
from daos.employee_login_dao import EmployeeLoginDAO
from entities.employee_login import EmployeeLogin
from services.employee_login_services import EmployeeLoginServices


class EmployeeLoginServicesImp(EmployeeLoginServices):

    def __init__(self, employee_login: EmployeeLoginDAO):
        self.employee_login = employee_login

    def create_employee_login(self, employee_login: EmployeeLogin) -> EmployeeLogin:
        result = self.employee_login.create_employee_login(employee_login)
        return result

    def get_employee_login_by_id(self, user_id: int) -> EmployeeLogin:
        result = self.employee_login.get_employee_login_by_id(user_id)
        return result

    def get_all_employee_logins(self) -> List[EmployeeLogin]:
        result = self.employee_login.get_all_employee_logins()
        return result

    def update_employee_login(self, employee_login: EmployeeLogin) -> EmployeeLogin:
        result = self.employee_login.update_employee_login(employee_login)
        return result

    def delete_employee_login(self, user_id: int) -> bool:
        result = self.employee_login.delete_employee_login(user_id)
        return result
