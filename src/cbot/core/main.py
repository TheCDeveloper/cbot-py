from .cli import CliInstance


def main() -> None:
    cli = CliInstance()
    cli.run()
