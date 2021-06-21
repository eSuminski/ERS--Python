Feature: Manager Reimbursement Actions

  Scenario Outline: Manager accepts/denies reimbursement

    Given The manager is on the Manager Homepage
    When  The manager clicks the button on reimbursement 1
    When  The manager enters <number> into the approval status input
    When  The manager enters <reason> into the reason input
    When  The manager clicks the submit button
    When  The manager clicks the alert button
    Then  The title should be <title>

    Examples: Manager inputs
    |number |reason |title |
    |2 |Stop stealing creamer! |Manager Homepage|

    