import re
from playwright.sync_api import Playwright, sync_playwright, expect
from Xareb import Xareb
from Survey import Respondent



for i in range (1, 5, 1):
    with sync_playwright() as playwright:
        r = Respondent(playwright)
        r.run()

# with sync_playwright() as playwright:
#     a = Xareb(playwright)
#     a.run()
