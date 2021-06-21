from abc import ABC, abstractmethod
from typing import List

from entities.reimbursements import Reimbursements


class ReimbursementDAO(ABC):

    @abstractmethod
    def create_reimbursement(self, reimbursement: Reimbursements) -> Reimbursements:
        pass

    @abstractmethod
    def select_reimbursement_by_id(self, reimbursement_id: int) -> Reimbursements:
        pass

    @abstractmethod
    def select_all_reimbursements(self) -> List[Reimbursements]:
        pass

    @abstractmethod
    def select_all_reimbursements_by_employee_id(self, employee_id: int) -> List[Reimbursements]:
        pass

    @abstractmethod
    def update_reimbursement(self, reimbursement: Reimbursements) -> Reimbursements:
        pass

    @abstractmethod
    def delete_reimbursement(self, reimbursement_id: int) -> bool:
        pass
