from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import pytest

# @pytest.mark.usefixtures("setup")

from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    @pytest.mark.FullValidation
    def test_e2e(self):
        log = self.GetLogger()
        country = "France"
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        # checkOutPage = CheckOutPage(self.driver)
        Products = checkOutPage.selectItems()
        selectCase = ConfirmPage(self.driver)
        # Products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        i = -1
        for x in Products:
            i = i + 1
            productname = x.text
            if productname == "Blackberry":
                checkOutPage.GetCardTitles()[i].click()

        time.sleep(1)
        self.driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
        ProductSelected = self.driver.find_element_by_xpath("//h4").text
        print (ProductSelected)

        checkOutPage.CheckOutClick().click()
        selectCase.selectcase().send_keys("fra")
        # self.driver.find_element_by_css_selector("#country").send_keys("fra")
        self.VerifyLinkPresence("France")
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element_by_xpath("//div[@class='suggestions']")).click().perform()
        Result = self.driver.find_element_by_css_selector("#country").get_attribute("value")
        print (Result)
        checkbox = self.driver.find_element_by_css_selector("#checkbox2")
        self.driver.execute_script("arguments[0].click();", checkbox)
        self.driver.find_element_by_xpath("//input[@class='btn btn-success btn-lg']").click()
        time.sleep(2)
        message = self.driver.find_element_by_class_name("alert-success").text
        print (message)
        assert "Success! Thank you!" in message, log.error("message is wrong")
        log.info("message is correct")
