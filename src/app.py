import typer

app = typer.Typer()

from src.commands.init import init
from src.commands.greet import hello
from src.commands.organize import organize
from src.commands.password import password
from src.commands.hash import hash

app.command()(hello)
app.command()(init)
app.command()(organize)
app.command()(password)
app.command()(hash)