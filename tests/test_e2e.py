from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from config import config


class TestE2E:
    def test_e2e(self, login_page: LoginPage):
        login_page.open()
        login_page.login(config.VALID_USERNAME, config.VALID_PASSWORD)

        secure_page = SecurePage(login_page.page)
        assert secure_page.is_on_secure_page(), "Not on secure page after login"

        title = secure_page.get_page_title()
        content = secure_page.get_page_content()
        assert title, "Page title is empty"
        assert content, "Page content is empty"
        assert "Secure Area" in content, "Expected content not found"

        secure_page.logout()

        assert "/login" in secure_page.page.url, "Not redirected to login page"
        assert not secure_page.is_logout_button_visible(), "Still on secure page"
