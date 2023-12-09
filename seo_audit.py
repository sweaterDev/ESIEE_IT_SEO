#Retourne un dictionnaire de mots présent dans un text ainsi que ses occuerences
# compléxité en temps O(n),complexité en espace O(m).
# args un texte
def compter_mots_occurences(texte):
    mots = texte.lower().split()
    print(mots)
    occurrences = {}
    
    for mot in mots:
        occurrences[mot] = occurrences.get(mot, 0) + 1

    mots_occurrences_tries = sorted(occurrences.items(), key=lambda x: x[1], reverse=True)

    return mots_occurrences_tries

   
