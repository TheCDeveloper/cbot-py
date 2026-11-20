from .parser import parse


class Chatbot:
    def __init__(self):
        self.memory: list[str] = []


    def reply(self, prompt: str):
        sentence = list(parse(prompt))
        words = set(sentence)

        # TODO: make it do stuff
        if "remember" in words or "this" in words:
            print("Remembering")
