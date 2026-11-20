from typing import Callable

type AnswerDict = dict[str, str | Callable[[], str]]


class QueryType:
    @staticmethod
    def add(answers: AnswerDict) -> None:
        raise NotImplemented
