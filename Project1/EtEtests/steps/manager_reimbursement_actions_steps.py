from behave import when
import time

from selenium.webdriver.common.alert import Alert


@when(u'The manager clicks the button on reimbursement 1')
def step_impl(context):
    context.manager_home_page.approve_deny_button_1().click()


@when(u'The manager enters {number} into the approval status input')
def step_impl(context, number: int):
    context.deny_approve_page.approval_key_input().send_keys(number)


@when(u'The manager enters {reason} into the reason input')
def step_impl(context, reason: str):
    context.deny_approve_page.reason_input().send_keys(reason)


@when(u'The manager clicks the submit button')
def step_impl(context):
    context.deny_approve_page.approve_deny_button().click()
    time.sleep(1)


@when(u'The manager clicks the alert button')
def step_impl(context):
    alert = Alert(context.driver)
    alert.accept()
    time.sleep(.5)
