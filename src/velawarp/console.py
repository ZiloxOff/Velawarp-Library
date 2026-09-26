"""Fonctions simples pour afficher et demander des valeurs."""


def afficher(*valeurs: object, sep: str = " ", fin: str = "\n") -> None:
    """Affiche une ou plusieurs valeurs, comme print."""
    print(*valeurs, sep=sep, end=fin)


def demander(message: str) -> str:
    """Demande une reponse texte a la personne."""
    return input(message)


def demander_entier(message: str) -> int:
    """Demande une valeur entiere."""
    return int(demander(message))


def demander_decimal(message: str) -> float:
    """Demande un nombre decimal; la virgule francaise est acceptee."""
    reponse = demander(message).replace(",", ".")
    return float(reponse)