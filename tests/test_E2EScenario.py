# test_E2EScenario.py
import pytest
from pages.homePage import HomePage
from utilities.api_client import get_request

class TestE2EScenario:
    @pytest.fixture(autouse=True)
    def _init(self, request):
        # Only initialize home_page if 'page' fixture is used
        if 'page' in request.fixturenames:
            self.home_page = HomePage(request.getfixturevalue('page'))

    def test_E2EScenario(self, page):
        self.home_page.add_to_cart()
        page.wait_for_timeout(2000)
        page.screenshot(path="reports/screenshots/test_E2EScenario.png")
        assert True

    @pytest.mark.smoketest
    def test_E2EScenario2(self, page):
        self.home_page.remove_from_cart()
        page.wait_for_timeout(2000)
        page.screenshot(path="reports/screenshots/test_E2EScenario2.png")
        assert True


    def test_E2EScenario3(self):
        # API test only, do not trigger any UI/browser actions
        response = get_request("https://jsonplaceholder.typicode.com/posts/1")
        print("API Response:", response.json())
        assert response.status_code == 200
        assert response.json()["id"] == 1
