# Velawarp

Velawarp regroupe des fonctions Python faciles a retenir en francais: console, mathematiques, formes texte et fichiers `.env`.

## Installation

Il faut Python 3.10 ou plus recent et Git installe. Depuis un environnement virtuel active, utilise `python` pour installer Velawarp dans cet environnement:

```powershell
python -m pip install "git+https://github.com/ZiloxOff/Velawarp-Library.git"
```

Sous Windows, si tu n'utilises pas d'environnement virtuel, tu peux utiliser le lanceur `py` pour installer dans le Python par defaut:

```powershell
py -m pip install "git+https://github.com/ZiloxOff/Velawarp-Library.git"
```

Puis importe la bibliotheque dans ton code:

```python
import velawarp as vw

vw.afficher("Velawarp est installe !")
```

## Developper Velawarp

```powershell
python -m pip install -e ".[dev]"
```

## Utilisation

```python
import velawarp as vw

vw.afficher("Bonjour !")
nom = vw.demander("Ton nom: ")
vw.afficher("Salut", nom)

print(vw.additionner(2, 3))
print(vw.aire_cercle(2))
print(vw.dessiner_triangle(4))

vw.charger_env()
cle_api = vw.obtenir_env("CLE_API")
```

Pour les nombres saisis au clavier, utilise `demander_entier` ou `demander_decimal`. Cette derniere accepte la virgule, par exemple `3,5`.

Les fonctions de dessin retournent du texte: affiche-le avec `vw.afficher(vw.dessiner_carre(4))`.

Les variables `.env` sont chargees avec `python-dotenv`, inclus dans les dependances de la bibliotheque.

Les fonctions de calcul disponibles sont `additionner`, `soustraire`, `multiplier`, `diviser`, `aire_rectangle`, `aire_triangle` et `aire_cercle`.

Les utilitaires texte et collections restent disponibles: `slugify`, `normalize_whitespace`, `truncate`, `chunked` et `flatten`.

## Architecture

```text
.
|-- pyproject.toml
|-- README.md
|-- src/
|   `-- velawarp/
|       |-- __init__.py
|       |-- console.py
|       |-- environnement.py
|       |-- formes.py
|       |-- mathematiques.py
|       |-- collections.py
|       `-- text.py
`-- tests/
    |-- test_collections.py
    |-- test_console.py
    |-- test_environnement.py
    |-- test_formes.py
    |-- test_mathematiques.py
    `-- test_text.py
```

Importe `velawarp` une seule fois avec `import velawarp as vw`; les fonctions sont regroupees par domaine dans les modules et reunies sous le meme prefixe.

Lancer les tests avec `pytest`.

'# Example de code'

'import velawarp as vw'

'age = vw.demander("Quel age a tu ? : ")'

'vw.sortie(f"Tu as {age} ans.")'
