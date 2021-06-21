from typing import List
from util.connection_util import connection
from daos.employee_login_dao import EmployeeLoginDAO
from entities.employee_login import EmployeeLogin


class EmployeeLoginDAOImp(EmployeeLoginDAO):
    # user_id needs to match employee id
    def create_employee_login(self, employee_login: EmployeeLogin) -> EmployeeLogin:
        sql = """INSERT INTO "Project1".employee_login VALUES (%s, %s, %s) returning user_id"""
        cursor = connection.cursor()
        cursor.execute(sql, (employee_login.user_id, employee_login.username, employee_login.u_password))
        connection.commit()
        e_l_id = cursor.fetchone()[0]
        employee_login.user_id = e_l_id
        return employee_login

    def get_employee_login_by_id(self, user_id: int) -> EmployeeLogin:
        sql = """SELECT * FROM "Project1".employee_login WHERE user_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [user_id])
        record = cursor.fetchone()
        employee_login = EmployeeLogin(*record)
        return employee_login

    def get_all_employee_logins(self) -> List[EmployeeLogin]:
        sql = """SELECT * FROM "Project1".employee_login"""
        cursor = connection.cursor()
        cursor.execute(sql)
        employee_login_record = cursor.fetchall()
        employee_login_list = []
        for el in employee_login_record:
            employee_login_list.append(EmployeeLogin(*el))
        return employee_login_list

    def update_employee_login(self, employee_login: EmployeeLogin) -> EmployeeLogin:
        sql = """UPDATE "Project1".employee_login SET username = %s, u_password = %s WHERE user_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, (employee_login.username, employee_login.u_password, employee_login.user_id))
        connection.commit()
        return employee_login

    def delete_employee_login(self, user_id: int) -> bool:
        sql = """DELETE FROM "Project1".employee_login WHERE user_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [user_id])
        connection.commit()
        return True
