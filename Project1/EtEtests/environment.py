from selenium import webdriver

from poms.approve_deny_page import DenyApprovePage
from poms.employee_home_page import EmployeeHomePage
from poms.login_page import LoginPage
from poms.manager_home_page import ManagerHomePage
from poms.submit_reimbursement_page import SubmitReimbursementPage


def before_all(context):
    context.driver = webdriver.Chrome("C:\\Users\\rctol\\Desktop\\coding\\chromedriver_win32\\chromedriver.exe")
    context.login_home_page = LoginPage(context.driver)
    context.employee_home_page = EmployeeHomePage(context.driver)
    context.manager_home_page = ManagerHomePage(context.driver)
    context.deny_approve_page = DenyApprovePage(context.driver)
    context.submit_reimbursement_page = SubmitReimbursementPage(context.driver)
    context.driver.implicitly_wait(5)


def after_all(context):
    context.driver.quit()
