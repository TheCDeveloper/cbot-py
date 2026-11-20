import re


def parse(prompt: str) -> map[str]:
    # Regex removes punchuations
    return map(lambda e: re.sub("[^a-zA-Z0-9]*", "", e), prompt.lower().strip().split())


def filter_filler_words(words: list[str]):
    # TODO: Add more filters for words not contributing meaning to the sentence
    for word in ("a", "an", "the"):
        while True:
            try:
                words.remove(word)
            except ValueError:
                break


# TODO: Add common abbreviations, must be non ambigious in the language
__abbreviations = {
    "u": "you",
    "r": "are",
    "idk": "i do not know",
    "ye": "yes",

    "dont": "do not",
    "cant": "can not",
    "thats": "that is",
    "weekday": "week day",
}


def expand_abbreviations(words: list[str]):
    for i, word in enumerate(words):
        if word in __abbreviations:
            full_form = __abbreviations[word].split()
            words[i] = full_form[0]

            for other_word in full_form[-1:0:-1]: # Reversed of [1:]
                words.insert(i + 1, other_word)
