import requests

ENDPOINT = "https://opentdb.com/api.php?amount=10&type=boolean"


class QuestionData:
    def __init__(self, endpoint=ENDPOINT):
        self.endpoint = endpoint
        self.questions = self._get_questions_from_server()

    def _get_questions_from_server(self):
        response = requests.get(self.endpoint)
        response.raise_for_status()
        return response.json()["results"]

    def reset_questions(self):
        self.questions = self._get_questions_from_server()

    def get_questions(self):
        return self.questions
