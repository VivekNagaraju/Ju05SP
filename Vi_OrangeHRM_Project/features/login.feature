#Author: your.email@your.domain.com
#Keywords Summary :
#Feature: List of scenarios.
#Scenario: Business rule through list of steps with arguments.
#Given: Some precondition step
#When: Some key actions
#Then: To observe outcomes or validation
#And,But: To enumerate more Given,When,Then steps
#Scenario Outline: List of steps for data-driven as an Examples and <placeholder>
#Examples: Container for s table
#Background: List of steps run before each of the scenarios
#""" (Doc Strings)
#| (Data Tables)
#@ (Tags/Labels):To group Scenarios
#<> (placeholder)
#""
## (Comments)
#Sample Feature Definition Template
@tag
Feature: Login page feature

  @tag1
  Scenario: Navigation to OrangeHRM Login Page
    Given Chrome browser is launched
    When User navigates to OrangeHRM Login Page
    Then User should see page title as OrangeHRM

  @Login
  Scenario: Validate the login to OrangeHRM
    Given Chrome browser is launched
    When User navigates to OrangeHRM Login Page
    And User enters Username
    And User enters Password
    And User clicks on Login button
    Then User should see /dashboard/index in the current page URL

	@LoginWithParamters 
  Scenario: Validate the login to OrangeHRM with parameters
    Given Chrome browser is launched
    When User navigates to OrangeHRM Login Page
    And User enters Username "Admin"
    And User enters Password "admin123"
    And User clicks on Login button
    Then User should see "/dashboard/index" in the current page URL
    
    
    
  #@tag2
  #Scenario Outline: Title of your scenario outline
    #Given I want to write a step with <name>
    #When I check for the <value> in step
    #Then I verify the <status> in step
#
    #Examples: 
      #| name  | value | status  |
      #| name1 |     5 | success |
      #| name2 |     7 | Fail    |
