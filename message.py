from database import Database

class Message : 
    def __init__(self) -> None:
        #Initialise la classe Message avec le nom de latable dans la BDD et crée une instance de la classe DATABASE 
        self.table = 'messages'
        self.database = Database(host='localhost', user='root', password='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', database='mydiscord')

    def envoyer(self, utilisateur_id, canal_id, contenu):
        #Vérifier si le canal existe
        if not self.verifier_existence_canal(canal_id):
            print("Erreur : Le canal n'existe pas")
            return
        
        print(f"UtilisateurID avant l'envoie du message : {utilisateur_id}")
        print(f"CanalID avant l'envoie du message : {canal_id}")

        #Prépare la requête SQL pour insérer un nouveau message
        query = f'INSERT INTO {self.table} (UtilisateurID, CanalID, Contenu) Values (%s,%s,%s)'
        params = (utilisateur_id, canal_id, contenu)

        try:
            #exécute la requête SQL pour envoyer un nouveau message
            self.database.executeQuery(query, params)
            print("Message envoyé avec succès")
        except Exception as e: 
            print(f"Erreur lors de l'envoi du message : {e}")
    
    #LA methode lire permet de récupérer tous les messages de la base de données d'un canal spécifiques
    def lire(self, canal_id):

        #récupere tous les messages d'un canal spécifique
        query = f'SELECT * FROM {self.table} WHERE CanalID = %s'
        params = (canal_id,)
        try:

            #Execute la requête SQL pour récupérer le message
            result = self.database.fetch(query, params)
            #Formate les résultats en un format de dictionnaire
            messages = []
            for row in result:
                message = {
                    'UtilisateursID' : row['UtilisateurID'],
                    'Contenu' : row['Contenu'], 
                    'Timestamp' : row['Timestamp'] 
                }
                messages.append(message)

            # Retourne la liste des messages 
            return messages
        except Exception as e:
            print(f"Une erreur s'est produite lors de la lecture des messages : {e}")
            return None

    #Méthode qui permet de supprimer les message, mais cetté méthode supprimera le message de la base de donées et ne sera pas récupérable 
    def supprimerMessage(self, message_id):
        #Supprime un message de la base de données
        query = f'DELETE FROM {self.table} WHERE ID = %s'
        params = (message_id,)
        self.database.executeQuery(query, params)

    def verifier_existence_canal(self, canal_id):
        #Vérifie l'existence d'un canal dans la table canaux
        query = f'SELECT * FROM canaux WHERE ID = %s'
        params = (canal_id,)
        result = self.database.fetchone(query, params)

        if result:
            print(f"Le canal avec CanalID {canal_id} existe dans la table canaux.")
            return True
        else:
            print(f"Le canal avec CanalID {canal_id} n'existe pas dans la table canaux.")
            return False