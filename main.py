import re
from playwright.sync_api import Playwright, sync_playwright, expect
from Survey import Respondent
from Question import Question


def get_questions(filename : str) -> list:
    questions = list()
    f = open("questions.txt", "r")

    for line in f.readlines():
        wordlist = line.split(":")
        questions.append(Question(wordlist[0]))

        cur = questions[-1]
        answer_list = list()
        for w in range(1, len(wordlist)):

            elem = wordlist[w]

            if elem[-1] == '\n':
                elem = elem[:-1]

            answer_list.append(elem)
        
        cur.set_answers(answer_list)
        # print(cur.get_name())
        # print(cur.get_answers())
    
    f.close()
    return questions


questions = get_questions("questions.txt")

for i in questions:
    print(i.get_name())
    print(i.get_answers())


while True:
    with sync_playwright() as playwright:
        r = Respondent("https://forms.gle/TeFsohnJdJBnsy5f8", playwright, questions)
        r.vote()
