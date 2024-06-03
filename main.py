import re
from playwright.sync_api import Playwright, sync_playwright, expect
from Survey import Respondent
from Question import Question, Answer
from Utility import Utility




questions = Utility.get_questions("questions.txt")

# for i in questions:
#     print(i.get_name())
#     print(i.get_answers())


while True:
    with sync_playwright() as playwright:
        r = Respondent("https://forms.gle/TeFsohnJdJBnsy5f8", playwright, questions)
        r.vote()
