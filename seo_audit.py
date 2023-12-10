#pip install requests
import requests
import csv
#pip install bs4
from bs4 import BeautifulSoup
from urllib.parse import urlparse

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
#Retourne une liste de valeurs associées aux balises.
#args Code html, nom de la balise cible, nom de l'attribut cible
def extraire_valeurs_balises(html, nom_balise, nom_attribut):
    valeurs = []

    # Analyser le HTML avec BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Trouver toutes les balises spécifiées avec l'attribut correspondant
    balises = soup.find_all(nom_balise)

    # Extraire les valeurs associées à l'attribut spécifié
    for balise in balises:
        valeur_attribut = balise.get(nom_attribut)
        if valeur_attribut is not None:
            valeurs.append(valeur_attribut)

    return valeurs
#extrait le nom de domaine d'une url
#arg url du nom de domaine à extraire
def extraire_nom_domaine(url):

    return urlparse(url).netloc

def filtrer_urls_par_domaine(nom_domaine, liste_urls):
    urls_du_domaine = []
    urls_hors_domaine = []

    # Analyser le nom de domaine
    composants_domaine = urlparse("http://" + nom_domaine)
    domaine_base = composants_domaine.netloc.lower()

    for url in liste_urls:
        # Analyser l'URL
        composants_url = urlparse(url)
        domaine_url = composants_url.netloc.lower()

        # Comparer les domaines
        if domaine_url == domaine_base:
            urls_du_domaine.append(url)
        else:
            urls_hors_domaine.append(url)

    return urls_du_domaine, urls_hors_domaine

def recuperer_texte_html(url):
    try:
        # Effectuer la requête HTTP pour récupérer le contenu de la page
        print("récupération des infos de la page")
        reponse = requests.get(url)
        print("fait !")
        # Vérifier si la requête a réussi (statut 200 OK)
        if reponse.status_code == 200:
            return reponse.text
        else:
            print(f"Erreur de requête HTTP. Statut : {reponse.status_code}")
            return None

    except requests.RequestException as e:
        print(f"Erreur lors de la requête HTTP : {e}")
        return None

#Test Etape 4 
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

# Test Etape 6
#html_exemple = """
#<html>
 # <head>
  #  <title>Exemple HTML</title>
  #</head>
 # <body>
   # <a href="https://example.com">Website</a>
  #  <a href="mailto:m.bluth@example.com">Email</a>
   # <p class="paragraphe">Troisième valeur</p>
 # </body>
#</html>
#"""

#nom_balise_exemple = 'a'
#nom_attribut_exemple = 'href'

#resultat = extraire_valeurs_balises(html_exemple, nom_balise_exemple, nom_attribut_exemple)

# Afficher le résultat
print(extraire_nom_domaine("https://kinsta.com/fr/blog/commentaires-python/"))
print(recuperer_texte_html("https://esiee-it.blackboard.com/ultra/courses/_101859_1/outline/edit/document/_1173113_1?courseId=_101859_1&view=content"))