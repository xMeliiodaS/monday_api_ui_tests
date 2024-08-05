import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from infra.browser.base_page import BasePage


class BoardPage(BasePage):
    # ------------------Locators related to the Task------------------
    TASKS_LIST = '//div[@class="kanban-gb-compact-card-inner-component"]'
    TASK_NAME = '//div[@class="ds-text-component line-clamp"]//span[text() = "{}"]'
    TASK_OPTIONS = '//i[@class="icon ellipsis icon-v2-ellipsis"]'
    DELETE_TASK_BUTTON = '//span[text() = "Delete"]'
    DELETE_BUTTON_CONFIRMATION = '//button[text() = "Delete"]'
    FIRST_OPTION = '(//i[@class="icon ellipsis icon-v2-ellipsis"])[1]'

    # ------------------Locators related to the Sections------------------
    WORKING_ON_IT_SECTION_ID = '//div[@id="kanban-gb-card-container_0_no_group"]'
    SECTIONS = '//span[@class="list-name list-name-left" and text() = "{}"]'

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
        task_xpath = self.TASK_NAME.format(task_name)
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

    def move_task_to_another_section(self, section_name):
        """
        Moves the first task in the tasks list to the 'Working On It' section.
        """
        # Locate the first task in the tasks list
        task = WebDriverWait(self._driver, 15).until(
            EC.presence_of_all_elements_located((By.XPATH, self.TASKS_LIST)))[0]

        task_xpath = self.SECTIONS.format(section_name)

        # Locate the target element representing the 'Working On It' section
        target_element = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((By.XPATH, task_xpath)))

        action = ActionChains(self._driver)
        action.click_and_hold(task)

        # Add a small wait to ensure the task is picked up
        time.sleep(0.3)

        # Move to the target element and add a slight wait before releasing
        action.move_to_element(target_element).perform()

        # Move the mouse a bit in the y offset
        action.move_by_offset(0, 50).release().perform()
