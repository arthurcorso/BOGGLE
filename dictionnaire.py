def charger_dictionnaire(chemin):
    with open(chemin, encoding="utf-8") as f:
        return set(mot.strip().upper() for mot in f if len(mot.strip()) >= 3)
