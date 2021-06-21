import logging
from flask import Flask, request, jsonify
from flask_cors import CORS

from dao_imp.employee_dao_imp import EmployeeDAOImp
from dao_imp.employee_login_dao_imp import EmployeeLoginDAOImp
from dao_imp.manager_login_dao_imp import ManagerLoginDAOImp
from dao_imp.manger_dao_imp import ManagerDAOImp
from dao_imp.reimbursement_dao_imp import ReimbursementDAOImp
from entities.employee import Employee
from entities.manager import Manager
from entities.reimbursements import Reimbursements
from services_imp.employee_login_services_imp import EmployeeLoginServicesImp
from services_imp.employee_services_imp import EmployeeServicesImp
from services_imp.login_imp import LoginImp
from services_imp.manager_login_services_imp import ManagerLoginServicesImp
from services_imp.manger_services_imp import ManagerServicesImp
from services_imp.reimbursement_services_imp import ReimbursementServicesImp

app: Flask = Flask(__name__)
CORS(app)
logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")

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


@app.get("/hello")
def hello():
    return "Hello"


@app.get("/login")
def initial_login():
    try:
        username = request.args.get("username")
        password = request.args.get("password")
        if username is not None:
            if password is not None:
                try:
                    user = login_services.login(str(username), str(password))
                    if isinstance(user, Employee):
                        json_user: Employee = user.as_json_dict()
                        return jsonify(json_user), 200
                    if isinstance(user, Manager):
                        json_user: Manager = user.as_json_dict()
                        return jsonify(json_user), 200
                    login_fail = {"loginFail": "No user with those login credentials was found"}
                    return jsonify(login_fail), 404
                except:
                    catastrophic_failure = {"catastrophe": "You broke it. It's your fault"}
                    return jsonify(catastrophic_failure), 400
    except:
        catastrophic_failure = {"catastrophe": "You broke it. It's your fault"}
        return jsonify(catastrophic_failure), 400


@app.get("/employee")
def get_employee_reimbursements():
    try:
        user = request.args.get("user")
        if user != "null":
            employee_reimbursements = reimbursement_service.get_all_reimbursements_by_employee_id(int(user))
            json_employee_reimbursements = [r.as_json_dict() for r in employee_reimbursements]
            return jsonify(json_employee_reimbursements), 200
        table_fetch_fail = {"tableFail": "No employee ID was found. You will now be redirected"}
        return jsonify(table_fetch_fail), 404
    except:
        catastrophic_failure = {"catastrophe": "You broke it. It's your fault"}
        return jsonify(catastrophic_failure), 400


@app.get("/manager")
def get_all_employee_reimbursements():
    try:
        user = request.args.get("user")
        if user != "null":
            employee_reimbursements = reimbursement_service.get_all_reimbursements()
            json_employee_reimbursements = [r.as_json_dict() for r in employee_reimbursements]
            return jsonify(json_employee_reimbursements), 200
        table_fetch_fail = {"tableFail": "No manager ID was found. You will now be redirected"}
        return jsonify(table_fetch_fail), 404
    except:
        catastrophic_failure = {"catastrophe": "You broke it. It's your fault"}
        return jsonify(catastrophic_failure), 400


@app.post("/employee")
def create_reimbursement_request():
    try:
        user = request.args.get("user")
        if user != "null":
            body = request.json
            reimbursement = Reimbursements(0, user, body["reimbursement"], body["reason"])
            reimbursement_service.create_reimbursement(reimbursement)
            success_message = {"successMessage": "Your request went through"}
            return jsonify(success_message), 201
        reimbursement_fail = {"reimbursementFail": "No employee ID was found. You will now be redirected"}
        return jsonify(reimbursement_fail), 404
    except:
        catastrophic_failure = {"catastrophe": "You broke it. It's your fault"}
        return jsonify(catastrophic_failure), 400


@app.patch("/manager")
def deny_approve_reimbursement():
    try:
        body = request.json
        reimbursement = Reimbursements(
            body["reimbursementID"],
            body["employeeID"],
            body["reimbursement"],
            body["reason"],
            body["approval"],
            body["managerComment"]
        )
        reimbursement_service.update_reimbursement(reimbursement)
        success_message = {"successMessage": "Your decision went through"}
        return jsonify(success_message), 201
    except:
        catastrophic_failure = {"catastrophe": "You broke it. It's your fault"}
        return jsonify(catastrophic_failure), 400


@app.get("/manager/most")
def get_most_reimbursement_requests():
    try:
        greedy_employee = employee_services.get_employee_by_id(
            reimbursement_service.get_employee_id_for_most_reimbursement_requests())
        json_greedy_employee = greedy_employee.as_json_dict()
        return jsonify(json_greedy_employee), 200
    except:
        catastrophic_failure = {"catastrophe": "You broke it. It's your fault"}
        return jsonify(catastrophic_failure), 400


@app.get("/manager/payouts")
def get_most_payouts_request():
    try:
        lucky_employee = employee_services.get_employee_by_id(
            reimbursement_service.get_employee_id_for_most_reimbursement_payouts())
        json_lucky_employee = lucky_employee.as_json_dict()
        return jsonify(json_lucky_employee), 200
    except:
        catastrophic_failure = {"catastrophe": "You broke it. It's your fault"}
        return jsonify(catastrophic_failure), 400


@app.get("/manager/average")
def get_average_payout_request():
    try:
        average_payout = reimbursement_service.get_average_reimbursement_payout()
        json_average_payout = {"averagePayout": average_payout}
        return jsonify(json_average_payout), 200
    except:
        catastrophic_failure = {"catastrophe": "You broke it. It's your fault"}
        return jsonify(catastrophic_failure), 400


@app.get("/manager/total")
def get_total_payouts_request():
    try:
        total_reimbursement_requests = reimbursement_service.get_number_of_reimbursement_requests_total()
        json_total_reimbursement_requests = {"totalRequests": total_reimbursement_requests}
        return jsonify(json_total_reimbursement_requests), 200
    except:
        catastrophic_failure = {"catastrophe": "You broke it. It's your fault"}
        return jsonify(catastrophic_failure), 400


@app.get("/manager/pending")
def get_pending_payout_request():
    try:
        pending_reimbursement_requests = reimbursement_service.get_number_of_reimbursement_requests_pending()
        json_pending_reimbursement_requests = {"pendingRequests": pending_reimbursement_requests}
        return jsonify(json_pending_reimbursement_requests), 200
    except:
        catastrophic_failure = {"catastrophe": "You broke it. It's your fault"}
        return jsonify(catastrophic_failure), 400


@app.get("/manager/approved")
def get_approved_payout_request():
    try:
        approved_reimbursement_requests = reimbursement_service.get_number_of_reimbursement_requests_approved()
        json_approved_reimbursement_requests = {"approvedRequests": approved_reimbursement_requests}
        return jsonify(json_approved_reimbursement_requests), 200

    except:
        catastrophic_failure = {"catastrophe": "You broke it. It's your fault"}
        return jsonify(catastrophic_failure), 400


@app.get("/manager/denied")
def get_denied_payout_request():
    try:
        denied_reimbursement_requests = reimbursement_service.get_number_of_reimbursement_requests_denied()
        json_denied_reimbursement_requests = {"deniedRequests": denied_reimbursement_requests}
        return jsonify(json_denied_reimbursement_requests), 200
    except:
        catastrophic_failure = {"catastrophe": "You broke it. It's your fault"}
        return jsonify(catastrophic_failure), 400


if __name__ == '__main__':
    app.run()
