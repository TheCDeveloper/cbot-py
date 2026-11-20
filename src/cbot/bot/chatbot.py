from .parser import expand_abbreviations, parse, filter_filler_words
from .queries.query import AnswerDict

from .queries.gk import GkQuery
from .queries.time import TimeQuery
from .queries.util import UtilQuery


class Chatbot:
    def __init__(self):
        self.try_asking: list[str] = [
            "What is the color of the sky?",
            "What is the capital of India?",
            "Who are you?",
            "What is the current date/time/weekday?",
            "Bye \033[3;90m(To end the conversation)\033[0m"
        ]

        self.answers: AnswerDict = {}


        # Add queries
        GkQuery.add(self.answers)
        TimeQuery.add(self.answers)
        UtilQuery.add(self.answers)


    def introduce(self):
        print("Rule-based chatbot, made in \033[1;34mPython\033[0m\n" \
            "\033[3;90m(Because I didn't had the time to write a C/Rust based version)\033[0m\n")

        print("\033[1mTry asking\033[0m")
        print("\n".join([f"- {query}" for query in self.try_asking]), end="\n\n")


    def fast_reply(self, prompt: str):
        reply = self.answers.get(prompt)

        if not reply:
            print("I don't know how to process your query...")
            return


        if isinstance(reply, str):
            print(reply)
        else:
            print(reply())


    def reply(self, prompt: str):
        words = list(parse(prompt))
        filter_filler_words(words)
        expand_abbreviations(words)
        sentence = " ".join(words)


        print("\033[3m", end="") # Italics
        self.fast_reply(sentence)
        print("\033[0m") # Remove formatting and newline
