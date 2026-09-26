"""Transformations de texte."""

import re
import unicodedata


def slugify(value: str, separator: str = "-") -> str:
    """Convertit un texte en identifiant lisible dans une URL."""
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    words = re.sub(r"[^a-zA-Z0-9]+", separator, ascii_value.lower())
    return words.strip(separator)


def normalize_whitespace(value: str) -> str:
    """Remplace toute suite d'espaces par un espace simple."""
    return " ".join(value.split())


def truncate(value: str, max_length: int, suffix: str = "...") -> str:
    """Limite un texte a max_length, suffixe inclus."""
    if max_length < 0:
        raise ValueError("max_length doit etre positif ou nul")
    if len(value) <= max_length:
        return value
    if max_length <= len(suffix):
        return suffix[:max_length]
    prefix = value[: max_length - len(suffix)].rstrip()
    return prefix + suffix