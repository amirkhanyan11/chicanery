import re
import time
import random
from playwright.sync_api import Playwright, sync_playwright, expect



class Respondent:

    def __init__(self, playwright: Playwright, qst : dict):
        self.__browser = playwright.chromium.launch(headless=False)
        self.__context = self.__browser.new_context()
        self.__page = self.__context.new_page()
        self.__questions = qst


    def respond(self) -> None:
        
        answers = []
        for q in self.__questions:
            answers.append(random.randint(1, 100) % len(self.__questions[q])) 
        

        i = 0;
        for q in self.__questions:
            self.__page.wait_for_load_state("networkidle")
            self.__page.get_by_label(q).locator("div").filter(has_text=self.__questions[q][answers[i]]).nth(2).click()     # self.__page.get_by_label(self.__questions[q][answers[i]]).click()
            time.sleep(1)
            i += 1


    def send(self) -> None:
        self.__page.get_by_role("button", name="Ուղարկել").click()


    def vote(self) -> None:

        self.__page.goto("https://forms.gle/TeFsohnJdJBnsy5f8")

        self.respond()
        self.send()

        # ---------------------

        self.__context.close()
        self.__browser.close()

