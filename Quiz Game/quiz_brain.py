class QuestionBrain:
    def __init__(self, question):
        self.question_number = 0
        self.question_list = question
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Retrieve the item at the current position and displays the question"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q. {self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(current_question.answer, answer)

    def check_answer(self, correct_answer, answer_given):
        if correct_answer.lower() == answer_given.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You are wrong.")
        print(f"The correct answer was : {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
