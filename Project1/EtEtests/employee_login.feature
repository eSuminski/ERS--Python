Feature: Employee Login

  Scenario Outline: Employee logs in
    Given The employee is on the login home page
    When  The employee types <username> into the username input
    When  The employee types <password> into the password input
    When  The employee clicks the login button
    Then  The title should be <title>

    Examples: Employee login
      |username |password |title |
      |Linderp |Fl0w3rs |Employee Homepage|
