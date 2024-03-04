from database import Database
import re

class Utilisateur :
    def __init__(self) -> None:
        self.table = 'utilisateurs'
        self.database = Database(host='localhost', user='root', password='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', database='mydiscord')

    def inscription(self,nom, prenom, email, mot_de_passe):
        #Vérification si le mot de passe contient des caractères spéciaux 
        if not re.search('[!@#$%^&*(),.?":;|<>]'):
            print("Erreur : le mot de passe doit contenir des caractères spéciaux")
            return
        
        query = f'INSERT INTO {self.table} (nom, prenom, email, mot_de_passe) VALUES (%s,%s,%s,%s)'
        params = (nom, prenom, email, mot_de_passe)
        self.database.executeQuery(query, params)

    def connexion(self, email, mot_de_passe):
        query = f'SELECT * FROM {self.table} WHERE email = %s AND mot_de_passe = %s'
        params = (email, mot_de_passe)
        result = self.database.executeQuery(query,params)
        if result : 
            print("Connexion réussie")
        else:
            print("Erreur de connexion : email ou mot de passe incorect")

    def deconnexion(self):
        self.database.closeConnection()