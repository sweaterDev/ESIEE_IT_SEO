import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def supprimer_balises_html(html):
    """Retourne le texte HTML sans les balises."""
    soup = BeautifulSoup(html, 'html.parser')
    # Extraire le texte du HTML
    texte_sans_balises = soup.get_text(separator=' ', strip=True)
    
    return texte_sans_balises

def extraire_valeurs_balises(html, nom_balise, nom_attribut):
    """Retourne une liste de valeurs associées aux balises."""
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

def extraire_nom_domaine(url):
    """Extrait le nom de domaine d'une URL."""
    return urlparse(url).netloc

def filtrer_urls_par_domaine(nom_domaine, liste_urls):
    """Retourne deux listes d'URLs : celles du domaine et celles hors du domaine."""
    urls_du_domaine = []
    urls_hors_domaine = []

    domaine_base = extraire_nom_domaine("http://" + nom_domaine).lower()

    for url in liste_urls:
        
        domaine_url = extraire_nom_domaine(url).lower()

        # Comparer les domaines
        if domaine_url == domaine_base:
            urls_du_domaine.append(url)
        else:
            urls_hors_domaine.append(url)

    return urls_du_domaine, urls_hors_domaine


def recuperer_texte_html(url):
    """Récupère le texte HTML d'une page à partir de son URL."""
    try:
        # Effectuer la requête HTTP pour récupérer le contenu de la page
        reponse = requests.get(url)
        # Vérifier si la requête a réussi (statut 200 OK)
        if reponse.status_code == 200:
            return reponse.text
        else:
            print(f"Erreur de requête HTTP. Statut : {reponse.status_code}")
            return None

    except requests.RequestException as e:
        print(f"Erreur lors de la requête HTTP : {e}")
        return None