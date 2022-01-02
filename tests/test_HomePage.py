import pytest

from TestDatas.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium.webdriver.support.select import Select


class TestHomePage(BaseClass):
    @pytest.mark.Intake
    @pytest.mark.FullValidation
    def test_formSumission(self, GetDatas):
        log = self.GetLogger()
        homepage = HomePage(self.driver)
        homepage.GetName().send_keys(GetDatas["firstname"])
        log.info("first name is : "+GetDatas["firstname"])
        homepage.GetEmail().send_keys(GetDatas["email"])
        log.info("email is : "+GetDatas["email"])
        homepage.Check().click()
        homepage.RadioSelect().click()
        homepage.SubmitSelect().click()
        message = homepage.AlertMessage().text
        log.info(message)
        # logs

        assert "submitted" in message  # check
        self.GenderSelect(homepage.Gender(), GetDatas["gender"])
        log.info("Gender is : " + GetDatas["gender"])
        gendertext = homepage.Gender().text
        print (gendertext)
        # OR
        # dropdown.select_by_index(1)
    @pytest.fixture(params=HomePageData.GetTestData("TestCase1"))
    def GetDatas(self, request):
        return request.param