import csv

def filtrer_mots_parasites(dict_avec_parasites, mots_parasites):
    """Retourne une copie d'un dictionnaire sans les mots parasites définis."""
    occurrences = dict(dict_avec_parasites)

    # Supprimer les mots parasites du dictionnaire
    for mot_parasite in mots_parasites:
        occurrences.pop(mot_parasite, None)

    return occurrences

def lire_mots_parasites(fichier_csv):
    """Retourne une liste de mots parasites lus dans un fichier CSV."""
    mots_parasites = []

    with open(fichier_csv, newline='', encoding='utf-8') as csvfile:
        lecteur_csv = csv.reader(csvfile)
        for ligne in lecteur_csv:
            mots_parasites.extend(ligne)

    return mots_parasites

