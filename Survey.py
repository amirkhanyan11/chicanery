import re
import time
import random
from playwright.sync_api import Playwright, sync_playwright, expect
from Question import Question


class Respondent:

    def __init__(self, playwright: Playwright, qst : list):
        self.__browser = playwright.chromium.launch(headless=False)
        self.__context = self.__browser.new_context()
        self.__page = self.__context.new_page()
        self.__questions = qst


    def respond(self) -> None:
        
        answers = self.__generate_answers()

        for question in self.__questions:
            self.__respond_to(question, answers)
            time.sleep(1)


    def __respond_to(self, question : str, answers : dict) -> None:
        
        self.__page.wait_for_load_state("networkidle")
        self.__page.get_by_label(question.get_name()).locator("div").filter(has_text=answers[question.get_name()]).nth(2).click()     # self.__page.get_by_label(self.__questions[q][answers[i]]).click()
            

    def __generate_answers(self) -> list:

        answers = dict()
        for q in self.__questions:
            answers[q.get_name()] = q.get_answers()[random.randint(1, 100) % len(q.get_answers())]
        
        for a in answers:
            print(a)
            print(answers[a])

        return answers


    def send(self) -> None:
        self.__page.get_by_role("button", name="Ուղարկել").click()


    def vote(self) -> None:

        self.__page.goto("https://forms.gle/TeFsohnJdJBnsy5f8")

        self.respond()
        self.send()

        # ---------------------

        self.__context.close()
        self.__browser.close()

