import typer


app = typer.Typer()

@app.command()
def hello(name: str, age: int):
    typer.echo(f"Hello, {name}! You are {age} years old.")