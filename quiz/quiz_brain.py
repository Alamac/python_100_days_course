class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        q = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f'Q.{self.question_number + 1}: {q.text} (True/False)?: ')
        self.check_answer(ans, q.answer)

    def check_answer(self, user_answer, q_answer):
        if user_answer.lower() == q_answer.lower():
            print('You got it right!')
            self.score += 1
        else:
            print('You got it wrong')
        print(f'The correct answer is {q_answer}')
        print(f'Your current score is: {self.score}/{self.question_number}')
        print('\n')

    def print_result(self):
        print('You\'ve completed the quiz!')
        print(f'Your score is {self.score}/{self.question_number}')



