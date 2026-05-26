from pages.base_page import BasePage
from config import config
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    URL = config.BASE_URL

    def open(self) -> None:
        self.navigate(self.URL)

    def is_fork_me_on_github_visible(self) -> bool:
        return self.is_element_visible(MainPageLocators.FORK_ME_GITHUB)

    def get_links_count(self) -> int:
        return self.get_element_count(MainPageLocators.LINKS)

    def navigate_to_login(self) -> None:
        self.click_element(MainPageLocators.FORM_AUTHENTICATION)
