from pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME = "#username"
    PASSWORD = "#password"
    LOGIN_BUTTON = "#submit"

    def login(self, username: str, password: str):
        self.fill(self.USERNAME, username)
        self.fill(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)