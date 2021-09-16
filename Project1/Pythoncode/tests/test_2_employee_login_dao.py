from dao_imp.employee_login_dao_imp import EmployeeLoginDAOImp
from daos.employee_login_dao import EmployeeLoginDAO
from entities.employee_login import EmployeeLogin

employee_login_dao: EmployeeLoginDAO = EmployeeLoginDAOImp()

e_login1 = EmployeeLogin(1, "Linderp", "Fl0w3rs")
e_login2 = EmployeeLogin(2, "I Love Ted", "Passw0rd")
e_login3 = EmployeeLogin(2, "Wrong", "Person")


def test_create_employee_login():
    print()
    print(e_login1)
    employee_login_dao.create_employee_login(e_login1)
    check_against = employee_login_dao.get_employee_login_by_id(1)
    print(check_against)
    assert check_against.user_id == e_login1.user_id


def test_get_employee_login_by_id():
    print()
    result = employee_login_dao.get_employee_login_by_id(1)
    assert result.user_id == 1


def test_get_all_employee_logins():
    employee_login_dao.create_employee_login(e_login2)
    print()
    e_logins = employee_login_dao.get_all_employee_logins()
    assert len(e_logins) == 2


def test_update_employee_login():
    employee_login_dao.update_employee_login(e_login3)
    result = employee_login_dao.get_employee_login_by_id(2)
    assert result.username == "Wrong"


def test_delete_employee_login():
    employee_login_dao.delete_employee_login(2)
    e_logins = employee_login_dao.get_all_employee_logins()
    assert len(e_logins) == 1
