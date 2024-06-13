import re
from playwright.sync_api import Playwright, sync_playwright, expect
from Survey import Question, Respondent
from Question import  Answer
from Utility import Utility


questions = Utility.get_questions()

# for i in range(1, 3, 1):
#     with sync_playwright() as playwright:
#         r = Respondent(playwright, questions)
#         r.vote()
