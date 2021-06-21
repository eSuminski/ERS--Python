Feature: Employee Submits Reimbursement

  Scenario Outline: Employee Submits a Reimbursement
    Given The employee is logged in and on the Employee Homepage
    When  The employee clicks the Submit Reimbursement Request
    When  The employee enters <value> into the Reimbursement Amount
    When  The employee enters <reason> into the Reason section for the reimbursement
    When  The employee clicks the submit button
    When  The employee clicks the ok button on the alert
    Then  The employee should be returned to the Employee Homepage titled <title>

    Examples:
    |value|reason|title|
    |100  |I like money|Employee Homepage|