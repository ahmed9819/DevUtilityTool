from pathlib import Path
import re

class InvalidProjectNameError(Exception):
    pass

class ProjectAlreadyExistsError(Exception):
    pass

def create_project(project_name: str):
    
    if not re.match(r"^[a-zA-Z0-9_-]+$", project_name):
        raise InvalidProjectNameError(
            f"Invalid project name '{project_name}'. Only alphanumeric characters, hyphens, and underscores are allowed."
        )

    project_path = Path(project_name)

    if project_path.exists():
        raise ProjectAlreadyExistsError(
            f"Project '{project_name}' already exists."
            )
    
    project_path.mkdir()

    folders = [
        "src",
        "tests",
        "docs"
    ]

    for folder in folders:
        folder_path = project_path / folder
        folder_path.mkdir()

    
    files = [
        "README.md",
        ".gitignore",
        "requirements.txt",
        "main.py"
    ]

    for file in files:
        file_path = project_path / file
        file_path.touch()

    return project_path

