def trouver_max(liste):
    if len(liste) == 1:
        return liste[0]
    else:
        max_precedent = trouver_max(liste[1:])
        return liste[0] if liste[0] > max_precedent else max_precedent
