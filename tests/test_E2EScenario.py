import pytest
from pages.homePage import HomePage
from pages.loginPage import LoginPage
from utilities import get_decoded_credentials

@pytest.mark.usefixtures("page")
class TestE2EScenario:
    @pytest.fixture(autouse=True)
    def _init(self, page):
        self.login_page = LoginPage(page)
        self.home_page = HomePage(page)
        username, password = get_decoded_credentials()
        self.login_page.login_to_application(username, password)

    def test_E2EScenario(self, page):
        self.home_page.add_to_cart()
        page.wait_for_timeout(5000)

    def test_E2EScenario2(self, page):
        self.home_page.add_to_cart()
        page.wait_for_timeout(5000)
