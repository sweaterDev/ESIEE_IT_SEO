# ESIEE_IT_SEO
# Audit SEO

Ce projet vise à fournir des outils d'audit SEO pour analyser le contenu des pages web, compter les occurrences de mots, filtrer les mots parasites, extraire des informations utiles, etc.

## Fonctionnalités

- **Compter les Occurrences de Mots :** L'outil permet de compter les occurrences de mots dans le contenu textuel d'une page web.

- **Filtrer les Mots Parasites :** Filtrer les mots parasites à partir d'une liste prédéfinie pour obtenir des résultats plus pertinents.

- **Extraire des Informations :** Extraire des informations telles que les liens entrants et sortants, la présence de balises alt dans les images, etc.

## Comment Utiliser

1. **Installer les Dépendances :** Assurez-vous d'avoir les dépendances nécessaires installées en exécutant `pip install -r requirements.txt`.

2. **Lancer l'Audit :** Utilisez le script `seo_audit.py` pour lancer un audit sur une page web spécifique. Par exemple :

    ```bash
    python seo_audit.py
    ```

3. **Personnaliser :** Vous pouvez personnaliser les paramètres d'audit, ajouter de nouveaux modules, ou étendre les fonctionnalités en fonction de vos besoins.

## Structure du Projet

- `wordCounter.py`: Module pour compter les occurrences de mots.
- `parasiteFilter.py`: Module pour filtrer les mots parasites.
- `htmlParser.py`: Module pour analyser le HTML et extraire des informations.

## Auteurs

- [smercellus]

## Licence

Ce projet est sous licence [insérez la licence de votre choix].
## Version
1.0
