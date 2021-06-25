from behave import given, when, then
import time


@given(u'The manager is on the login home page')
def step_impl(context):
    context.driver.get("C:\\Users\\rctol\\Desktop\\coding\\Paid Training\\Project1\\project1htmlpages\\login.html")


@when(u'The manager types {username} into the username input')
def step_impl(context, username: str):
    context.login_home_page.username_input().send_keys(username)


@when(u'The manager types {password} into the password input')
def step_impl(context, password: str):
    context.login_home_page.password_input().send_keys(password)


@when(u'The manager clicks the login button')
def step_impl(context):
    context.login_home_page.login_button().click()
    time.sleep(.5)
