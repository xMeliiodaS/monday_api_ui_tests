from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from infra.browser.base_page import BasePage


class HomePage(BasePage):
    # ------------------Locators related to the workspace------------------
    BOARD_BUTTON = '//div[@id="quick_search_item_board_1583771705"]'

    def __init__(self, driver):
        """
        Initializes the HomePage with the provided WebDriver instance.

        :param driver: The WebDriver instance to use for browser interactions.
        """
        super().__init__(driver)

    def click_on_the_board(self):
        """
        Clicks the board button on the home page after ensuring it's clickable.
        """
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.BOARD_BUTTON))).click()
