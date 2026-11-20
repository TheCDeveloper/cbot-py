import re

def parse(prompt: str) -> map[str]:
    # Regex removes punchuations
    return map(lambda e: re.sub("[^a-zA-Z0-9]*", "", e), prompt.strip().split())
