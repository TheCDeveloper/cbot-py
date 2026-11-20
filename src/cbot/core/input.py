def sinput(prompt: object) -> str:
    try:
        return input(prompt)
    except KeyboardInterrupt, EOFError:
        exit()
