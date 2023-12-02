class QuizBrain:
    
    def __init__(self,question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        choice = input(f"Q.{self.question_number} {current_question.text}: True or False? ")
        self.check_answer(choice,current_question)
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def increase_score(self):
        self.score += 1
     
    def check_answer(self,choice,current_question):
        if choice.lower() == current_question.answer.lower():
            self.increase_score()
            self.show_score()
        else:
            self.show_score()
        print(f"The correct answer is {current_question.answer}")
               
    def show_score(self):
        print(f"Your score is : {self.score}/{self.question_number}")
        
    def final_score(self):
        print(f"Your Final Score is : {self.score}")
