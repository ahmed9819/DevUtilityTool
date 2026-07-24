import typer

from src.services.password_service import (
    generate_password,
    InvalidPasswordLengthError,
    EmptyCharacterPoolError
)

def password(
        length: int = typer.Option(
            12,
            "--length",
            "-l",
            help="Length of the password."
        ),
        upper_case: bool = typer.Option(
            True,
            "--uppercase/--no-uppercase",
            help="Include uppercae letters."
        ),
        lowercase: bool = typer.Option(
        True,
        "--lowercase/--no-lowercase",
        help="Include lowercase letters."
        ),
        digits: bool = typer.Option(
            True,
            "--digits/--no-digits",
            help="Include digits."
        ),
        symbols: bool = typer.Option(
            True,
            "--symbols/--no-symbols",
            help="Include symbols."
        )
):

    try: 
        generated_password = generate_password(
            length=length,
            use_uppercase=upper_case,
            use_lowercase=lowercase,
            use_digits=digits,
            use_symbols=symbols
        )
        typer.echo(generated_password)

    except (
        InvalidPasswordLengthError,
        EmptyCharacterPoolError
    ) as e:
        typer.echo(e)
        raise typer.Exit(code=1)



