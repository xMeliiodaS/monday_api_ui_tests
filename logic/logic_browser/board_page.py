from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from infra.browser.base_page import BasePage


class BoardPage(BasePage):
    # ------------------Locators related to the creating task------------------
    TASK_NAME = '//div[@class="ds-text-component line-clamp"]//span[text() = "lImd9Dmw"]'

    def __init__(self, driver):
        """
        Initialize the Base App Page with a WebDriver instance.

        :param driver: The WebDriver instance to use for browser interactions.
        """
        super().__init__(driver)

    def is_task_name_displayed(self, task_name):
        return WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f'//div[@class="ds-text-component line-clamp"]'
                                                      f'//span[text() = "{task_name}"]'))).is_displayed()
