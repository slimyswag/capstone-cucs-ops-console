from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        context = browser.new_context(storage_state="auth.json")
        page = context.new_page()

        print("Navigating directly to Coursera...")
        page.goto("https://www.coursera.org/")

        print("Opening profile menu...")
        profile_btn = page.locator('[data-e2e="header-profile"]')
        
        profile_btn.wait_for(state="visible")
        profile_btn.click()

        # --- NEW STEPS ---
        print("Clicking Educator admin...")
        # Playwright automatically waits for the dropdown animation to finish
        page.locator('text="Educator Admin"').click()

        print("Waiting for admin dashboard to load...")
        # domcontentloaded waits for the base HTML to load (less strict than networkidle)
        page.wait_for_load_state("domcontentloaded") 
        print(f"Successfully arrived at: {page.url}")
        page.wait_for_timeout(2000)
        page.screenshot(path="screenshot.png")
        # -----------------

        browser.close()

if __name__ == "__main__":
    run()