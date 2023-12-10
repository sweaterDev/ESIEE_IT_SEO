from wordCounter import compter_occurrences_mots
from parasiteFilter import filtrer_mots_parasites, lire_mots_parasites
from htmlParser import supprimer_balises_html, extraire_valeurs_balises, extraire_nom_domaine, filtrer_urls_par_domaine, recuperer_texte_html

def audit_page(url):
    # Récupérer le texte HTML de la page
    html = recuperer_texte_html(url)

    if html is not None:
        # Supprimer les balises HTML
        texte_sans_balises = supprimer_balises_html(html)

        # Compter les occurrences des mots et afficher les 3 premières
        occurrences_mots = compter_occurrences_mots(texte_sans_balises)
        print("Occurrences des mots (3 premières valeurs) :")
        print(occurrences_mots[:3],"\n")

        # Lire les mots parasites depuis un fichier CSV
        fichier_parasites = "parasite.csv"
        mots_parasites = lire_mots_parasites(fichier_parasites)

        # Filtrer les mots parasites et afficher les occurrences restantes
        occurrences_filtrees = filtrer_mots_parasites(occurrences_mots, mots_parasites)
        print("Occurrences des mots (filtrées des mots parasites) :")
        print(occurrences_filtrees,"\n")

        # Extraire les liens entrants et sortants
        liens_entrants = extraire_valeurs_balises(html, 'a', 'href'), 
        liens_sortants = []
        print("Nombre de liens entrants :", len(liens_entrants),liens_entrants)
        if liens_sortants :
            print("Nombre de liens sortants :", len(liens_sortants),"\n")

        # Vérifier la présence de balises alt dans les images
        balises_alt = extraire_valeurs_balises(html, 'img', 'alt')
        print("Présence de balises alt dans les images :", balises_alt)

if __name__ == "__main__":
    # Saisir l'URL de la page à analyser
    page_url = input("Veuillez entrer l'URL de la page à analyser : \n")

    # Lancer l'audit de la page
    audit_page(page_url)
