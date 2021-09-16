from dao_imp.employee_dao_imp import EmployeeDAOImp
from daos.employee_dao import EmployeeDAO
from entities.employee import Employee

employee1 = Employee(0, "Linda", "Something")
employee2 = Employee(0, "Incorect", "Still wrong")
employee3 = Employee(0, "Rufus", "wait wrong show")

employee_dao: EmployeeDAO = EmployeeDAOImp()


def test_create_employee():
    print()
    print(employee1)
    employee_dao.create_employee(employee1)
    print(employee1)
    assert employee1.employee_id == 1


def test_get_employee_by_id():
    show = employee_dao.get_employee_by_id(1)
    print(show)
    assert show.employee_id == 1


def test_get_all_employees():
    employee_dao.create_employee(employee2)
    employee_dao.create_employee(employee3)
    elist = employee_dao.get_all_employees()
    assert len(elist) == 3


def test_update_employee():
    updated_employee = Employee(2, "Veronica", "is the boss")
    former_employee = employee_dao.get_employee_by_id(2)
    print(former_employee)
    employee_dao.update_employee(updated_employee)
    show = employee_dao.get_employee_by_id(2)
    print(show)
    assert show.first_name == "Veronica"


def test_delete_employee_pass():
    result = employee_dao.delete_employee(3)
    assert result
