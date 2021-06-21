from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class SubmitReimbursementPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def reimbursement_amount_input(self):
        element: WebElement = self.driver.find_element_by_id("amountInput")
        return element

    def reason_input(self):
        element: WebElement = self.driver.find_element_by_id("reasonInput")
        return element

    def submit_button(self):
        element: WebElement = self.driver.find_element_by_id("submitReimbursementButton")
        return element
