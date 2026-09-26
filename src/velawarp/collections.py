from collections.abc import Iterable, Iterator
from typing import TypeVar

T = TypeVar("T")


def chunked(items: Iterable[T], size: int) -> Iterator[list[T]]:
    """Decoupe un iterable en blocs de taille maximale size."""
    if size <= 0:
        raise ValueError("size doit etre strictement positif")

    chunk: list[T] = []
    for item in items:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def flatten(items: Iterable[Iterable[T]]) -> Iterator[T]:
    """Aplati un niveau d'iterables sans creer de liste intermediaire."""
    for group in items:
        yield from group