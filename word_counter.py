def compter_occurrences_mots(texte):
    """Retourne un dictionnaire de mots présents dans un texte ainsi que leurs occurrences."""
    mots = texte.lower().split()
    occurrences = {}
    
    for mot in mots:
        occurrences[mot] = occurrences.get(mot, 0) + 1

    return sorted(occurrences.items(), key=lambda x: x[1], reverse=True)

