import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from infra.browser.base_page import BasePage


class BoardPage(BasePage):
    # ------------------Locators related to the Task------------------
    TASKS_LIST = '//div[@class="kanban-gb-compact-card-inner-component"]'
    TASK_NAME = '//div[@class="ds-text-component line-clamp"]//span[text() = "{}"]'
    TASK_OPTIONS = '//i[@class="icon ellipsis icon-v2-ellipsis"]'

    # ------------------Locators related to deleting a Task------------------
    DELETE_TASK_BUTTON = '//span[text() = "Delete"]'
    DELETE_BUTTON_CONFIRMATION = '//button[text() = "Delete"]'

    # ------------------Locators related to the Sections------------------
    WORKING_ON_IT_SECTION_ID = '//div[@id="kanban-gb-card-container_0_no_group"]'
    SECTIONS_NAME = '//span[@class="list-name list-name-left" and text() = "{}"]'
    SECTIONS_TASK_COUNT = '//span[@class="list-name list-name-right" and text() = "/ 0"]'

    # ------------------Locators related to the board header------------------
    SORT_SETTING_BUTTON = '//div[@class="board-filter-item-component sort-settings-component"]'
    CHOOSE_COLUMN_BUTTON = '//div[text() ="Choose column"]'
    INPUT_SEARCH_FILTER = '//input[@aria-label="Dropdown input"]'

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

    def delete_all_tasks_from_board(self):
        """
        Deletes all tasks from the board by iterating through task options and clicking
        the delete button for each. Stops when no more tasks are present.
        """
        elements_length = len(self.get_task_elements())

        for i in range(elements_length):
            self.click_task_option()
            self.click_delete_button()
            self.confirm_deletion()
            time.sleep(1.3)

    def get_task_elements(self):
        """
        Returns the list of task option elements on the board.
        """
        return WebDriverWait(self._driver, 15).until(
            EC.presence_of_all_elements_located((By.XPATH, self.TASK_OPTIONS))
        )

    def click_task_option(self):
        """
        Clicks on the first task option from the task options list.
        """
        options = self.get_task_elements()[0]
        options.click()

    def click_delete_button(self):
        """
        Clicks the delete button for a task.
        """
        WebDriverWait(self._driver, 8).until(
            EC.element_to_be_clickable((By.XPATH, self.DELETE_TASK_BUTTON))
        ).click()

    def confirm_deletion(self):
        """
        Clicks the confirmation button to finalize task deletion.
        """
        WebDriverWait(self._driver, 8).until(
            EC.element_to_be_clickable((By.XPATH, self.DELETE_BUTTON_CONFIRMATION))
        ).click()

    def move_task_to_another_section(self, section_name):
        """
        Moves the first task in the tasks list to the 'Working On It' section.
        """
        # Locate the first task in the tasks list
        task = WebDriverWait(self._driver, 15).until(
            EC.presence_of_all_elements_located((By.XPATH, self.TASKS_LIST)))[0]

        task_xpath = self.SECTIONS_NAME.format(section_name)

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

    def get_task_count_in_section(self, section_name):
        """
        Gets the number of tasks in a specific section by name.

        :param section_name: The name of the section.
        :return: The count of tasks in the specified section.
        """
        task_count_xpath = self.SECTIONS_NAME.format(
            section_name) + "/following-sibling::span[contains(@class, 'list-name list-name-right')]"
        task_count_element = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((By.XPATH, task_count_xpath))
        )
        task_count_text = task_count_element.text.strip().split("/")[1].strip()
        return int(task_count_text)

    def click_on_sort_setting_button(self):
        WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.SORT_SETTING_BUTTON))).click()

    def click_on_choose_column_button_and_apply(self):
        WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.CHOOSE_COLUMN_BUTTON))).click()

    def insert_the_column_name(self, column_name):
        input_field = WebDriverWait(self._driver, 15).until(
            EC.presence_of_all_elements_located((By.XPATH, self.INPUT_SEARCH_FILTER)))[0]
        input_field .send_keys(column_name)
        input_field .send_keys(Keys.RETURN)

    def choose_sort_flow(self, column_name):
        self.click_on_sort_setting_button()
        self.click_on_choose_column_button_and_apply()
        self.insert_the_column_name(column_name)
