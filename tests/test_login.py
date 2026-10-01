


from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_valid_login(page, config):

    login_page = LoginPage(page)

    page.goto(config["base_url"])

    login_page.login(
        config["credentials"]["username"],
        config["credentials"]["password"]
    )
    homepage= HomePage(page)
    homepage.verify_dashboard()
    