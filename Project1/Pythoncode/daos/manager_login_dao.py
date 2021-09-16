from abc import ABC, abstractmethod
from typing import List

from entities.manager_login import ManagerLogin


class ManagerLoginDAO(ABC):

    @abstractmethod
    def create_manager_login(self, manager_login: ManagerLogin) -> ManagerLogin:
        pass

    @abstractmethod
    def select_manager_login_by_id(self, user_id: int) -> ManagerLogin:
        pass

    @abstractmethod
    def select_all_manager_logins(self) -> List[ManagerLogin]:
        pass

    @abstractmethod
    def update_manager_login(self, manager_login: ManagerLogin) -> ManagerLogin:
        pass

    @abstractmethod
    def delete_manager_login(self, user_id: int) -> bool:
        pass