from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class DenyApprovePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def approval_key_input(self):
        element: WebElement = self.driver.find_element_by_id("approvalKeyInput")
        return element

    def reason_input(self):
        element: WebElement = self.driver.find_element_by_id("approvalReasonInput")
        return element

    def approve_deny_button(self):
        element: WebElement = self.driver.find_element_by_id("submitDenyApprove")
        return element

