"""Module for model evalutation."""

from pathlib import Path
from typing import Annotated

import typer


def main(model_file: Annotated[Path, typer.Option(...)]) -> None:
    """Main function, print hello message."""
    print("Reading message from training:")
    print(model_file.read_text())


if __name__ == "__main__":
    typer.run(main)
