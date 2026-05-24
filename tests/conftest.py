import pytest
from playwright.sync_api import Page
from config import config
from pages.main_page import MainPage
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    context_args = {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
    }
    return context_args

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    launch_args = {
        **browser_type_launch_args,
        "headless": config.HEADLESS,
        "slow_mo": 500
    }
    return launch_args

@pytest.fixture(scope="function")
def page(page: Page):
    page.set_default_timeout(config.TIMEOUT)
    yield page


@pytest.fixture(scope="function")
def main_page(page: Page):
    mp = MainPage(page)
    mp.open()
    yield mp

@pytest.fixture(scope="function")
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture(scope="session")
def base_url():
    return config.BASE_URL
