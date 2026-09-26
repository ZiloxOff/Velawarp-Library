from velawarp import charger_env, obtenir_env


def test_charger_env_et_obtenir_variable(tmp_path, monkeypatch):
    cle = "VELAWARP_TEST_MESSAGE"
    monkeypatch.delenv(cle, raising=False)
    fichier = tmp_path / ".env"
    fichier.write_text(f"{cle}=bonjour\n", encoding="utf-8")

    assert charger_env(fichier)
    assert obtenir_env(cle) == "bonjour"


def test_obtenir_env_utilise_la_valeur_par_defaut():
    assert obtenir_env("VELAWARP_CLE_ABSENTE", "defaut") == "defaut"