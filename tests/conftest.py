import pytest
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--ignore-certificate-errors")
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", options=chrome_options)

    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
        driver.minimize_window()
        #geckodriver
    elif browser_name == "IE":
        print ("IE driver")

    driver.get("https://rahulshettyacademy.com/angularpractice/")


    request.cls.driver = driver
    yield
    driver.close()