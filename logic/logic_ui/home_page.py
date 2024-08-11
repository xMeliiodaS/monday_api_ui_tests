import time

from logic.logic_ui.base_page_app import BasePageApp
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

    def toggle_first_favorite_status(self):
        """
        Toggles the favorite status of the first item in the list.
        If the item is not a favorite, it will be added to favorites;
         if it is already a favorite, it will be removed.
        """
        WebDriverWait(self._driver, 15).until(
            EC.presence_of_all_elements_located((By.XPATH, self.ADD_TO_FAVORITES)))[0].click()
        time.sleep(1)

    def click_on_the_first_remove_from_favorite_button(self):
        """
        Toggles the favorite status of the first item twice to remove it from favorites.
        """
        self.toggle_first_favorite_status()
        time.sleep(1)
        self.toggle_first_favorite_status()

