from typing import List

from dao_imp.manager_login_dao_imp import ManagerLoginDAOImp
from daos.manager_login_dao import ManagerLoginDAO
from entities.manager_login import ManagerLogin
from services.manager_login_services import ManagerLoginServices


class ManagerLoginServicesImp(ManagerLoginServices):

    def __init__(self, manager_login: ManagerLoginDAO):
        self.manager_login = manager_login

    def create_manager_login(self, manager_login: ManagerLogin) -> ManagerLogin:
        result = self.manager_login.create_manager_login(manager_login)
        return result

    def select_manager_login_by_id(self, user_id: int) -> ManagerLogin:
        result = self.manager_login.select_manager_login_by_id(user_id)
        return result

    def select_all_manager_logins(self) -> List[ManagerLogin]:
        result = self.manager_login.select_all_manager_logins()
        return result

    def update_manager_login(self, manager_login: ManagerLogin) -> ManagerLogin:
        result = self.manager_login.update_manager_login(manager_login)
        return result

    def delete_manager_login(self, user_id: int) -> bool:
        result = self.manager_login.delete_manager_login(user_id)
        return result
