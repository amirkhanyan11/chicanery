import re
import time
import random
from playwright.sync_api import Playwright, sync_playwright, expect
from Question import Question

survey = "https://forms.gle/TeFsohnJdJBnsy5f8"

class Respondent:

    def __init__(self, playwright: Playwright, qst : list, gender : str = "Unspecified"):
        self.__browser = playwright.chromium.launch(headless=False)
        self.__context = self.__browser.new_context()
        self.__page = self.__context.new_page()
        self.__questions = qst
        self.__src = survey
        g_arr = ["Male", "Female"]
        self.__gender = g_arr[0 if random.randint(1, 101) >= 65 else 1] if gender == "Unspecified" else gender 


    def respond(self) -> None:
        
        answers = self.__generate_answers()

        for question in self.__questions:
            self.__respond_to(question, answers)
            # time.sleep(1)


    def __respond_to(self, question : str, answers : dict) -> None:
        
        self.__page.wait_for_load_state("networkidle")
        self.__page.get_by_label(question.get_name()).locator("div").filter(has_text=answers[question.get_name()]).nth(2).click()     # self.__page.get_by_label(self.__questions[q][answers[i]]).click()

    def __decide(self, question : Question, answers : dict) -> str:
        
        ansz = question.get_answers();
        
        choice = ansz[0]
        for a in ansz:
            if a.get_odds()[self.__gender] >= random.randint(1, 101):
                choice = a
                break
        # print (choice.get_name())
        # print (choice.get_odds()[self.__gender])
        return choice.get_name()
        

    def __generate_answers(self) -> list:

        answers = dict()
        for q in self.__questions:
            answers[q.get_name()] = self.__decide(q, answers)          #q.get_answers()[random.randint(1, 100) % len(q.get_answers())].get_name()

        return answers


    def send(self) -> None:
        self.__page.get_by_role("button", name="Ուղարկել").click()


    def vote(self) -> None:

        self.__page.goto(self.__src)

        self.respond()
        self.send()

        # ---------------------

        self.__context.close()
        self.__browser.close()

