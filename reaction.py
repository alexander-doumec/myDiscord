from database import Database


class Reaction:
    def __init__(self) -> None:

        #Initialisation de la classe avec la connexion à la base de données et la table 'reaction'
        self.table = 'reactions'
        self.database = Database(host='localhost', user='root', password='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', database='mydiscord')


    #Méthode pour ajouter une réaction (emoji) à un message 
    def ajouter_emoji(self, message_id, utilisateur_id, emoji):

        # Définition de la requête SQL pour l'insertion d'une réaction dans la table 'reactions'
        query = f'INSERT INTO {self.table} (MessageID, UtilisateurID, Emoji) VALUES (%s,%s,%s)'
        
        # Définition des paramètres pour la requête
        params = (message_id, utilisateur_id, emoji)

        
        self.database.executeQuery(query, params)