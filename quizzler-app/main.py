from question_model import Question
from data import QuestionData
from quiz_brain import QuizBrain
from ui import QuizInterface


def main():
    qd = QuestionData()
    questions = qd.get_questions()
    quiz = QuizBrain(questions)
    quiz_ui = QuizInterface(quiz)


if __name__ == "__main__":
    main()
