from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckOutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    examplecheck = (By.ID, "exampleCheck1")
    radio = (By.CSS_SELECTOR, "#inlineRadio2")
    submit = (By.CSS_SELECTOR, "input[value='Submit']")
    alertsuccess = (By.CSS_SELECTOR, "[class*='alert-success']")
    gender = (By.ID, "exampleFormControlSelect1")


    def shopItems(self):
        #self.driver.find_element_by_css_selector("a[href*='shop']")
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def GetName(self):

        return self.driver.find_element(*HomePage.name)

    def GetEmail(self):

        return self.driver.find_element(*HomePage.email)

    def Check(self):

        return self.driver.find_element(*HomePage.examplecheck)

    def RadioSelect(self):

        return self.driver.find_element(*HomePage.radio)

    def SubmitSelect(self):

        return self.driver.find_element(*HomePage.submit)

    def AlertMessage(self):

        return self.driver.find_element(*HomePage.alertsuccess)

    def Gender(self):

        return self.driver.find_element(*HomePage.gender)

