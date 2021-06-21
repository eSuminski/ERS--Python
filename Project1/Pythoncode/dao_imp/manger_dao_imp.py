from typing import List

from daos.manager_dao import ManagerDAO
from entities.manager import Manager
from util.connection_util import connection


class ManagerDAOImp(ManagerDAO):

    def create_manager(self, manager: Manager) -> Manager:
        sql = """INSERT INTO "Project1".managers VALUES (DEFAULT, %s, %s) returning manager_id"""
        cursor = connection.cursor()
        cursor.execute(sql, (manager.first_name, manager.last_name))
        connection.commit()
        m_id = cursor.fetchone()[0]
        manager.manager_id = m_id
        return manager

    def get_manager_by_id(self, manager_id: int) -> Manager:
        sql = """SELECT * FROM "Project1".managers WHERE manager_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [manager_id])
        record = cursor.fetchone()
        manager = Manager(*record)
        return manager

    def get_all_managers(self) -> List[Manager]:
        sql = """SELECT * FROM "Project1".managers"""
        cursor = connection.cursor()
        cursor.execute(sql)
        manager_record = cursor.fetchall()
        manager_list = []
        for m in manager_record:
            manager_list.append(Manager(*m))
        return manager_list

    def update_manager(self, manager: Manager) -> Manager:
        sql = """UPDATE "Project1".managers SET first_name = %s, last_name = %s WHERE manager_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, (manager.first_name, manager.last_name, manager.manager_id))
        connection.commit()
        return manager

    def delete_manager(self, manager_id) -> bool:
        sql = """DELETE FROM "Project1".managers WHERE manager_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [manager_id])
        connection.commit()
        return True

