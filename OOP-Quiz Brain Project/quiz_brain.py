class QuizBrain:

    def __init__(self,q_list):
        self.q_num=0
        self.q_list=q_list
        self.score=0

    def still_has_question(self):
        return self.q_num < len(self.q_list)


    def next_question(self):
        current_question=self.q_list[self.q_num]
        self.q_num+=1
        user_answer=input(f"Q_no:{self.q_num} {current_question.text} (True/False) : ").capitalize()
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self,u_answer,r_answer):
        if u_answer==r_answer:
            self.score+=1
            print("you got it right!")


        else:
            print("that's wrong")
        print(f"the correct answer is {r_answer}")
        print(f"your current score is {self.score}/{self.q_num}\n\n")
