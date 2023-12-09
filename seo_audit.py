#Retourne un dictionnaire de mots présent dans un text ainsi que ses occuerences
# compléxité en temps O(n),complexité en espace O(m).
# args un texte
def compter_mots_occurences(texte):
    mots = texte.lower().split()
    print(mots)
    occurrences = {}
    
    for mot in mots:
        occurrences[mot] = occurrences.get(mot, 0) + 1

    return sorted(occurrences.items(), key=lambda x: x[1], reverse=True)

   
def filtrer_mots_parasites(dict_avec_parasites, mots_parasites):
    # Créer une copie de la structure de données pour éviter de modifier l'original
    occurrences = dict(dict_avec_parasites)

    # Supprimer les mots parasites du dictionnaire
    for mot_parasite in mots_parasites:
        occurrences.pop(mot_parasite, None)

    return occurrences