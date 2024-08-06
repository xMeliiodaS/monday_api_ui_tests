from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from infra.browser.base_page import BasePage


class ArchivePage(BasePage):
    ARCHIVED_TASK = '//span[@class="lu7xO fs-mask" and text() ="{}"]'

    def __init__(self, driver):
        """
        Initializes the HomePage with the provided WebDriver instance.

        :param driver: The WebDriver instance to use for browser interactions.
        """
        super().__init__(driver)

    def is_task_in_archive(self, task_name):
        archived_task = self.ARCHIVED_TASK.format(task_name)
        WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((By.XPATH, archived_task))).is_displayed()
