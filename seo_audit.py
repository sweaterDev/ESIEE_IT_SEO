import csv
from bs4 import BeautifulSoup

#Retourne un dictionnaire de mots présent dans un text ainsi que ses occuerences
# arg un texte
# compléxité en temps O(n),complexité en espace O(m).
def compter_mots_occurences(texte):
    mots = texte.lower().split()
    occurrences = {}
    
    for mot in mots:
        occurrences[mot] = occurrences.get(mot, 0) + 1

    return sorted(occurrences.items(), key=lambda x: x[1], reverse=True)

#Retourne une copie d'un dictionnaire sans ses mots parasites qu'on aura définie
# args dictionnaire cible , listes mots parasites
# compléxité en temps O(n),complexité en espace O(m).
def filtrer_mots_parasites(dict_avec_parasites, mots_parasites):
    # Créer une copie de la structure de données pour éviter de modifier l'original
    occurrences = dict(dict_avec_parasites)

    # Supprimer les mots parasites du dictionnaire
    for mot_parasite in mots_parasites:
        occurrences.pop(mot_parasite, None)

    return occurrences

#Retourne une liste de mots parasites lus dans un fichier csv
# arg le path vers le fichier csv
# compléxité en temps O(n),complexité en espace O(n).
def lire_mots_parasites(fichier_csv):
    mots_parasites = []

    with open(fichier_csv, newline='', encoding='utf-8') as csvfile:
        lecteur_csv = csv.reader(csvfile)
        for ligne in lecteur_csv:
            mots_parasites.extend(ligne)

    return mots_parasites

def supprimer_balises_html(html):
    # Analyser le HTML avec BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Extraire le texte du HTML
    texte_sans_balises = soup.get_text(separator=' ', strip=True)

    return texte_sans_balises

#Etape 4 
#text ="Etape 9 : Créer une fonction prenant en paramètre une chaine de caractère représentant un nom de domaine, et une liste de valeurs qui sont des url et qui retourne deux listes avec les url qui font partie du domaine et ceux qui n’en font pas partie."
#fichier ="parasite.csv"
#print(filtrer_mots_parasites(compter_mots_occurences(text),lire_mots_parasites(fichier)))

#Test Etape 5
#html_exemple = """
#<html>
 # <head>
   # <title>Exemple HTML</title>
  #</head>
  #<body>
   # <p>Ceci est un <b>exemple</b> de texte <a href="#">HTML</a>.</p>
  #</body>
#</html>
#"""
#print(supprimer_balises_html(html_exemple))