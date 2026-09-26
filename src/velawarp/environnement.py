"""Lecture des variables d'environnement et des fichiers .env."""

import os
from pathlib import Path

from dotenv import load_dotenv


def charger_env(fichier: str | Path = ".env", ecraser: bool = False) -> bool:
    """Charge un fichier .env; retourne False si le fichier est absent."""
    return load_dotenv(dotenv_path=Path(fichier), override=ecraser)


def obtenir_env(cle: str, valeur_par_defaut: str | None = None) -> str | None:
    """Lit une variable d'environnement, avec une valeur de secours."""
    return os.getenv(cle, valeur_par_defaut)