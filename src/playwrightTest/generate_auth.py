from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        # MUST be headed so you can see the screen and solve puzzles if needed
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.coursera.org/")
        
        print("1. A browser window has opened.")
        print("2. Please log into Coursera manually (solve any CAPTCHAs or 2FA).")
        print("3. Once you are successfully on your dashboard, return to this terminal.")
        
        # This pauses the Python script until you type Enter in the terminal
        input("Press Enter in this terminal ONLY AFTER you are fully logged in...")

        # Save all cookies and session tokens to a file
        context.storage_state(path="auth.json")
        print("Success! Authentication state saved to auth.json")
        
        browser.close()

if __name__ == "__main__":
    run()