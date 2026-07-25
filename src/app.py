import typer

from src.commands.greet import hello
from src.commands.init import init
from src.commands.organize import organize
from src.commands.password import password
from src.commands.hash import hash

app = typer.Typer()

app.command()(hello)
app.command()(init)
app.command()(organize)
app.command()(password)
app.command()(hash)
