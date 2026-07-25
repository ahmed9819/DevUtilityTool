from pathlib import Path

import typer

from src.services.hash_service import (
    hash_text,
    hash_file,
    InvalidHashAlgorithmError,
    HashFileNotFoundError,
    InvalidFileError,
)


def hash(
    input_value: str = typer.Argument(
        ...,
        help="Text or file path to hash.",
    ),
    algorithm: str = typer.Option(
        "sha256",
        "--algorithm",
        "-a",
        help="Hash algorithm (md5, sha1, sha256).",
    ),
):
    """
    Generate the hash of text or a file.
    """

    try:
        path = Path(input_value)

        if path.exists():
            digest = hash_file(
                file_path=path,
                algorithm=algorithm,
            )
        else:
            digest = hash_text(
                text=input_value,
                algorithm=algorithm,
            )

        typer.echo(f"{algorithm.upper()}: {digest}")

    except (
        InvalidHashAlgorithmError,
        HashFileNotFoundError,
        InvalidFileError,
    ) as e:
        typer.secho(str(e), fg=typer.colors.RED)
        raise typer.Exit(code=1)