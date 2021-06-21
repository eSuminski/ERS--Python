from abc import ABC, abstractmethod
from typing import List

from entities.reimbursements import Reimbursements


class ReimbursementServices(ABC):

    @abstractmethod
    def create_reimbursement(self, reimbursement: Reimbursements) -> Reimbursements:
        pass

    @abstractmethod
    def get_reimbursement_by_id(self, reimbursement_id: int) -> Reimbursements:
        pass

    @abstractmethod
    def get_all_reimbursements(self) -> List[Reimbursements]:
        pass

    @abstractmethod
    def get_all_reimbursements_by_employee_id(self, employee_id: int) -> List[Reimbursements]:
        pass

    @abstractmethod
    def update_reimbursement(self, reimbursement: Reimbursements) -> Reimbursements:
        pass

    @abstractmethod
    def delete_reimbursement(self, reimbursement_id: int) -> bool:
        pass

    @abstractmethod
    def get_employee_id_for_most_reimbursement_requests(self):
        pass

    @abstractmethod
    def get_employee_id_for_most_reimbursement_payouts(self):
        pass

    @abstractmethod
    def get_average_reimbursement_payout(self):
        pass

    @abstractmethod
    def get_number_of_reimbursement_requests_total(self):
        pass

    @abstractmethod
    def get_number_of_reimbursement_requests_pending(self):
        pass

    @abstractmethod
    def get_number_of_reimbursement_requests_approved(self):
        pass

    @abstractmethod
    def get_number_of_reimbursement_requests_denied(self):
        pass
