import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from infra.browser.base_page import BasePage


class BoardPage(BasePage):
    # ------------------Locators related to the creating task------------------
    TASK_NAME = '//div[@class="ds-text-component line-clamp"]//span[text() = "lImd9Dmw"]'
    TASK_NAME_XPATH_PATTERN = '//div[@class="ds-text-component line-clamp"]//span[text() = "{}"]'
    TASK_OPTIONS = '//i[@class="icon ellipsis icon-v2-ellipsis"]'
    DELETE_TASK_BUTTON = '//span[text() = "Delete"]'
    DELETE_BUTTON_CONFIRMATION = '//button[text() = "Delete"]'
    FIRST_OPTION = '(//i[@class="icon ellipsis icon-v2-ellipsis"])[1]'

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

    def delete_all_tasks_from_board_v2(self):
        """
        Deletes all tasks from the board by iterating through task options and clicking
        the delete button for each. Stops when no more tasks are present.
        """
        elements_length = len(WebDriverWait(self._driver, 15).until(
            EC.presence_of_all_elements_located((By.XPATH, self.TASK_OPTIONS)))
        )
        for i in range(elements_length):
            # Get the first task
            element = self._driver.find_element(By.XPATH, self.FIRST_OPTION)
            element.click()

            WebDriverWait(self._driver, 8).until(
                EC.element_to_be_clickable((By.XPATH, self.DELETE_TASK_BUTTON))
            ).click()

            # Wait for the confirmation button to be clickable and click it
            WebDriverWait(self._driver, 8).until(
                EC.element_to_be_clickable((By.XPATH, self.DELETE_BUTTON_CONFIRMATION))
            ).click()

            time.sleep(1.3)
