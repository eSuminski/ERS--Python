from typing import List

from dao_imp.manger_dao_imp import ManagerDAOImp
from daos.manager_dao import ManagerDAO
from entities.manager import Manager
from services.manager_services import ManagerServices


class ManagerServicesImp(ManagerServices):

    def __init__(self, manager_dao: ManagerDAO):
        self.manager_dao = manager_dao

    def create_manager(self, manager: Manager) -> Manager:
        result = self.manager_dao.create_manager(manager)
        return result

    def get_manager_by_id(self, manager_id: int) -> Manager:
        result = self.manager_dao.get_manager_by_id(manager_id)
        return result

    def get_all_managers(self) -> List[Manager]:
        result = self.manager_dao.get_all_managers()
        return result

    def update_manager(self, manager: Manager) -> Manager:
        result = self.manager_dao.update_manager(manager)
        return result

    def delete_manager(self, manager_id) -> bool:
        result = self.manager_dao.delete_manager(manager_id)
        return result
