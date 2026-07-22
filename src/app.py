import typer
from src.commands.greet import hello
from src.commands.init import init

app = typer.Typer()

app.command()(hello)
app.command()(init)

