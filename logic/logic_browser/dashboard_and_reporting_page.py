import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from logic.enum.section import Section
from logic.logic_browser.base_page_app import BasePageApp


class DashboardAndReportingPage(BasePageApp):
    # ------------------Locators related to the number of tasks in sections------------------
    WORKING_ON_IT_SECTION = '//div[@id="overview-section-content_62488275"]//span[@class="unicode-bidi"]'
    STUCK_SECTION = '//div[@id="overview-section-content_62488276"]//span[@class="unicode-bidi"]'
    DONE_SECTION = '//div[@id="overview-section-content_62488277"]//span[@class="unicode-bidi"]'
    ALL_TASKS_SECTION = '//div[@id="overview-section-content_62488274"]//span[@class="unicode-bidi"]'

    def __init__(self, driver):
        """
        Initializes the BoardPage with the provided WebDriver instance.

        :param driver: The WebDriver instance to use for browser interactions.
        """
        super().__init__(driver)

    def get_task_count_in_section(self, section_xpath):
        """
        Gets the number of tasks in a specific section by XPath.

        :param section_xpath: The XPath of the section.
        :return: The count of tasks in the specified section.
        """
        task_count_element = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((By.XPATH, section_xpath))
        )
        task_count_text = task_count_element.text.strip()
        return int(task_count_text)

    def get_task_count_in_each_section(self):
        """
        Gets the number of tasks in each specified section.

        :return: A dictionary with section names as keys and task counts as values.
        """
        time.sleep(1.5)
        task_counts = {
            Section.WORKING_ON_IT.value: self.get_task_count_in_section(self.WORKING_ON_IT_SECTION),
            Section.STUCK.value: self.get_task_count_in_section(self.STUCK_SECTION),
            Section.DONE.value: self.get_task_count_in_section(self.DONE_SECTION)
        }
        return task_counts
