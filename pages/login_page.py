from pages.base_page import BasePage
from config import config
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    URL = f"{config.BASE_URL}/login"

    def open(self):
        self.navigate(self.URL)

    def login(self, username: str, password: str):
        self.fill_text(LoginPageLocators.USERNAME_INPUT, username)
        self.fill_text(LoginPageLocators.PASSWORD_INPUT, password)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    def is_error_message_visible(self):
        return self.is_element_visible(LoginPageLocators.ERROR_MESSAGE)
