from .input import sinput
from ..bot.chatbot import Chatbot


class CliInstance:
    def __init__(self):
        self.bot = Chatbot()


    def run(self) -> None:
        self.bot.introduce()

        while True:
            # Color the user input as green
            prompt: str = sinput("\033[90m> \033[32m")

            # Revert formatting
            print("\033[0m", end="")
            self.bot.reply(prompt)
