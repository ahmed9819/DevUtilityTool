from pathlib import Path
import re

class InvalidProjectNameError(Exception):
    pass

class ProjectAlreadyExistsError(Exception):
    pass


def create_project(project_name: str):

    """
    Create the root project directory after validating the project name.
    """

    
    if not re.match(r"^[a-zA-Z0-9_-]+$", project_name):
        raise InvalidProjectNameError(
            f"Invalid project name '{project_name}'. Only alphanumeric characters, hyphens, and underscores are allowed."
        )

    project_path = Path(project_name)

    if project_path.exists():
        raise ProjectAlreadyExistsError(
            f"Project '{project_name}' already exists."
            )
    
    project_path.mkdir(parents=True)
    return project_path

