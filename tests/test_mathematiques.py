import math

from velawarp import (
    additionner,
    aire_cercle,
    aire_rectangle,
    aire_triangle,
    diviser,
    multiplier,
    soustraire,
)


def test_operations_de_base():
    assert additionner(2, 3) == 5
    assert soustraire(5, 3) == 2
    assert multiplier(4, 3) == 12
    assert diviser(9, 3) == 3


def test_calculs_de_surface():
    assert aire_rectangle(4, 3) == 12
    assert aire_triangle(4, 3) == 6
    assert math.isclose(aire_cercle(1), math.pi)