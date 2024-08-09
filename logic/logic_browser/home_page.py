import time

from logic.logic_browser.base_page_app import BasePageApp
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class HomePage(BasePageApp):
    ADD_TO_FAVORITES = '//div[@class="favorite-star"]'

    def __init__(self, driver):
        """
        Initializes the BoardPage with the provided WebDriver instance.

        :param driver: The WebDriver instance to use for browser interactions.
        """
        super().__init__(driver)

    def click_on_the_first_add_to_favorite_button(self):
        WebDriverWait(self._driver, 15).until(
            EC.presence_of_all_elements_located((By.XPATH, self.ADD_TO_FAVORITES)))[0].click()

    def click_on_the_first_remove_from_favorite_button(self):
        self.click_on_the_first_add_to_favorite_button()
        time.sleep(1)
        self.click_on_the_first_add_to_favorite_button()

