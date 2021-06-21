Feature: Employee Logs Out

  Scenario: Employee logs out
    Given The employee is logged in and on the Employee Homepage
    When  The employee clicks the Logout button
    Then  The employee should be returned to the Login page
