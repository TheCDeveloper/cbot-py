from .query import AnswerDict, QueryType


class GkQuery(QueryType):
    @staticmethod
    def add(answers: AnswerDict):
        answers["what is color of sky"] = "The color of the sky is blue."

        answers["what is capital of india"] = "The capital of India is Delhi."

        answers["who are you"] = "I am a rule-based chatbot, written in Python. I don't have real" \
            " intelligence, nor an LLM does."
