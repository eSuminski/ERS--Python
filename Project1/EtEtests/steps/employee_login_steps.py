import time

from behave import given, when, then



@given(u'The employee is on the login home page')
def step_impl(context):
    context.driver.get("C:\\Users\\rctol\\Desktop\\coding\\Paid Training\\Project1\\project1htmlpages\\login.html")


@when(u'The employee types {username} into the username input')
def step_impl(context, username: str):
    context.login_home_page.username_input().send_keys(username)


@when(u'The employee types {password} into the password input')
def step_impl(context, password: str):
    context.login_home_page.password_input().send_keys(password)
    print(password)


@when(u'The employee clicks the login button')
def step_impl(context):
    context.login_home_page.login_button().click()  # button was taking longer to load, so I added the time.sleep(1)
    time.sleep(.5)


@then(u'The title should be {title}')
def step_impl(context, title: str):
    assert context.driver.title == title
