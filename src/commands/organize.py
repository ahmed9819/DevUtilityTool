import typer
from pathlib import Path
from src.services.organizer_service import (
    organize_files,
    FolderNotFoundError,
    InvalidDirectoryError
)

def organize(
        folder: str = typer.Argument(
            ...,
            help="Path to the folder to organize"
        )
):
    try:
        folder_path = Path(folder)
        organize_files(folder_path)
        typer.echo(f"Files in '{folder_path}' organized successfully.")
    except (FolderNotFoundError, InvalidDirectoryError) as e:
        typer.echo(f"Error: {e}")
        raise typer.Exit(code=1)