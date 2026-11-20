from .input import sinput
from ..bot.chatbot import Chatbot


class CliInstance:
    def __init__(self):
        self.bot = Chatbot()


    def run(self) -> None:
        print("How can I help you?")

        while True:
            prompt: str = sinput("> ")
            self.bot.reply(prompt)
