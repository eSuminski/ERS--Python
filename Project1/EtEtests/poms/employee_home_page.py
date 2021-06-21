from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class EmployeeHomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def title_id(self):
        element: WebElement = self.driver.find_element_by_id("employeeHomePage")
        return element

    def reimbursement_request_button(self):
        element: WebElement = self.driver.find_element_by_id("reimbursementRequestButton")
        return element

    def logout_button(self):
        element: WebElement = self.driver.find_element_by_id("logoutButton")
        return element
