from Survey import Question, NumericResponseQuestion
from Question import Answer 

male_ratio_by_default = 65
# survey = "https://forms.gle/TeFsohnJdJBnsy5f8"
survey = "https://forms.gle/nBvfMxFE8ixA9ouL8"

class Utility:

    def get_questions(filename : str = "some.txt") -> list:
        questions = list()
        f = open(filename, "r")

        for line in f.readlines():
            if not line == "\n":
                questions.append(eval(line[:-1]))
    
        for q in questions:
            print(q.get_name() + " --> " + q.respond(None))
