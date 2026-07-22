import typer
from src.services.project_creator import create_project, InvalidProjectNameError, ProjectAlreadyExistsError

def init(name: str):
    try:
        project_path = create_project(name)

        typer.echo(
            f"Project '{project_path}' created Successfully."
        )

    except (InvalidProjectNameError, ProjectAlreadyExistsError) as e:
        typer.echo(f"{e}")
        raise typer.Exit()
    