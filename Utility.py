from Question import Answer 
import random

# survey = "https://forms.gle/TeFsohnJdJBnsy5f8"

class Respondent:
    pass

class Question:

    def __init__(self, name : str, answers : list):
        self._name = name
        self._answers : list = answers
        self.__answer  = None


    def respond(self, respondent : Respondent) -> None:

        choice = self._answers[0]
        for a in self._answers:
            if a.get_odds()[respondent.get_gender()] >= random.randint(1, 100):
                choice = a
    
        respondent.get_page().get_by_label(self._name).locator("div").filter(has_text=choice.get_name()).nth(2).click()

    def get_name(self) -> str:
        return self._name


class NumericResponseQuestion(Question):

    def __init__(self, name : str, answers : list):
        Question.__init__(self, name, answers)

    def respond (self, respondent : Respondent) -> None:

        choice = self._answers[0];
        for a in self._answers:
            if a.get_odds()[respondent.get_gender()] >= random.randint(1, 100):
                choice = a

        respondent.get_page().get_by_label(str(random.randint(2, 4)), exact=True).click()



class MultipleResponseQuestion(Question):

    def __init__(self, name : str, answers : list):
        Question.__init__(self, name, answers)

    def __decide(self, respondent : Respondent) -> Answer:

        choice = self._answers[0];
        for a in self._answers:
            if a.get_odds()[respondent.get_gender()] >= random.randint(1, 100):
                choice = a

        return choice


    def respond (self, respondent : Respondent) -> None:

        lim = random.randint(1, 5)
        cache = set()

        for i in range(0, lim):
            choice = self.__decide(respondent)
            while choice.get_name() in cache:
                choice = self.__decide(respondent)
            cache.update(choice.get_name())
            respondent.get_page().get_by_label(self._name).locator("div").filter(has_text=choice.get_name()).nth(2).click()




class Utility:

    def __init__(self) -> None:
        self.survey = "https://forms.gle/nBvfMxFE8ixA9ouL8"
        self.male_ratio_by_default = 65

    @property
    def male_ratio_by_default(self):
        return self.__male_ratio_by_default
    
    @male_ratio_by_default.getter
    def male_ratio_by_default(self) -> str:
        return self.__male_ratio_by_default
    
    @male_ratio_by_default.setter
    def male_ratio_by_default(self, name : str):
        self.__male_ratio_by_default = name;

    @property
    def survey(self):
        return self.__survey_reference
    
    @survey.getter
    def survey(self) -> str:
        return self.__survey_reference
    
    @survey.setter
    def survey(self, name : str):
        self.__survey_reference = name;


    def get_questions(filename : str = "some.txt") -> list:

        questions = list()
        f = open(filename, "r")

        for line in f.readlines():
            if not line == "\n":
                questions.append(eval(line[:-1]))
        
        return questions
    