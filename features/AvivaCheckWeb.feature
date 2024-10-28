Feature: Aviva Check Web Page

  This automation is for demonstrate capabilities of behave library with python language.

  Background:
    Given launch chrome browser
    When open aviva web page



  Scenario: Open Aviva Web page and validate it
    Then The title should be "Aviva corporate website - Aviva plc"
     And close browser

  Scenario Outline:
    Then The title should be "<title>"
     And close browser
    Examples:
    |title                              |
    |Aviva corporate website - Aviva plc|