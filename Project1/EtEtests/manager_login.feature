Feature: Manager Login

  Scenario Outline: Manager logs in
    Given The manager is on the login home page
    When  The manager types <username> into the username input
    When  The manager types <password> into the password input
    When  The manager clicks the login button
    Then  The title should be <title>

    Examples: Manager info
      |username |password |title |
      |Teddington |P@333OrD |Manager Homepage|