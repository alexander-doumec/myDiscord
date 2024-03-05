from database import Database

class Appel : 
    def __init__(self) -> None:
        self.table = 'appels'
        self.database = Database(host='localhost', user='root', password='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', database='mydiscord')

    def appeler(self, utilisateur_id, canal_id):
        #Vérifier si l'utilisateur et le canal existent dans la base de données
        utilisateur = self.database.fetch('SELECT * FROM utilisateurs WHERE ID = %s', (utilisateur_id,))

        canal = self.database.fetch('SELECT * FROM canaux WHERE ID = %s', (canal_id,))

        if utilisateur and canal :
            print(f"Appel initié à l'utilisateur {utilisateur_id} sur le canal {canal_id}")
        else:
            print("Erreur : l'utilisateur ou le canal n'existe pas")

    #Ici, je donne l'exemple pour créer une méthode pour répondre, malheuresement il me manque une table canal appel, avec avec un statut état
            #dans ma base de donné
    #def decrocher(self, appel_id):
        #query = f'UPDATE {self.table} SET Etat = "en cours" WHERE ID = %s'
        #params = (appel_id)
        #self.database.executeQuery(query, params)
            
    #def raccrocher(self, appel_id):
        #query = f'UPDATE {self.table} SET Etat = "terminé" WHERE ID = %s'
        #params = (appel_id)
        #self.database.executeQuery(query, params)