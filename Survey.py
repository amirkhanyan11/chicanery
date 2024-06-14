import re
import time
import random
from Question import Answer
from playwright.sync_api import Playwright, sync_playwright, expect
from Utility import Utility, Question, NumericResponseQuestion


class Respondent:

    def __init__(self, playwright: Playwright, qlist: list, gender: str = "Unspecified"):
        self.__m_utility = Utility()
        self.__browser   = playwright.chromium.launch(headless=False)
        self.__context   = self.__browser.new_context()
        self.__page      = self.__context.new_page()
        self.__questions = qlist
        self.__gender    = "Male" if random.randint(1, 100) >= self.__m_utility.male_ratio_by_default else "Female" if gender == "Unspecified" else gender
        

    def respond(self) -> None:

        for question in self.__questions:
            self.__respond_to(question)
            # time.sleep(1)

    def __respond_to(self, strategy: Question) -> None:
        self.__page.wait_for_load_state("networkidle")
        strategy.respond(self)

    def send(self) -> None:
        self.__page.wait_for_load_state("networkidle")
        self.__page.get_by_role("button", name="Ուղարկել").click()

    def vote(self) -> None:

        self.__page.goto(self.__m_utility.survey)

        self.respond()
        # time.sleep(100)
        self.send() 

        self.__context.close()
        self.__browser.close()

    def get_gender(self):
        return self.__gender

    def get_page(self):
        return self.__page
