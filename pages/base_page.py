from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str) -> None:
        self.page.goto(url)

    def fill_text(self, locator: str, text: str) -> None:
        self.page.fill(locator, text)

    def get_page_title(self) -> str:
        return self.page.title()

    def is_element_visible(self, locator: str) -> bool:
        return self.page.is_visible(locator)

    def get_element_count(self, locator: str) -> int:
        return self.page.locator(locator).count()

    def click_element(self, locator: str) -> None:
        self.page.click(locator)
