"""Operations mathematiques de base et calculs de surfaces."""

import math


def additionner(a: int | float, b: int | float) -> int | float:
    return a + b


def soustraire(a: int | float, b: int | float) -> int | float:
    return a - b


def multiplier(a: int | float, b: int | float) -> int | float:
    return a * b


def diviser(a: int | float, b: int | float) -> float:
    return a / b


def aire_rectangle(largeur: int | float, hauteur: int | float) -> int | float:
    return largeur * hauteur


def aire_triangle(base: int | float, hauteur: int | float) -> float:
    return base * hauteur / 2


def aire_cercle(rayon: int | float) -> float:
    return math.pi * rayon**2