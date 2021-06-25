import time
from behave import given, when, then

@given(u'The manager is on the Manager Homepage')
def step_impl(context):
    context.driver.get("C:\\Users\\rctol\\Desktop\\coding\\Paid Training\\Project1\\project1htmlpages\\login.html")
    context.login_home_page.username_input().send_keys("Teddington")
    context.login_home_page.password_input().send_keys("P@333OrD")
    context.login_home_page.login_button().click()
    time.sleep(.5)


@when(u'The manager clicks on the logout button')
def step_impl(context):
    context.manager_home_page.logout_button().click()
    time.sleep(.5)


@then(u'The manager should be returned to the Login page')
def step_impl(context):
    assert context.driver.title == "Login"
