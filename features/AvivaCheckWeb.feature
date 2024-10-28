Feature: Aviva Check Web Page

  This automation is for demonstrate capabilities of behave library with python language.

  Scenario: Open Aviva Web page and validate it
    Given launch chrome browser
    When open aviva web page
    Then The title should be "Aviva corporate website - Aviva plc"
    And close browser