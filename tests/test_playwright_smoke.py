def test_playwright_fixture(page):
    page.goto("https://example.com")
    assert "Example Domain" in page.title()
