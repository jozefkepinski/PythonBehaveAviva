from behave import *
from  selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.home_page import HomePage


@given('launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()


@when('open aviva web page')
def open_home_webpage(context):
    context.home_page = HomePage(context.driver)
    context.home_page.navigate_to_home_page()


@then('The title should be "{expected_title}"')
def verify_title(context, expected_title):
    context.home_page.accept_all_cookies()

    actual_title = context.home_page.get_title()
    assert expected_title == actual_title

@then('close browser')
def close_browser(context):
    context.driver.close()
