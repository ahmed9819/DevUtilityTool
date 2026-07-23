import typer


def hello(name: str):
    typer.echo(f"Hello, Mr. {name}!")