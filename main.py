import re
from playwright.sync_api import Playwright, sync_playwright, expect
from Utility import *
from Survey import Respondent
from Question import Answer


questions : list = Utility.get_questions()

while True:
    with sync_playwright() as playwright:
        r = Respondent(playwright, questions, "Female")
        r.vote()
