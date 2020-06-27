import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import logging
import sys
from allure_commons.types import AttachmentType
import allure


class BaseTest:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
        self.log = logging.getLogger("Registration Test")
        logging.basicConfig(stream=sys.stderr, level=logging.INFO)

        yield
        if sys.exc_info()[0]:
            allure.attach(self.driver.get_screenshot_as_png(), name="Test failed", attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("Test_failed.png")
        self.driver.quit()
