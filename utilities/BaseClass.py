import pytest
import inspect
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    pass

    def GetLogger(self):
        loggerName = inspect.stack()[1][3] #to have the name of TC
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        return logger

    def VerifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def GenderSelect(self,path, visible_text):
        dropdown = Select(path)
        dropdown.select_by_visible_text(visible_text)