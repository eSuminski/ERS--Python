from typing import List
from daos.manager_login_dao import ManagerLoginDAO
from entities.manager_login import ManagerLogin
from util.connection_util import connection


class ManagerLoginDAOImp(ManagerLoginDAO):
    def create_manager_login(self, manager_login: ManagerLogin) -> ManagerLogin:
        sql = """INSERT INTO "Project1".manager_login VALUES (%s, %s, %s) returning user_id"""
        cursor = connection.cursor()
        cursor.execute(sql, (manager_login.user_id, manager_login.username, manager_login.u_password))
        connection.commit()
        m_l_id = cursor.fetchone()[0]
        manager_login.user_id = m_l_id
        return manager_login

    def select_manager_login_by_id(self, user_id: int) -> ManagerLogin:
        sql = """SELECT * FROM "Project1".manager_login WHERE user_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [user_id])
        record = cursor.fetchone()
        manager_login = ManagerLogin(*record)
        return manager_login

    def select_all_manager_logins(self) -> List[ManagerLogin]:
        sql = """SELECT * FROM "Project1".manager_login"""
        cursor = connection.cursor()
        cursor.execute(sql)
        manager_login_record = cursor.fetchall()
        manager_login_list = []
        for ml in manager_login_record:
            manager_login_list.append(ManagerLogin(*ml))
        return manager_login_list

    def update_manager_login(self, manager_login: ManagerLogin) -> ManagerLogin:
        sql = """UPDATE "Project1".manager_login SET username = %s, u_password = %s WHERE user_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, (manager_login.username, manager_login.u_password, manager_login.user_id))
        connection.commit()
        return manager_login

    def delete_manager_login(self, user_id: int) -> bool:
        sql = """DELETE FROM "Project1".manager_login WHERE user_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [user_id])
        connection.commit()
        return True
