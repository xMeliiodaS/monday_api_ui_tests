from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from infra.browser.base_page import BasePage


class BasePageApp(BasePage):
    # ------------------Locators related to the workspace------------------
    BOARD_SIDE_BAR_BUTTON = '//span[text() ="Monday_automation"]'
    DASHBOARD_AND_REPORTING_BUTTON = '//span[text() ="Dashboard and reporting"]'

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
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.BOARD_SIDE_BAR_BUTTON))).click()

    def click_on_the_dashboard_and_reporting_button(self):
        """
        Clicks the board button on the home page after ensuring it's clickable.
        """
        WebDriverWait(self._driver, 10).until(
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
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ARCHIVE_BUTTON))).click()
