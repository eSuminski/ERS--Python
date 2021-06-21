from dao_imp.employee_dao_imp import EmployeeDAOImp
from dao_imp.employee_login_dao_imp import EmployeeLoginDAOImp
from dao_imp.manager_login_dao_imp import ManagerLoginDAOImp
from dao_imp.manger_dao_imp import ManagerDAOImp
from dao_imp.reimbursement_dao_imp import ReimbursementDAOImp
from entities.reimbursements import Reimbursements
from services_imp.employee_login_services_imp import EmployeeLoginServicesImp
from services_imp.employee_services_imp import EmployeeServicesImp
from services_imp.login_imp import LoginImp
from services_imp.manager_login_services_imp import ManagerLoginServicesImp
from services_imp.manger_services_imp import ManagerServicesImp
from services_imp.reimbursement_services_imp import ReimbursementServicesImp

employee_dao = EmployeeDAOImp()
employee_services: EmployeeServicesImp = EmployeeServicesImp(employee_dao)
manager_dao = ManagerDAOImp()
manager_services: ManagerServicesImp = ManagerServicesImp(manager_dao)
employee_login_dao = EmployeeLoginDAOImp()
employee_login_services: EmployeeLoginServicesImp = EmployeeLoginServicesImp(employee_login_dao)
manager_login_dao = ManagerLoginDAOImp()
manager_login_services: ManagerLoginServicesImp = ManagerLoginServicesImp(manager_login_dao)
reimbursement_dao = ReimbursementDAOImp()
reimbursement_service: ReimbursementServicesImp = ReimbursementServicesImp(reimbursement_dao)

login_services: LoginImp = LoginImp(employee_login_services, manager_login_services, employee_services,
                                    manager_services)


def test_employee_login():
    result = login_services.login("Linderp", "Fl0w3rs")
    print()
    print(result)
    assert result.first_name == "Linda"


def test_manager_login():
    result = login_services.login("Teddington", "P@333OrD")
    print()
    print(result)
    assert result.first_name == "Ted"


def test_get_employee_id_for_most_reimbursement_requests():
    reimbursement1 = Reimbursements(0, 2, 1000, "Cats", 1)
    reimbursement2 = Reimbursements(0, 2, 1000, "Dogs", 1)
    reimbursement3 = Reimbursements(0, 2, 1000, "I hate birds", 1)
    reimbursement4 = Reimbursements(0, 2, 1000, "Viva La Mexico", 1)
    reimbursement_service.create_reimbursement(reimbursement1)
    reimbursement_service.create_reimbursement(reimbursement2)
    reimbursement_service.create_reimbursement(reimbursement3)
    reimbursement_service.create_reimbursement(reimbursement4)
    result = reimbursement_service.get_employee_id_for_most_reimbursement_requests()
    assert result == 2


def test_get_employee_id_for_most_reimbursement_payouts():
    result = reimbursement_service.get_employee_id_for_most_reimbursement_payouts()
    assert result == 2


def test_get_average_reimbursement_payout():
    result = reimbursement_service.get_average_reimbursement_payout()
    assert result == 1000


def test_get_number_of_reimbursement_requests_total():
    result = reimbursement_service.get_number_of_reimbursement_requests_total()
    assert result == 5


def test_get_number_of_reimbursement_requests_pending():
    result = reimbursement_service.get_number_of_reimbursement_requests_pending()
    assert result == 1


def test_get_number_of_reimbursement_requests_approved():
    result = reimbursement_service.get_number_of_reimbursement_requests_approved()
    assert result == 4


def test_get_number_of_reimbursement_requests_denied():
    reimbursement5 = Reimbursements(0, 1, 1000, "should not be accepted", 2)
    reimbursement_service.create_reimbursement(reimbursement5)
    result = reimbursement_service.get_number_of_reimbursement_requests_denied()
    assert result == 1
