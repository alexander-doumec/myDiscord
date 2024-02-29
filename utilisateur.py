from database import Database

class Utilisateur :
    def __init__(self) -> None:
        self.table = 'utilisateurs'
        self.database = Database(host='localhost', user='root', password='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', database='mydiscord')

    def inscription(self,nom, prenom, email, mot_de_passe):
        query = f'INSERT INTO {self.table} (nom, prenom, email, mot_de_passe) VALUES (%s,%s,%s,%s)'
        params = (nom, prenom, email, mot_de_passe)
        self.database.executeQuery(query, params)

    def connexion(self, email, mot_de_passe):
        query = f'SELECT email FROM utilisateurs'