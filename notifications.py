from database import Database

class Notification:
    def __init__(self) -> None:
        self.database = Database(host='localhost', user='root', password='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', database='mydiscord')

    def notifier_message(self, utilisateur_id, message_id):
        #Récupérer le message de la base de données
        query = 'SELECT * FROM messages WHERE ID = %s'
        params = (message_id)
        message = self.database.fetch(query, params)[0]
        #Vérifiez que le message est destiné à l'utilisateur 
        if message['UtilisateurID'] == utilisateur_id:
        #Affichez la notifications 
            print(f"Notification : Vous avez recu un nouveau message de {message['UtilisateurID']}")

    def notifier_appel(self, utilisateur_id, appel_id):
        #Récupérez l'appel de la base de donées
        query = 'SELECT * FROM appels WHERE ID = %s'
        params = (appel_id)
        appel = self.database.fetch(query, params)[0]
        #Vérifiez que le message est destiné à l'utilisateur 
        if appel['UtilisateurID'] == utilisateur_id:
        #Affichez la notification
            print(f"Notification : Vous avez recu un appel de {appel['UtilisateurID']}")