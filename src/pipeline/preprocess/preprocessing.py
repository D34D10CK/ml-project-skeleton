"""Module for data preprocessing."""

from pathlib import Path
from typing import Annotated

import typer


def main(output_file: Annotated[Path, typer.Option(...)]) -> None:
    """Main function, print hello message."""
    output_file.parent.mkdir(exist_ok=True, parents=True)
    output_file.write_text("Hello from preprocessing!")


if __name__ == "__main__":
    typer.run(main)
