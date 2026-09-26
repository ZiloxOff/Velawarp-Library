"""Dessins de formes simples en texte."""


def _verifier(largeur: int, hauteur: int, symbole: str) -> None:
    if largeur <= 0 or hauteur <= 0:
        raise ValueError("Les dimensions doivent etre positives")
    if len(symbole) != 1:
        raise ValueError("Le symbole doit contenir un seul caractere")


def dessiner_carre(taille: int, symbole: str = "*") -> str:
    """Retourne un carre compose du symbole choisi."""
    _verifier(taille, taille, symbole)
    ligne = symbole * taille
    return "\n".join([ligne] * taille)


def dessiner_rectangle(largeur: int, hauteur: int, symbole: str = "*") -> str:
    """Retourne un rectangle compose du symbole choisi."""
    _verifier(largeur, hauteur, symbole)
    ligne = symbole * largeur
    return "\n".join([ligne] * hauteur)


def dessiner_triangle(hauteur: int, symbole: str = "*") -> str:
    """Retourne un triangle compose du symbole choisi."""
    _verifier(1, hauteur, symbole)
    lignes = [" " * (hauteur - ligne) + symbole * (2 * ligne - 1) for ligne in range(1, hauteur + 1)]
    return "\n".join(lignes)