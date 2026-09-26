import pytest

from velawarp import dessiner_carre, dessiner_rectangle, dessiner_triangle


def test_dessiner_carre():
    assert dessiner_carre(2) == "**\n**"


def test_dessiner_rectangle_avec_symbole_personnalise():
    assert dessiner_rectangle(3, 2, "#") == "###\n###"


def test_dessiner_triangle():
    assert dessiner_triangle(3) == "  *\n ***\n*****"


def test_dessiner_refuse_les_dimensions_invalides():
    with pytest.raises(ValueError):
        dessiner_carre(0)