import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from infra.browser.base_page import BasePage


class BasePageApp(BasePage):
    # ------------------Locators related to the workspace------------------
    BOARD_SIDE_BAR_BUTTON = '//span[text() ="Monday_automation"]'
    DASHBOARD_AND_REPORTING_BUTTON = '//span[text() ="Dashboard and reporting"]'
    FAVORITES_SECTION = '//span[text() ="Favorites"]'
    BOARDS_IN_SIDEBAR = '//div[@class="home-item-content"]'

    # ------------------Locators related to the menu------------------
    MENU_BUTTON = '//div[@id="surface-avatar-menu-component"]'
    ARCHIVE_BUTTON = '//span[@class="ds-title" and text() = "Archive"]'

    def __init__(self, driver):
        """
        Initializes the HomePage with the provided WebDriver instance.

        :param driver: The WebDriver instance to use for browser interactions.
        """
        super().__init__(driver)

    def click_on_the_board_side_bar_button(self):
        """
        Clicks the board button on the home page after ensuring it's clickable.
        """
        WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.BOARD_SIDE_BAR_BUTTON))).click()

    def click_on_the_dashboard_and_reporting_button(self):
        """
        Clicks the dashboard and reporting button on the home page after ensuring it's clickable.
        """
        WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.DASHBOARD_AND_REPORTING_BUTTON))).click()

    def click_on_the_menu_button(self):
        """
        Clicks on the menu button and waits until it is clickable.
        """
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.MENU_BUTTON))).click()

    def click_on_the_archive_button(self):
        """
        Clicks on the archive button and waits until it is clickable.
        """
        WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.ARCHIVE_BUTTON))).click()

    def click_on_favorite_on_sidebar_button(self):
        """
        Clicks on the favorites section button and waits until it is clickable.
        """
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.FAVORITES_SECTION))).click()

    def check_if_favorite_section_have_board(self):
        """
        Checks if the favorites section in the sidebar contains any boards.

        :return: True if boards are present; otherwise, False.
        """
        time.sleep(1)
        elements = self._driver.find_elements(By.XPATH, self.BOARDS_IN_SIDEBAR)

        return bool(elements)
