import time
from selenium.webdriver.common.alert import Alert
from behave import given, when, then

@given(u'The employee is logged in and on the Employee Homepage')
def step_impl(context):
    context.driver.get("C:\\Users\\rctol\\Desktop\\coding\\Paid Training\\Project1\\project1htmlpages\\login.html")
    context.login_home_page.username_input().send_keys("Linderp")
    context.login_home_page.password_input().send_keys("Fl0w3rs")
    context.login_home_page.login_button().click()
    time.sleep(1)


@when(u'The employee clicks the Submit Reimbursement Request')
def step_impl(context):
    context.employee_home_page.reimbursement_request_button().click()


@when(u'The employee enters {value} into the Reimbursement Amount')
def step_impl(context, value: int):
    context.submit_reimbursement_page.reimbursement_amount_input().send_keys(value)


@when(u'The employee enters {reason} into the Reason section for the reimbursement')
def step_impl(context, reason: str):
    context.submit_reimbursement_page.reason_input().send_keys(reason)


@when(u'The employee clicks the submit button')
def step_impl(context):
    context.submit_reimbursement_page.submit_button().click()
    time.sleep(1)


@when(u'The employee clicks the ok button on the alert')
def step_impl(context):
    alert = Alert(context.driver)
    alert.accept()
    time.sleep(.5)


@then(u'The employee should be returned to the Employee Homepage titled {title}')
def step_impl(context, title: str):
    assert context.driver.title == title
