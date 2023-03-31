import argparse
from playwright.sync_api import sync_playwright
import time
import secrets


def screenshot(website: str, headless: bool = True, delay: int = 0, full: bool = False):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=headless)
        page = browser.new_page()
        page.goto(website)
        time.sleep(delay)
        page.screenshot(
            full_page=full,
            timeout=15 * 1000,
            type="png",
            path=f"screenshots/{secrets.token_urlsafe(8)}.png",
        )
        print("Screenshot saved.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--website", "-w", required=True, help="The website to take a screenshot of"
    )
    parser.add_argument(
        "--delay",
        "-d",
        required=False,
        help="How long to wait before taking the screenshot (seconds)",
        type=int,
        default=0,
    )
    parser.add_argument(
        "--headless",
        required=False,
        help="If the process should be headless or not",
        default=True,
        type=bool,
    )
    parser.add_argument(
        "--full_page",
        "-fp",
        required=False,
        help="If the screenshot should be of the full page",
        default=False,
        type=bool,
    )
    ParsedArgs = parser.parse_args()
    screenshot(
        website=ParsedArgs.website,
        headless=ParsedArgs.headless,
        delay=ParsedArgs.delay,
        full=ParsedArgs.full_page,
    )
