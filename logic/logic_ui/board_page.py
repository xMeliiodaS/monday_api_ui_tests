import random
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

from infra.config_provider import ConfigProvider
from logic.enum.section import Section
from logic.logic_ui.base_page_app import BasePageApp
from logic.utils import Utils as LogicUtils
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BoardPage(BasePageApp):
    # ------------------Locators related to creating a Task------------------
    NEW_TASK_BUTTON = '//button[text() = "New task"]'
    TASK_NAME_INPUT = '//input[@value ="New Task"]'
    CREATE_TASK_BUTTON = '//button[text() ="Create Task"]'

    # ------------------Locators related to the Task------------------
    TASKS_LIST = '//div[@class="kanban-gb-compact-card-inner-component"]'
    TASK_NAME = '//div[@class="ds-text-component line-clamp"]//span[text() = "{}"]'
    TASKS_NAME = '//div[@class="ds-text-component line-clamp"]/span'
    TASK_OPTIONS = '//i[@class="icon ellipsis icon-v2-ellipsis"]'
    UPDATE_TASK_NAME_BUTTON = '//div[@class="pulse-card-name-cell"]'
    UPDATE_TASK_NAME_INPUT = '//input[@class="ds-editable-input ds-editable-input-text-align focus-visible"]'

    # ------------------Locators related to deleting a Task------------------
    DELETE_TASK_BUTTON = '//span[text() = "Delete"]'
    DELETE_BUTTON_CONFIRMATION = '//button[text() = "Delete"]'

    # ------------------Locators related to the Sections------------------
    SECTIONS_NAME = '//span[@class="list-name list-name-left" and text() = "{}"]'

    # ------------------Locators related to the board header------------------
    SORT_SETTING_BUTTON = '//div[@class="board-filter-item-component sort-settings-component"]'
    CHOOSE_COLUMN_BUTTON = '//div[text() ="Choose column"]'
    INPUT_SEARCH_FILTER = '//input[@aria-label="Dropdown input"]'

    # ------------------Locators related to searching a task------------------
    SEARCH_BUTTON = '//div[@class="board-filter-input-wrapper_v2"]'
    SEARCH_INPUT = '//input[@placeholder = "Type to filter"]'
    CLEAR_SEARCH_BUTTON = '//button[@aria-label="Clear search"]'

    def __init__(self, driver):
        """
        Initializes the BoardPage with the provided WebDriver instance.

        :param driver: The WebDriver instance to use for browser interactions.
        """
        self.config = ConfigProvider.load_config_json()

        super().__init__(driver)

    # ------------------------------------------------------------------------

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
        try:
            options = self.get_task_elements()[0]
            options.click()
        except NoSuchElementException:
            print("The task's option element was not found. Which mean there is no tasks")

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

    # ------------------------------------------------------------------------

    def move_task_to_another_section(self, section_name, task_index=0):
        """
        Moves the first task in the tasks list to the 'Working On It' section.
        """
        # Locate the first task in the tasks list
        try:
            # Locate the task in the tasks list
            task = WebDriverWait(self._driver, 15).until(
                EC.presence_of_all_elements_located((By.XPATH, self.TASKS_LIST))
            )[task_index]
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error locating task at index {task_index}: {str(e)}")
            return

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

    def move_tasks_to_another_section(self, section_name, tasks_count):
        """
        Moves the specified number of tasks to the given section.

        :param section_name: The name of the target section to move tasks to.
        :param tasks_count: The number of tasks to move.
        """
        for i in range(tasks_count):
            # Move the task at the current index
            self.move_task_to_another_section(section_name, i)

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

    def get_task_count_in_each_section(self):
        """
        Gets the number of tasks in each specified section.

        :return: A dictionary with section names as keys and task counts as values.
        """
        task_counts = {}

        sections = [Section.WORKING_ON_IT.value, Section.STUCK.value, Section.DONE.value]
        for section in sections:
            task_counts[section] = self.get_task_count_in_section(section)
        return task_counts

    def move_tasks_to_another_sections(self):
        """
        Moves the tasks to the given section.
        """
        self.move_tasks_to_another_section(Section.WORKING_ON_IT.value, self.config['drag_to_working_on_it_count'])
        self.move_tasks_to_another_section(Section.STUCK.value, self.config['drag_to_stuck_count'])
        self.move_tasks_to_another_section(Section.DONE.value, self.config['drag_to_done_count'])

    # ------------------------------------------------------------------------

    def click_on_sort_setting_button(self):
        """
        Clicks on the sort setting button to open the sorting options.
        """
        WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.SORT_SETTING_BUTTON))).click()

    def click_on_choose_column_button_and_apply(self):
        """
        Clicks on the button to choose a column for sorting and applies the selection.
        """
        WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.CHOOSE_COLUMN_BUTTON))).click()

    def insert_the_column_name(self, column_name):
        """
        Enters the column name into the search filter input field and
        simulates pressing the Enter key to apply the filter.

        :param column_name: The name of the column to search for and select.
        """
        try:
            # Locate the input field for search filtering
            input_field = WebDriverWait(self._driver, 15).until(
                EC.presence_of_element_located((By.XPATH, self.INPUT_SEARCH_FILTER))
            )
            # Enter the column name and simulate pressing Enter
            input_field.send_keys(column_name)
            input_field.send_keys(Keys.RETURN)

            # Add a brief wait to ensure the action is completed
            time.sleep(1)

        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error locating or interacting with the search input field: {str(e)}")

    def choose_sort_flow(self, column_name):
        """
        Performs the full sorting flow by clicking on the sort settings button,
         choosing the column to sort by, and applying the sort.

        :param column_name: The name of the column to sort the tasks by.
        """
        self.click_on_sort_setting_button()
        self.click_on_choose_column_button_and_apply()
        self.insert_the_column_name(column_name)

    def check_if_tasks_is_sorted_by_name(self):
        """
        Checks if the tasks are sorted by name in ascending order.

        :return: True if tasks are sorted by name, False otherwise.
        """
        elements = WebDriverWait(self._driver, 15).until(
            EC.presence_of_all_elements_located((By.XPATH, self.TASKS_NAME)))
        tasks_name = LogicUtils.get_tasks_name(elements)

        is_sorted = tasks_name == sorted(tasks_name)

        return is_sorted

    def shuffle_tasks_name(self):
        """
        Shuffles the tasks names to create an unsorted list and checks if they are sorted.

        :return: True if tasks are still sorted, False otherwise.
        """
        elements = WebDriverWait(self._driver, 15).until(
            EC.presence_of_all_elements_located((By.XPATH, self.TASKS_NAME)))
        tasks_name = LogicUtils.get_tasks_name(elements)

        # Shuffle the tasks names
        shuffled_tasks_name = tasks_name[:]
        random.shuffle(shuffled_tasks_name)

        # Check if the shuffled list is sorted
        is_sorted_after_shuffle = shuffled_tasks_name == sorted(shuffled_tasks_name)

        return not is_sorted_after_shuffle

    # ------------------------------------------------------------------------

    def click_on_new_task_button(self):
        """
        Clicks on the button to create a new task after waiting and unsure it is clickable.
        """
        WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.NEW_TASK_BUTTON))).click()

    def fill_task_name_input(self, task_name):
        """
        Fills the task name input field with the provided task name.
        """
        WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.TASK_NAME_INPUT))).send_keys(task_name)

    def click_on_create_task_button(self):
        """
        Clicks on the button to create a task and waits until it is clickable.
        """
        WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.CREATE_TASK_BUTTON))).click()

    def create_tasks_with_names(self, task_names):
        """
        Creates multiple tasks using the provided list of task names.

        :param task_names: A list of task names to use for creating tasks.
        """
        for name in task_names:
            self.click_on_new_task_button()
            time.sleep(1)
            self.fill_task_name_input(name)
            time.sleep(1)
            self.click_on_create_task_button()
            time.sleep(1)

    def click_on_search_button(self):
        """
        Clicks on the search button and waits until it is clickable.
        """
        WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((By.XPATH, self.SEARCH_BUTTON))).click()

    def fill_search_input(self, task_name):
        """
        Fills the search input field with the provided task name.
        """
        WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((By.XPATH, self.SEARCH_INPUT))).send_keys(task_name)

    def check_if_searched_task_appear(self, task_name):
        """
        Checks if the searched task appears in the search results.

        :param task_name: The name of the task to verify.
        :return: True if only one task is displayed and its name matches the searched task, False otherwise.
        """
        time.sleep(2)
        is_only_one_task = len(WebDriverWait(self._driver, 15).until(
            EC.presence_of_all_elements_located((By.XPATH, self.TASKS_LIST)))) == 1

        task_xpath = self.TASK_NAME.format(task_name)
        is_the_task_name_displayed = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((By.XPATH, task_xpath))).is_displayed()

        return is_only_one_task and is_the_task_name_displayed

    def check_if_searched_task_does_not_appear(self):
        """
        Checks if no tasks appear in the search results.

        :return: True if no tasks are displayed, False otherwise.
        """
        time.sleep(2)
        elements = self._driver.find_elements(By.XPATH, self.TASKS_LIST)
        return len(elements) == 0

    def click_on_clear_search(self):
        """
        Clicks the clear search button after ensuring it is clickable.
        """
        WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.CLEAR_SEARCH_BUTTON))).click()

    def click_on_first_task_to_update(self):
        """
        Clicks the first task in the list to update after ensuring it is present.

        Handles the case where the task list element is not found by printing an error message.
        """
        try:
            WebDriverWait(self._driver, 15).until(
                EC.presence_of_all_elements_located((By.XPATH, self.TASKS_LIST)))[0].click()
        except NoSuchElementException:
            # Handle the exception, such as logging the error or performing alternative actions
            print("The task list element was not found.")

    def click_on_task_name_input(self):
        """
        Clicks the task name input field after ensuring it is clickable.
        """
        WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.UPDATE_TASK_NAME_BUTTON))).click()

    def fill_updated_task_name_in_input(self, updated_name):
        """
        Fills in the updated task name in the input field.

        :param updated_name: The new name to be set for the task.
        """
        WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((By.XPATH, self.UPDATE_TASK_NAME_BUTTON))).send_keys(updated_name)

    def update_task_name_flow(self, updated_name):
        """
        Performs the full flow to update a task name by clicking the task,
         the name input field, and filling in the new name.

        :param updated_name: The new name to be set for the task.
        """
        self.click_on_first_task_to_update()
        self.click_on_task_name_input()
        self.fill_updated_task_name_in_input(updated_name)
