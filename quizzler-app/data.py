import requests
from question_model import Question

ENDPOINT = "https://opentdb.com/api.php?amount=10&type=boolean"


class QuestionData:
    def __init__(self, endpoint=ENDPOINT):
        self.endpoint = endpoint
        self.questions = self._get_questions_from_server()

    def _get_questions_from_server(self):
        response = requests.get(self.endpoint)
        response.raise_for_status()
        results = response.json()["results"]
        processed_results = [Question(question=q["question"], answer=q["correct_answer"]) for q in results]
        return processed_results

    def reset_questions(self):
        self.questions = self._get_questions_from_server()

    def get_questions(self):
        return self.questions
