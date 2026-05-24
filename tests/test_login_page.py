from config import config
from pages.login_page import LoginPage
from pages.main_page import MainPage

class TestLoginPage:

    def test_negative_to_login_page(self, main_page: MainPage):
        main_page.navigate_to_login()
        assert "/login" in main_page.page.url, "Not navigated to login page"

    def test_login_with_empty_credentials(self, main_page: MainPage, login_page: LoginPage):
        main_page.navigate_to_login()
        login_page.login(username="", password= "")
        assert login_page.is_error_message_visible(), "Error message not shown for empty credentials"

    def test_login_with_invalid_username(self, main_page: MainPage, login_page: LoginPage):
        main_page.navigate_to_login()
        login_page.login(username="invalid_username", password=config.VALID_PASSWORD)
        assert login_page.is_error_message_visible(), "Error message not shown for invalid username"

    def test_login_with_invalid_password(self, main_page: MainPage, login_page: LoginPage):
        main_page.navigate_to_login()
        login_page.login(username=config.VALID_USERNAME, password="wrong_password")
        assert login_page.is_error_message_visible(), "Error message not shown for invalid password"

    def test_login_with_valid_credentials(self, main_page: MainPage, login_page: LoginPage):
        main_page.navigate_to_login()
        login_page.login(username="invalid_username", password="wrong_password")
