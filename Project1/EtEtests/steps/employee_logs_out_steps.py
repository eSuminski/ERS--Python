import time
from behave import when, then


@when(u'The employee clicks the Logout button')
def step_impl(context):
    context.employee_home_page.logout_button().click()
    time.sleep(.5)


@then(u'The employee should be returned to the Login page')
def step_impl(context):
    assert context.driver.title == "Login"
