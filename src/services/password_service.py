import secrets
import string


class InvalidPasswordLengthError(Exception):
    """Raised when the password length is invalid."""
    pass


class EmptyCharacterPoolError(Exception):
    """Raised when no character set is selected."""
    pass


def generate_password(
    length: int = 12,
    use_uppercase: bool = True,
    use_lowercase: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
) -> str:
    """
    Generate a cryptographically secure password.

    Args:
        length: Desired password length.
        use_uppercase: Include uppercase letters.
        use_lowercase: Include lowercase letters.
        use_digits: Include digits.
        use_symbols: Include symbols.

    Returns:
        A secure randomly generated password.

    Raises:
        EmptyCharacterPoolError:
            If no character set is enabled.

        InvalidPasswordLengthError:
            If the requested password length is too short.
    """

    character_pool = ""
    password = []

    if use_lowercase:
        character_pool += string.ascii_lowercase
        password.append(secrets.choice(string.ascii_lowercase))

    if use_uppercase:
        character_pool += string.ascii_uppercase
        password.append(secrets.choice(string.ascii_uppercase))

    if use_digits:
        character_pool += string.digits
        password.append(secrets.choice(string.digits))

    if use_symbols:
        character_pool += string.punctuation
        password.append(secrets.choice(string.punctuation))

    if not character_pool:
        raise EmptyCharacterPoolError(
            "At least one character set must be enabled."
        )

    required_characters = len(password)

    if length < required_characters:
        raise InvalidPasswordLengthError(
            f"Password length must be at least {required_characters} "
            "based on the selected character sets."
        )

    for _ in range(length - required_characters):
        password.append(
            secrets.choice(character_pool)
        )

    rng = secrets.SystemRandom()
    rng.shuffle(password)

    return "".join(password)