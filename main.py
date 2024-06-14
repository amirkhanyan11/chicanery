import re
from playwright.sync_api import Playwright, sync_playwright, expect
from Utility import *
from Survey import Respondent
from Question import Answer


questions : list = Utility.get_questions()

for i in range(1, 3, 1):
    with sync_playwright() as playwright:
        r = Respondent(playwright, questions, "Female")
        r.vote()
