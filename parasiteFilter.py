import csv

"""
Module Parasite Filter

Ce module offre des fonctionnalités pour filtrer les mots parasites d'un dictionnaire d'occurrences de mots.

"""

def filtrer_mots_parasites(dict_avec_parasites, mots_parasites):
    """
    Filtre les mots parasites d'un dictionnaire d'occurrences de mots.
    
    :param dict_avec_parasites: Le dictionnaire d'occurrences de mots.
    :param mots_parasites: La liste des mots parasites à filtrer.
    :return: Un nouveau dictionnaire sans les mots parasites.
    """
    occurrences = dict(dict_avec_parasites)

    # Supprimer les mots parasites du dictionnaire
    for mot_parasite in mots_parasites:
        occurrences.pop(mot_parasite, None)

    return occurrences

def lire_mots_parasites(fichier_csv):
    """
    Lit les mots parasites à partir d'un fichier CSV.

    :param fichier_csv: Le chemin vers le fichier CSV.
    :return: Une liste de mots parasites.
    """
    mots_parasites = []

    with open(fichier_csv, newline='', encoding='utf-8') as csvfile:
        lecteur_csv = csv.reader(csvfile)
        for ligne in lecteur_csv:
            mots_parasites.extend(ligne)

    return mots_parasites

