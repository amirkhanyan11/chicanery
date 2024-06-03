from Question import Question, Answer

class Utility:

    def get_questions(filename : str) -> list:
        questions = list()
        f = open("questions.txt", "r")

        for line in f.readlines():
            wordlist = line.split(":")
            questions.append(Question(wordlist[0]))

            cur = questions[-1]
            answer_list = list()
            for w in range(1, len(wordlist) - 1):

                x = wordlist[w].split(",")

                ans = Answer(x[0], int(x[-1]))

                answer_list.append(ans)
            
            cur.set_answers(answer_list)
        
        f.close()
        return questions