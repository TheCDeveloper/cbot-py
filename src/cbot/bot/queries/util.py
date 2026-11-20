from .query import AnswerDict, QueryType


class UtilQuery(QueryType):
    @staticmethod
    def add(answers: AnswerDict):
        fn = lambda: exit()

        answers["exit"] = fn
        answers["quit"] = fn
        answers["bye"] = fn
        answers["have a nice day"] = fn
        answers["see you soon"] = fn
        answers["i have to go"] = fn
        answers["that is all"] = fn
