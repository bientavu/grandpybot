
def answer(question):
    # 1. Question nettoyée = utiliser une classe Parser pour
    #    analyser la question et conserver uniquement l'info
    #    utile (c'est à dire l'info de lieu)

    # 2. La question nettoyée est envoyée à une API de geocoding
    #    (here.com) pour obtenir (a) l'adresse du lieu et (b)
    #    les coordonnées de latitude et longitude

    # 3. Envoyer la latitude et la longitude à l'API wikipedia
    #    qui va nous envoyer des articles liés à ces coordonnées.
    #    On choisit l'article consernant le lieu le plus proche

    return {
        # Infos récupérées en réponse à la question
    }