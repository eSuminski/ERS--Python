from typing import List
from util.connection_util import connection
from daos.reimbursements_dao import ReimbursementDAO
from entities.reimbursements import Reimbursements


class ReimbursementDAOImp(ReimbursementDAO):

    def create_reimbursement(self, reimbursement: Reimbursements) -> Reimbursements:
        sql = """INSERT INTO "Project1".reimbursement VALUES (DEFAULT, %s, %s, %s, %s, %s) returning reimbursement_id"""
        cursor = connection.cursor()
        cursor.execute(sql, (
            reimbursement.employee_id, reimbursement.reimbursement, reimbursement.reason, reimbursement.approval,
            reimbursement.manager_comment))
        connection.commit()
        r_id = cursor.fetchone()[0]
        reimbursement.reimbursement_id = r_id
        return reimbursement

    def select_reimbursement_by_id(self, reimbursement_id: int) -> Reimbursements:
        sql = """SELECT * FROM "Project1".reimbursement WHERE reimbursement_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [reimbursement_id])
        record = cursor.fetchone()
        reimbursement = Reimbursements(*record)
        return reimbursement

    def select_all_reimbursements(self) -> List[Reimbursements]:
        sql = """SELECT * FROM "Project1".reimbursement"""
        cursor = connection.cursor()
        cursor.execute(sql)
        reimbursement_record = cursor.fetchall()
        reimbursement_list = []
        for rl in reimbursement_record:
            reimbursement_list.append(Reimbursements(*rl))
        return reimbursement_list

    def select_all_reimbursements_by_employee_id(self, employee_id: int) -> List[Reimbursements]:
        sql = """SELECT * FROM "Project1".reimbursement WHERE employee_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        reimbursement_records_for_employee = cursor.fetchall()
        employee_reimbursements = []
        for er in reimbursement_records_for_employee:
            employee_reimbursements.append(Reimbursements(*er))
        return employee_reimbursements

    def update_reimbursement(self, reimbursement: Reimbursements) -> Reimbursements:
        sql = """UPDATE "Project1".reimbursement SET reimbursement = %s, reason = %s, approval = %s, manager_comment = %s WHERE 
        reimbursement_id = %s """
        cursor = connection.cursor()
        cursor.execute(sql, (
            reimbursement.reimbursement, reimbursement.reason, reimbursement.approval, reimbursement.manager_comment,
            reimbursement.reimbursement_id))
        connection.commit()
        return reimbursement

    def delete_reimbursement(self, reimbursement_id: int) -> bool:
        sql = """DELETE FROM "Project1".reimbursement WHERE reimbursement_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [reimbursement_id])
        connection.commit()
        return True
