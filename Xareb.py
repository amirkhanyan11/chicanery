import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


class Xareb:

    def __init__(self, playwright: Playwright):
        self.__browser = playwright.chromium.launch(headless=False)
        self.__context = self.__browser.new_context()
        self.__page = self.__context.new_page()


    def run(self) -> None:
        passwd : str = input("Enter the passwrd : ")
        self.__page.goto("https://github.com/")
        self.__page.get_by_role("link", name="Sign in").click()
        self.__page.get_by_label("Username or email address").click()
        self.__page.get_by_label("Username or email address").fill("artyom.amirkhanyan11@gmail.com")
        self.__page.get_by_label("Password").click()
        self.__page.get_by_label("Password").fill(passwd)
        self.__page.get_by_label("Password").press("Enter")
        self.__page.get_by_label("Account", exact=True).get_by_role("link", name="amirkhanyan11/BST").click()
        self.__page.get_by_role("link", name="_traversal.hpp, (File)").click()

        # ---------------------

        time.sleep(120)

        self.__context.close()
        self.__browser.close()