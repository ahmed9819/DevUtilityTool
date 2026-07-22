import typer
from src.services.project_initializer import initialize_project
from src.services.project_creator import (
    InvalidProjectNameError,
    ProjectAlreadyExistsError
)
from src.services.git_service import GitNotInstalledError
def init(name: str, git: bool = False):
    try:
        project_path = initialize_project(name, initialize_git=git)

        typer.echo(
            f"Project '{project_path}' created Successfully."
        )

    except (InvalidProjectNameError, ProjectAlreadyExistsError, GitNotInstalledError) as e:
        typer.echo(f"{e}")
        raise typer.Exit()
    