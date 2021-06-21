from abc import ABC, abstractmethod
from typing import List

from entities.employee_login import EmployeeLogin


class EmployeeLoginServices(ABC):

    @abstractmethod
    def create_employee_login(self, employee_login: EmployeeLogin) -> EmployeeLogin:
        pass

    @abstractmethod
    def get_employee_login_by_id(self, user_id: int) -> EmployeeLogin:
        pass

    @abstractmethod
    def get_all_employee_logins(self) -> List[EmployeeLogin]:
        pass

    @abstractmethod
    def update_employee_login(self, employee_login: EmployeeLogin) -> EmployeeLogin:
        pass

    @abstractmethod
    def delete_employee_login(self, user_id: int) -> bool:
        pass
