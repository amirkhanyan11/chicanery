import re
from playwright.sync_api import Playwright, sync_playwright, expect
from Xareb import Xareb


with sync_playwright() as playwright:
    a = Xareb(playwright)
    a.run()
