import re
from playwright.sync_api import Playwright, sync_playwright, expect
from Survey import Respondent
from Question import Question, Answer
from Utility import Utility


questions = Utility.get_questions("questions.txt")

while True:
    with sync_playwright() as playwright:
        r = Respondent(playwright, questions)
        r.vote()
