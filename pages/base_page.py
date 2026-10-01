from playwright.sync_api import Page, expect


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def click(self, locator: str):
        self.page.locator(locator).click()

    def fill(self, locator: str, value: str):
        self.page.locator(locator).fill(value)

    def get_text(self, locator: str) -> str:
        return self.page.locator(locator).inner_text()

    def verify_visible(self, locator: str):
        expect(self.page.locator(locator)).to_be_visible(timeout=30000)

    def navigate(self, url: str):
        self.page.goto(url)

    def screenshot(self, name: str):
        self.page.screenshot(
            path=f"screenshots/{name}.png",
            full_page=True
        )