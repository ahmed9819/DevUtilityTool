import typer
from src.services.project_initializer import initialize_project
from src.services.project_creator import (
    InvalidProjectNameError,
    ProjectAlreadyExistsError
)
from src.services.git_service import GitNotInstalledError
from src.services.venv_service import VirtualEnvironmentCreationError
from src.services.template_service import TemplateNotFoundError


def init(
    name: str = typer.Argument(
        ...,
        help="Name of the project to create"
    ),
    git: bool = typer.Option(
        False,
        "--git",
        help="Initialize a Git Repository."
    ),
    venv: bool =typer.Option(
        False,
        "--venv",
        help="Create a Python virtual environment."
    ),
    template: str = typer.Option(
        "Default",
        "--template",
        help="project template to use."
    )

):
    try:
        project_path = initialize_project(name, initialize_git=git, initialize_venv=venv, template_name=template)

        typer.echo(
            f"Project '{project_path}' created Successfully."
        )
        if git:
            typer.echo(
                f"git initialized in project '{project_path}'"
            )
        if venv:
            typer.echo(
                f"Python virtual environment created in '{project_path}'"
            )

    except (InvalidProjectNameError, ProjectAlreadyExistsError, GitNotInstalledError, VirtualEnvironmentCreationError, TemplateNotFoundError) as e:
        typer.echo(f"{e}")
        raise typer.Exit()
    