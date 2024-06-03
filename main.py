import re
from playwright.sync_api import Playwright, sync_playwright, expect
from Xareb import Xareb
from Survey import Respondent
 
questions = {
    "are u gay?" : ("yes", "no", "Maybe"),
    # "are you sure?" : ("yesssssss", "sssssssno", "issssssdk")
    "are you sure?" : ("yes", "no", "idk"),
    "there's no doubt in your mind?" : ("meh", "i would prefer not to answer")
}


for i in range (1, 5, 1):
    with sync_playwright() as playwright:
        r = Respondent(playwright, questions)
        r.run()

# with sync_playwright() as playwright:
#     a = Xareb(playwright)
#     a.run()
