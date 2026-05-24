from pages.base_page import BasePage
from config import config
from locators.secure_page_locators import SecurePageLocators

class SecurePage(BasePage):
    URL = f"{config.BASE_URL}/secure"

    def is_on_secure_page(self) -> bool:
        return self.URL in self.page.url

    def logout(self) -> None:
        self.click_element(SecurePageLocators.LOGOUT_BUTTON)

    def is_logout_button_visible(self) -> bool:
        return self.is_element_visible(SecurePageLocators.LOGOUT_BUTTON)

    def get_page_content(self):
        return self.page.text_content("body")
