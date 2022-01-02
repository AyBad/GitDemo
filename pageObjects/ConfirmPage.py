from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    CountryCase = (By.CSS_SELECTOR, "#country")
    def selectcase(self):

        return self.driver.find_element(*ConfirmPage.CountryCase)