Feature: InteractiveInvestors header links

  Scenario: the one where i check all the services links
    Given i am on the interactive investors page
    When i click on the services link in the header
    Then the links in the services_account menu should work
    Then the links in the services_investing menu should work
    Then the links in the services_investment types menu should work

  Scenario: the one where i check all the Pensions links
    Given i am on the interactive investors page
    When i click on the Pensions link in the header
    Then the links in the Pensions_pensions menu should work
    Then the links in the Pensions_retirement menu should work

  Scenario: the one where i check all the Investments links
    Given i am on the interactive investors page
    When i click on the Investments link in the header
    Then the links in the Investments_shares menu should work
    Then the links in the Investments_funds menu should work
    Then the links in the Investments_expertpicks menu should work
    Then the links in the Investments_markets menu should work

  Scenario: the one where i check all the help links
    Given i am on the interactive investors page
    When i click on the Help link in the header
    Then the links in the help_investments menu should work
    Then the links in the help_learn menu should work
    Then the links in the help_help menu should work

  Scenario: the one where i check  the news link
    Given i am on the interactive investors page
    When i click on the news link in the header
    Then the news link should work