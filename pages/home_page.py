from pages.base_page import BasePage


class HomePage(BasePage):

    DASHBOARD_TITLE = "text=Logged In Successfully"

    def verify_dashboard(self):

        self.verify_visible(self.DASHBOARD_TITLE)
