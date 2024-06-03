
class Answer:   
    def __init__(self, name : str, gender_p : int = 50):
        self.__name = name
        self.__odds = {

            "Male" : gender_p,
            "Female" : 100 - gender_p
        }

    def get_odds(self) -> dict:
        return self.__odds
    
    def get_name(self) -> str:
        return self.__name

class Question:

    def __init__(self, name : str, answers : list = list()):
        self.__name = name
        self.__answers = answers
        self.is_mult = False

    def get_answers(self) -> list:
        return self.__answers
    
    def get_name(self) -> str:
        return self.__name
    
    def set_answers(self, answers : list) -> None:
        self.__answers = answers

