class Reimbursements:

    def __init__(self, reimbursement_id: int, employee_id: int, reimbursement: float, reason: str,
                 approval: int = 0, manager_comment: str = ""):
        self.reimbursement_id = reimbursement_id
        self.employee_id = employee_id
        self.reimbursement = reimbursement
        self.reason = reason
        self.approval = approval
        self.manager_comment = manager_comment

    def __str__(self):
        return f"reimbursement ID: {self.reimbursement_id}, employee ID: {self.employee_id}, reimbursement: {self.reimbursement}, reason: {self.reason}, approval: {self.approval}, manager comment: {self.manager_comment} "

    def as_json_dict(self):
        return {
            "reimbursementID": self.reimbursement_id,
            "employeeID": self.employee_id,
            "reimbursement": self.reimbursement,
            "reason": self.reason,
            "approval": self.approval,
            "managerComment": self.manager_comment
        }
