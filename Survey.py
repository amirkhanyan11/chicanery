import re
import time
import random
from Question import Answer
from playwright.sync_api import Playwright, sync_playwright, expect

class Respondent:
    pass

class Question:

    def __init__(self, name : str, answers : list):
        self.__name = name
        self.__answers : list = answers
        self.__answer  = None


    def respond(self, respondent : Respondent) -> None:

        choice = self.__answers[0]
        for a in self.__answers:
            if a.get_odds()["Male"] >= random.randint(1, 100):
            # if a.get_odds()[respondent.get_gender()] >= random.randint(1, 100):
                choice = a

        return choice.get_name()
        # print (choice.get_name())
        # print (choice.get_odds()[self.__gender])
    
        # respondent.get_page().get_by_label(self.__name).locator("div").filter(has_text=choice.get_name()).nth(2).click()

    def get_name(self) -> str:
        return self.__name


class NumericResponseQuestion(Question):

    def __init__(self, name : str, answers : list = dict()):
        Question.__init__(self, name, answers)

    def respond (self, respondent : Respondent) -> None:
        choice = None
        for a in self.__answers:
            if a.get_odds()[respondent.get_gender()] >= random.randint(1, 100):
                choice = a

        respondent.get_page().get_by_label(str(random.randint(2, 4)), exact=True).click()


class Respondent:

    def __init__(self, playwright: Playwright, qst : list, gender : str = "Unspecified"):
        self.__browser = playwright.chromium.launch(headless=False)
        self.__context = self.__browser.new_context()
        self.__page = self.__context.new_page()
        self.__questions = qst
        self.__src = Utility.survey
        self.__gender = "Male" if random.randint(1, 100) >= Utility.male_ratio_by_default else "Female" if gender == "Unspecified" else gender


    def respond(self) -> None:

        answers = self.__generate_answers()

        for question in self.__questions:
            self.__respond_to(question)
            time.sleep(1) 

    def __respond_to(self, strategy : Question) -> None:
        self.__page.wait_for_load_state("networkidle")
        strategy.respond(self)

    def send(self) -> None:
        self.__page.get_by_role("button", name="Ուղարկել").click()

    def vote(self) -> None:

        self.__page.goto(self.__src)

        self.respond()
        self.send()

        # ---------------------

        self.__context.close()
        self.__browser.close()

    def get_gender(self):
        return self.__gender

    def get_page(self):
        return self.__page

