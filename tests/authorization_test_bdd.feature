Feature: Authorization test
  Checking if authorization works correctly

  Scenario: login attempt
    Given open login page
    And fill in login and password and click login button
    Then I should see success login page