from velawarp import afficher, demander, demander_decimal, demander_entier


def test_afficher_ecrit_les_valeurs(capsys):
    afficher("Bonjour", 42)
    assert capsys.readouterr().out == "Bonjour 42\n"


def test_demander_retourne_la_saisie(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "salut")
    assert demander("Ton mot: ") == "salut"


def test_demander_entier_convertit_la_saisie(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "12")
    assert demander_entier("Un entier: ") == 12


def test_demander_decimal_accepte_la_virgule(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "3,5")
    assert demander_decimal("Un nombre: ") == 3.5