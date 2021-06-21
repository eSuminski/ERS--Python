from unittest.mock import MagicMock

from dao_imp.employee_dao_imp import EmployeeDAOImp
from dao_imp.employee_login_dao_imp import EmployeeLoginDAOImp
from dao_imp.manager_login_dao_imp import ManagerLoginDAOImp
from dao_imp.manger_dao_imp import ManagerDAOImp
from dao_imp.reimbursement_dao_imp import ReimbursementDAOImp
from entities.employee import Employee
from entities.employee_login import EmployeeLogin
from entities.manager import Manager
from entities.manager_login import ManagerLogin
from entities.reimbursements import Reimbursements
from services_imp.employee_login_services_imp import EmployeeLoginServicesImp
from services_imp.employee_services_imp import EmployeeServicesImp
from services_imp.login_imp import LoginImp
from services_imp.manager_login_services_imp import ManagerLoginServicesImp
from services_imp.manger_services_imp import ManagerServicesImp

employees_logins = [
    EmployeeLogin(1, "first", "1"),
    EmployeeLogin(2, "second", "2"),
    EmployeeLogin(3, "third", "3")
]

manager_logins = [
    ManagerLogin(1, "fourth", "4"),
    ManagerLogin(2, "fifth", "5"),
    ManagerLogin(3, "sixth", "6")
]

employees = [
    Employee(1, "employee1", "1"),
    Employee(2, "employee2", "2"),
    Employee(3, "employee3", "3")
]

managers = [
    Manager(2, "manager4", "4"),
    Manager(2, "manager5", "5"),
    Manager(2, "manager6", "6")
]

reimbursements = [
    Reimbursements(1, 2, 100.25, "testing purposes", 0, ""),
    Reimbursements(2, 2, 100.25, "testing purposes 2", 0, "")
]

login_fail = {"loginFail": "No user with those login credentials was found"}

mock_dao_el = EmployeeLoginDAOImp()
mock_dao_ml = ManagerLoginDAOImp()
mock_dao_m = ManagerDAOImp()
mock_dao_e = EmployeeDAOImp()
moc_dao_r = ReimbursementDAOImp()
login_service = LoginImp(mock_dao_el, mock_dao_ml, mock_dao_e, mock_dao_m)

mock_dao_el.get_all_employee_logins = MagicMock(return_value=employees_logins)
employees_logins = mock_dao_el.get_all_employee_logins()

mock_dao_ml.select_all_manager_logins = MagicMock(return_value=manager_logins)
manager_logins = mock_dao_ml.select_all_manager_logins()

mock_dao_e.get_employee_by_id = MagicMock(return_value=employees[0])
employees[0] = mock_dao_e.get_employee_by_id()

mock_dao_m.get_manager_by_id = MagicMock(return_value=managers[0])
managers[0] = mock_dao_m.get_manager_by_id()

login_service.login = MagicMock(return_value=login_fail)
login_fail = login_service.login()

employee_login_services = EmployeeLoginServicesImp(mock_dao_el)
manager_login_services = ManagerLoginServicesImp(mock_dao_ml)
employee_services = EmployeeServicesImp(mock_dao_e)
manager_services = ManagerServicesImp(mock_dao_m)


def test_mock_get_employee_by_id():
    result = employee_services.get_employee_by_id(1)
    print(result)
    assert result.first_name == "employee1"


def test_mock_get_manager_by_id():
    result = manager_services.get_manager_by_id(1)
    print(result)
    assert result.first_name == "manager4"


def test_mock_get_all_employee_logins():
    result = employee_login_services.get_all_employee_logins()
    print(result)
    assert len(result) == 3


def test_mock_get_all_manager_logins():
    result = manager_login_services.select_all_manager_logins()
    print(result)
    assert len(result) == 3


def test_mock_login_fail():
    result = login_service.login("wrong", "still wrong")
    print(result)
    assert result["loginFail"] == "No user with those login credentials was found"
