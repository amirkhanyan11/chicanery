from Question import Answer 
import random

# survey = "https://forms.gle/TeFsohnJdJBnsy5f8"

class Respondent:
    pass

class Question:

    def __init__(self, name : str, answers : list):
        self.__name = name
        self._answers : list = answers
        self.__answer  = None


    def respond(self, respondent : Respondent) -> None:

        choice = self._answers[0]
        for a in self._answers:
            # if a.get_odds()["Male"] >= random.randint(1, 100):
            if a.get_odds()[respondent.get_gender()] >= random.randint(1, 100):
                choice = a
    
        respondent.get_page().get_by_label(self.__name).locator("div").filter(has_text=choice.get_name()).nth(2).click()

    def get_name(self) -> str:
        return self.__name

    



class NumericResponseQuestion(Question):

    def __init__(self, name : str, answers : list):
        Question.__init__(self, name, answers)

    def respond (self, respondent : Respondent) -> None:

        choice = self._answers[0];
        for a in self._answers:
            # if a.get_odds()["Male"] >= random.randint(1, 100):
            if a.get_odds()[respondent.get_gender()] >= random.randint(1, 100):
                choice = a

        # return choice.get_name()

        respondent.get_page().get_by_label(str(random.randint(2, 4)), exact=True).click()



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
    
        # for q in questions:
        #     if type(q) is NumericResponseQuestion:
        #         print(super(NumericResponseQuestion, q).get_name() + " --> " + q.respond(None))
        #     else:
        #         print(q.get_name() + " --> " + q.respond(None))

