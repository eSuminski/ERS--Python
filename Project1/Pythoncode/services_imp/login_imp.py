from services.employee_login_services import EmployeeLoginServices
from services.employee_services import EmployeeServices
from services.login import Login
from services.manager_login_services import ManagerLoginServices
from services.manager_services import ManagerServices
from services_imp.employee_login_services_imp import EmployeeLoginServicesImp
from services_imp.employee_services_imp import EmployeeServicesImp
from services_imp.manager_login_services_imp import ManagerLoginServicesImp
from services_imp.manger_services_imp import ManagerServicesImp


class LoginImp(Login):
    def __init__(self,
                 employee_login_services: EmployeeLoginServices,
                 manager_login_services: ManagerLoginServices,
                 employee_services: EmployeeServices,
                 manager_services: ManagerServices
                 ):
        self.employee_login_services = employee_login_services
        self.manager_login_services = manager_login_services
        self.employee_services = employee_services
        self.manager_services = manager_services

    def login(self, username: str, password: str):
        elogins = self.employee_login_services.get_all_employee_logins()
        for l in elogins:
            if l.username == username and l.u_password == password:
                result = self.employee_services.get_employee_by_id(l.user_id)
                return result
        mlogins = self.manager_login_services.select_all_manager_logins()
        for l in mlogins:
            if l.username == username and l.u_password == password:
                result = self.manager_services.get_manager_by_id(l.user_id)
                return result
