from pages.main_page import MainPage

class TestMainPage:

    def test_page_has_title(self, main_page: MainPage):
        title = main_page.get_page_title()
        assert title, "Page title is empty"

    def test_fork_me_github_visible(self, main_page: MainPage):
        assert main_page.is_fork_me_on_github_visible(), "Fork me on GitHub element not found"

    def test_page_has_links(self, main_page: MainPage):
        links_count = main_page.get_links_count()
        assert links_count == 44, f"Expected 44 links, but found {links_count}"
