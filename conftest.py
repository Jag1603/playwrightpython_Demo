import os
import pytest
import yaml
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def config():
    environment = os.getenv("ENV", "qa")
    config_file = f"config/{environment}.yaml"

    with open(config_file, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            yield page
        finally:
            browser.close()