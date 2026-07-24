from pathlib import Path
import shutil

from src.config.file_type import FILE_TYPES


class FolderNotFoundError(Exception):
    pass


class InvalidDirectoryError(Exception):
    pass


def organize_files(folder_path: Path):

    # Validation
    if not folder_path.exists():
        raise FolderNotFoundError(
            f"Folder '{folder_path}' does not exist."
        )

    if not folder_path.is_dir():
        raise InvalidDirectoryError(
            f"'{folder_path}' is not a directory."
        )

    # Organize files
    for item in folder_path.iterdir():

        # Skip directories
        if not item.is_file():
            continue

        # Get extension
        extension = item.suffix.lower()

        # Find category
        category = FILE_TYPES.get(extension)

        # Skip unsupported file types
        if category is None:
            continue

        # Create destination folder
        destination = folder_path / category
        destination.mkdir(parents=True, exist_ok=True)

        # Destination file path
        destination_file = destination / item.name

        # Move file
        shutil.move(item, destination_file)