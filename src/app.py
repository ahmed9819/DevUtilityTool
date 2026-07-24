import typer
from src.commands.greet import hello
from src.commands.init import init
from src.commands.organize import organize

app = typer.Typer()

app.command()(hello)
app.command()(init)
app.command()(organize)
