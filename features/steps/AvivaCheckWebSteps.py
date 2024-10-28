"""Test steps for validate Aviva web page."""

from behave import *
from  selenium import webdriver
from selenium.webdriver.common.by import By

@given('launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()


@when('open aviva web page')
def open_home_webpage(context):
    context.driver.get("https://www.aviva.com/")


@then('The title should be "{expected_title}"')
def verify_title(context, expected_title):
    accept_cookie_button = context.driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
    accept_cookie_button.click()

    actual_title = context.driver.title
    assert expected_title == actual_title

@then('close browser')
def close_browser(context):
    context.driver.close()
