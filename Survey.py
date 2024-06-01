import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect



class Respondent:

    def __init__(self, playwright: Playwright):
        self.__browser = playwright.chromium.launch(headless=False)
        self.__context = self.__browser.new_context()
        self.__page = self.__context.new_page()


    def run(self) -> None:

        self.__page.goto("https://docs.google.com/forms/d/e/1FAIpQLScfBKueK5ZNaoLxVzqPWlXsVyGyHwUb5CL9j7sRO0nQEQq8ZQ/viewform?usp=send_form")
        self.__page.goto("https://docs.google.com/forms/d/e/1FAIpQLScfBKueK5ZNaoLxVzqPWlXsVyGyHwUb5CL9j7sRO0nQEQq8ZQ/viewform")
        self.__page.get_by_label("Maybe").click()
        self.__page.get_by_role("button", name="Ուղարկել").click()

        # ---------------------

        self.__context.close()
        self.__browser.close()

