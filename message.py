from database import Database

class Message : 
    def __init__(self) -> None:
        self.table = 'messages'
        self.database = Database(host='localhost', user='root', password='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', database='mydiscord')

    def envoyer(self, utilisateur_id, canal_id, contenu):
        query = f'INSERT INTO {self.table} (UtilisateurID, CanalID, Contenu) Values (%s,%s,%s)'
        params = (utilisateur_id, canal_id, contenu)
        self.database.executeQuery(query, params)
    
    #LA methode lire permet de récupérer tous les messages de la base de données d'un canal spécifiques
    def lire(self, canal_id):
        query = f'SELECT * FROM {self.table} WHERE CanalID = %s'
        params = (canal_id)
        result = self.database.fetch(query, params)
        #row permet d'accéder aux données 
        for row in result:
            print(f"{row['UtilisateurID']}: {row['Contenu']} (envoyé à {row['Timestamp']})")