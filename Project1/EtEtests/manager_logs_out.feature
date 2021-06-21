Feature: Manager Logs Out

  Scenario: Manager logs out

    Given The manager is on the Manager Homepage
    When  The manager clicks on the logout button
    Then  The manager should be returned to the Login page