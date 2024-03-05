from database import Database
import hashlib
import os

class Utilisateur :
    #Initialisation de la clasee avec la connexion à la base de données
    def __init__(self) -> None:
        self.table = 'utilisateurs'
        self.database = Database(host='localhost', user='root', password='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', database='mydiscord')
     
     #Méthode pour Hasher le mot de passe avec un sel
    def hash_password(self, mot_de_passe):
        salt = os.urandom(16)
        hashed_password = hashlib.pbkdf2_hmac('sha256', mot_de_passe.encode(), salt, 100000)
        return salt, hashed_password
    
    #Méthode pour l'inscription d'un nouvel utilisateur 
    def inscription(self, nom, prenom, email, mot_de_passe):
    # Vérifie d'abord si l'email existe déjà
        query = f'SELECT * FROM {self.table} WHERE Email = %s'
        params = (email,)
        try:
            result = self.database.executeQuery(query, params)
            # Lire tous les résultats de la requête
            result.fetchall()
        except Exception as e:
            print(f"Une erreur s'est produite lors de la vérification de l'email : {e}")
            return False

    # Si l'email n'existe pas, procéde à l'insertion
        if not result:
            salt, hashed_password = self.hash_password(mot_de_passe)
            query = f"INSERT INTO {self.table} (Nom, Prenom, Email, MotDePasse) VALUES (%s, %s, %s, %s)"
            params = (nom, prenom, email, hashed_password, salt)
            try:
                self.database.executeQuery(query, params)
                return True
            except Exception as e:
                print(f"Une erreur s'est produite lors de l'insertion de l'utilisateur : {e}")
                return False
        else:
            print("Erreur : cet email est déjà utilisé")
            return False



    # Méthode pour la connexion d'un utilisateur
    def connexion(self, email, mot_de_passe):
        query = f'SELECT * FROM {self.table} WHERE Email = %s AND MotDePasse = %s'
        params = (email, mot_de_passe)
        result = self.database.fetchone(query, params)

        if result:
            return True
        else:
            return False
        

    #Méthode pour vérifier l'existence d'un canal de la base de données
    def recuperer_utilisateur_id(self, email):
        query = f'SELECT ID FROM {self.table} WHERE Email = %s'
        params = (email,)
        result = self.database.fetchone(query, params)
        try:
            if result:
                return result[0]  # Accédez au premier élément du tuple
            else:
                return None
        except TypeError as e:
            print(f"Erreur lors de la récupération de l'ID : {e}")
            return None
        
    def verifier_existence_canal(self, canal_id):
        query = f'SELECT * FROM canaux WHERE ID = %s'
        params = (canal_id,)

        result = self.database.fetchone(query, params)

        if result:
            print(f"Le canal avec CanalID {canal_id} existe dans la table canaux.")
            return True
        else:
            print(f"Le canal avec CanalID {canal_id} n'existe pas dans la table canaux.")
            return False
        