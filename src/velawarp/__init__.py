"""Outils simples pour nettoyer et transformer des donnees."""

from velawarp.collections import chunked, flatten
from velawarp.console import afficher, demander, demander_decimal, demander_entier
from velawarp.environnement import charger_env, obtenir_env
from velawarp.formes import dessiner_carre, dessiner_rectangle, dessiner_triangle
from velawarp.mathematiques import (
    additionner,
    aire_cercle,
    aire_rectangle,
    aire_triangle,
    diviser,
    multiplier,
    soustraire,
)
from velawarp.text import normalize_whitespace, slugify, truncate

__version__ = "0.1.0"

__all__ = [
    "__version__",
    "additionner",
    "afficher",
    "aire_cercle",
    "aire_rectangle",
    "aire_triangle",
    "charger_env",
    "chunked",
    "demander",
    "demander_decimal",
    "demander_entier",
    "dessiner_carre",
    "dessiner_rectangle",
    "dessiner_triangle",
    "diviser",
    "flatten",
    "multiplier",
    "normalize_whitespace",
    "obtenir_env",
    "slugify",
    "soustraire",
    "truncate",
]