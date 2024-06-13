import random

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

