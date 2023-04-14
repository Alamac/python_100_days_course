from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


def main():
    question_bank = []
    for item in question_data:
        question_bank.append(Question(item["text"], item["answer"]))
    qb = QuizBrain(question_bank)
    while qb.still_has_question():
        qb.next_question()
    qb.print_result()


if __name__ == '__main__':
    main()
