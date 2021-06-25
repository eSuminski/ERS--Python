import time

from behave import when

@when(u'The manager clicks the edit button on reimbursement 1')
def step_impl(context):
    context.manager_home_page.edit_button_1().click()
    time.sleep(.5)
