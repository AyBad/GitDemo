from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    selectPhone = (By.CSS_SELECTOR, ".card-title a")
    CardFooter = (By.CSS_SELECTOR, ".card-footer button")
    CheckOutButton = (By.XPATH, "//button[@class='btn btn-success']")
    def selectItems(self):

        return self.driver.find_elements(*CheckOutPage.selectPhone)

    def GetCardTitles(self):

        return self.driver.find_elements(*CheckOutPage.CardFooter)

    def CheckOutClick(self):
        return self.driver.find_element(*CheckOutPage.CheckOutButton)

