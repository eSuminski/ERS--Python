from dao_imp.reimbursement_dao_imp import ReimbursementDAOImp
from daos.reimbursements_dao import ReimbursementDAO
from entities.reimbursements import Reimbursements

reimbursement_dao: ReimbursementDAO = ReimbursementDAOImp()

reimbursement1 = Reimbursements(0, 1, 200.25, "To buy more coffee creamer", 0)
reimbursement2 = Reimbursements(0, 1, 210.25, "to keep Trixie out of daycare", 0)
reimbursement3 = Reimbursements(2, 1, 220.25, "to keep Veronica from finding out I illegally moved funds", 0)


def test_create_reimbursement():
    reimbursement_dao.create_reimbursement(reimbursement1)
    check = reimbursement_dao.select_reimbursement_by_id(1)
    assert check.reimbursement_id == 1


def test_select_reimbursement_by_id():
    result = reimbursement_dao.select_reimbursement_by_id(1)
    assert result.reimbursement_id == 1


def test_select_all_reimbursements():
    reimbursement_dao.create_reimbursement(reimbursement2)
    rlist = reimbursement_dao.select_all_reimbursements()
    assert len(rlist) == 2


def test_select_all_reimbursements_for_employee():
    reimbursements = reimbursement_dao.select_all_reimbursements_by_employee_id(1)
    assert len(reimbursements) == 2


def test_update_reimbursement():
    reimbursement_dao.update_reimbursement(reimbursement3)
    check = reimbursement_dao.select_reimbursement_by_id(2)
    assert check.reason == "to keep Veronica from finding out I illegally moved funds"


def test_delete_reimbursement():
    reimbursement_dao.delete_reimbursement(2)
    rlist = reimbursement_dao.select_all_reimbursements()
    assert len(rlist) == 1
