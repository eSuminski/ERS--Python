from selenium.webdriver.chrome.webdriver import WebDriver


class ManagerHomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def logout_button(self):
        element: WebDriver = self.driver.find_element_by_id("logoutButton")
        return element

    def approve_deny_button_1(self):
        element: WebDriver = self.driver.find_element_by_id("denyApproveButton1")
        return element

    def edit_button_1(self):
        element: WebDriver = self.driver.find_element_by_id("editButton3")
        return element
