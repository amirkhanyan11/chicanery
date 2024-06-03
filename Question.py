

class Question:

    def __init__(self, name : str, answers : list = list(), gender_p : int = 50):
        self.__name = name
        self.__answers = answers
        self.__odds = {

            "Male" : gender_p,
            "Female" : 100 - gender_p
        }

    def get_answers(self) -> list:
        return self.__answers
    
    def get_name(self) -> str:
        return self.__name

    def get_odds(self) -> dict:
        return self.__odds
    
    def set_answers(self, answers : list) -> None:

        self.__answers = answers

    def set_odds(self, odds : dict) -> None:
        self.__odds = odds
            

