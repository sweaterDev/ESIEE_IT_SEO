"""
Module Word Counter

Ce module contient des fonctions pour compter les occurrences des mots dans un texte.

"""
def compter_occurrences_mots(texte):
    """
    Compte les occurrences des mots dans un texte.
    
    :param texte: Le texte à analyser.
    :return: Une liste de tuples contenant les mots et leur nombre d'occurrences, triée par fréquence.
    """
    mots = texte.lower().split()
    occurrences = {}
    
    for mot in mots:
        occurrences[mot] = occurrences.get(mot, 0) + 1

    return sorted(occurrences.items(), key=lambda x: x[1], reverse=True)

