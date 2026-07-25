from pathlib import Path

from src.config.hash_algorithms import HASH_ALGORITHMS


CHUNK_SIZE = 4096
DEFAULT_ALGORITHM = "sha256"


class InvalidHashAlgorithmError(Exception):
    """Raised when an unsupported hash algorithm is requested."""
    pass


class HashFileNotFoundError(Exception):
    """Raised when the specified file does not exist."""
    pass


class InvalidFileError(Exception):
    """Raised when the provided path is not a file."""
    pass


def _get_hasher(algorithm: str):
    """
    Validate the requested hash algorithm and return a hash object.
    """

    algorithm = algorithm.strip().lower()

    hasher_factory = HASH_ALGORITHMS.get(algorithm)

    if hasher_factory is None:
        supported_algorithms = ", ".join(HASH_ALGORITHMS.keys())

        raise InvalidHashAlgorithmError(
            f"Unsupported hash algorithm '{algorithm}'. "
            f"Supported algorithms: {supported_algorithms}."
        )

    return hasher_factory()


def hash_text(
    text: str,
    algorithm: str = DEFAULT_ALGORITHM,
) -> str:
    """
    Generate the hash of a text string.

    Args:
        text: Text to hash.
        algorithm: Hash algorithm to use.

    Returns:
        Hexadecimal hash digest.
    """

    hasher = _get_hasher(algorithm)

    hasher.update(text.encode("utf-8"))

    return hasher.hexdigest()


def hash_file(
    file_path: Path,
    algorithm: str = DEFAULT_ALGORITHM,
) -> str:
    """
    Generate the hash of a file.

    Args:
        file_path: Path to the file.
        algorithm: Hash algorithm to use.

    Returns:
        Hexadecimal hash digest.
    """

    if not file_path.exists():
        raise HashFileNotFoundError(
            f"File '{file_path}' does not exist."
        )

    if not file_path.is_file():
        raise InvalidFileError(
            f"'{file_path}' is not a valid file."
        )

    hasher = _get_hasher(algorithm)

    with file_path.open("rb") as file:
        while chunk := file.read(CHUNK_SIZE):
            hasher.update(chunk)

    return hasher.hexdigest()