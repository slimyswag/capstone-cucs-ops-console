import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth

load_dotenv()

def run_admin_automation():
    email = os.getenv("COURSERA_EMAIL")
    password = os.getenv("COURSERA_PASSWORD")

    if not email or not password:
        raise ValueError("Missing credentials! Check your .env file.")

    print("Initializing Coursera automation...")

    with Stealth().use_sync(sync_playwright()) as p:
        
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        print("1. Navigating to Coursera")
        page.goto("https://www.coursera.org/")

        print("2. Logging in")
        page.locator('a:has-text("Log in"), button:has-text("Log in")').first.click()
        page.locator('input[type="email"]').fill(email)
        page.get_by_role("button", name="Continue", exact=True).click()
        password_field = page.locator('input[type="password"]')
        password_field.fill(password)
        password_field.press("Enter")

        print("3. Navigate to admin dashboard")
        profile_btn = page.locator('[data-e2e="header-profile"]')
        profile_btn.wait_for(state="visible", timeout=15000)
        page.wait_for_timeout(3000)
        profile_btn.hover()
        page.wait_for_timeout(500)
        profile_btn.click()
        page.get_by_text("Educator", exact=False).first.click()
        page.wait_for_load_state("domcontentloaded") 
        print(f"Successfully arrived at: {page.url}")
        page.wait_for_timeout(2000)
        page.screenshot(path="screenshot.png")
        
        browser.close()

if __name__ == "__main__":
    run_admin_automation()