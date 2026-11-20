from .input import sinput
from ..bot.chatbot import Chatbot


class CliInstance:
    def __init__(self):
        self.bot = Chatbot()


    def run(self) -> None:
        self.bot.introduce()

        while True:
            prompt: str = sinput("\033[90m> \033[32m")
            print("\033[0m", end="")
            self.bot.reply(prompt)
