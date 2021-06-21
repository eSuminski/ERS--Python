from typing import List
from util.connection_util import connection
from daos.employee_dao import EmployeeDAO
from entities.employee import Employee


class EmployeeDAOImp(EmployeeDAO):

    def create_employee(self, employee: Employee) -> Employee:
        sql = """INSERT INTO "Project1".employees VALUES (DEFAULT, %s, %s) returning employee_id"""
        cursor = connection.cursor()
        cursor.execute(sql, (employee.first_name, employee.last_name))
        connection.commit()
        e_id = cursor.fetchone()[0]
        employee.employee_id = e_id
        return employee

    def get_employee_by_id(self, employee_id: int) -> Employee:
        sql = """SELECT * FROM "Project1".employees WHERE employee_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        record = cursor.fetchone()
        employee = Employee(*record)
        return employee

    def get_all_employees(self) -> List[Employee]:
        sql = """SELECT * FROM "Project1".employees"""
        cursor = connection.cursor()
        cursor.execute(sql)
        employee_record = cursor.fetchall()
        employee_list = []
        for e in employee_record:
            employee_list.append(Employee(*e))
        return employee_list

    def update_employee(self, employee: Employee) -> Employee:
        sql = """UPDATE "Project1".employees SET first_name = %s, last_name = %s WHERE employee_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, (employee.first_name, employee.last_name, employee.employee_id))
        connection.commit()
        return employee

    def delete_employee(self, employee_id: int) -> bool:
        sql = """DELETE FROM "Project1".employees WHERE employee_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        connection.commit()
        return True
