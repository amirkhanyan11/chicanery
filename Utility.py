from Question import Question, Answer

male_ratio_by_default = 65
# survey = "https://forms.gle/TeFsohnJdJBnsy5f8"
survey = "https://forms.gle/nBvfMxFE8ixA9ouL8"

class Utility:

    def get_questions(filename : str = "text.txt") -> list:
        questions = list()
        f = open(filename, "r")

        for line in f.readlines():
            wordlist = line.split(":")
            questions.append(Question(wordlist[0]))

            cur = questions[-1]
            answer_list = list()
            for w in range(1, len(wordlist)):

                x = wordlist[w].split(",")

                for i in range(0, len(x)):
                    if x[i][-1] == '\n':
                        x[i] = x[i][:-1]

                ans = Answer(x[0], int(x[-1]))

                answer_list.append(ans)
            
            cur.set_answers(answer_list)
            print(cur.get_name())
        
        f.close()
        return questions