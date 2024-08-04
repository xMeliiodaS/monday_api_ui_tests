from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from infra.browser.base_page import BasePage


class BoardPage(BasePage):
    # ------------------Locators related to the creating task------------------
    TASK_NAME = '//div[@class="ds-text-component line-clamp"]//span[text() = "lImd9Dmw"]'
    TASK_NAME_XPATH_PATTERN = '//div[@class="ds-text-component line-clamp"]//span[text() = "{}"]'

    def __init__(self, driver):
        """
        Initializes the BoardPage with the provided WebDriver instance.

        :param driver: The WebDriver instance to use for browser interactions.
        """
        super().__init__(driver)

    def is_task_name_displayed(self, task_name):
        """
        Checks if a task with the specified name is displayed on the board page.

        :param task_name: The name of the task to check for visibility.
        :return: True if the task is displayed, False otherwise.
        """
        task_xpath = self.TASK_NAME_XPATH_PATTERN.format(task_name)
        return WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((By.XPATH, task_xpath))).is_displayed()
