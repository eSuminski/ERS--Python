from collections import Counter
from statistics import mean
from typing import List

from daos.reimbursements_dao import ReimbursementDAO
from entities.reimbursements import Reimbursements
from services.reimbursement_services import ReimbursementServices


class ReimbursementServicesImp(ReimbursementServices):

    def __init__(self, reimbursement_dao: ReimbursementDAO):
        self.reimbursement_dao = reimbursement_dao

    def create_reimbursement(self, reimbursement: Reimbursements) -> Reimbursements:
        result = self.reimbursement_dao.create_reimbursement(reimbursement)
        return result

    def get_reimbursement_by_id(self, reimbursement_id: int) -> Reimbursements:
        result = self.reimbursement_dao.select_reimbursement_by_id(reimbursement_id)
        return result

    def get_all_reimbursements(self) -> List[Reimbursements]:
        result = self.reimbursement_dao.select_all_reimbursements()
        return result

    def get_all_reimbursements_by_employee_id(self, employee_id: int) -> List[Reimbursements]:
        result = self.reimbursement_dao.select_all_reimbursements_by_employee_id(employee_id)
        return result

    def update_reimbursement(self, reimbursement: Reimbursements) -> Reimbursements:
        result = self.reimbursement_dao.update_reimbursement(reimbursement)
        return result

    def delete_reimbursement(self, reimbursement_id: int) -> bool:
        result = self.reimbursement_dao.delete_reimbursement(reimbursement_id)
        return result

    def get_employee_id_for_most_reimbursement_requests(self):
        requests = self.reimbursement_dao.select_all_reimbursements()
        request_ids = []
        for r in requests:
            request_ids.append(r.employee_id)
        occurrence_count = Counter(request_ids)
        return occurrence_count.most_common(1)[0][0]

    def get_employee_id_for_most_reimbursement_payouts(self):
        requests = self.reimbursement_dao.select_all_reimbursements()
        payouts = []
        for r in requests:
            if r.approval == 1:
                payouts.append(r.employee_id)
        payouts_count = Counter(payouts)
        return payouts_count.most_common(1)[0][0]

    def get_average_reimbursement_payout(self):
        requests = self.reimbursement_dao.select_all_reimbursements()
        payouts = []
        for r in requests:
            if r.approval == 1:
                payouts.append(r.reimbursement)
        return mean(payouts)

    def get_number_of_reimbursement_requests_total(self):
        requests = self.reimbursement_dao.select_all_reimbursements()
        return len(requests)

    def get_number_of_reimbursement_requests_pending(self):
        requests = self.reimbursement_dao.select_all_reimbursements()
        pending = []
        for r in requests:
            if r.approval == 0:
                pending.append(r)
        return len(pending)

    def get_number_of_reimbursement_requests_approved(self):
        requests = self.reimbursement_dao.select_all_reimbursements()
        approved = []
        for r in requests:
            if r.approval == 1:
                approved.append(r)
        return len(approved)

    def get_number_of_reimbursement_requests_denied(self):
        requests = self.reimbursement_dao.select_all_reimbursements()
        denied = []
        for r in requests:
            if r.approval == 2:
                denied.append(r)
        return len(denied)
