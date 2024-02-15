import sqlite3
import re

class Utilisateur :
    def __init__(self, id,nom, prenom, email, mot_de_passe):
        self.id = id
        self.nom = nom 
        self.prenom = prenom
        self.email = email 
        self.mot_de_passe = mot_de_passe
        

    def inscription(cls, id, nom, prenom, email, mot_de_passe):
        #Vérifiez que le mot de passe respecte les contraintes
        if not re.match(r'[A-Za-z0-9@#$%&^+=]{8,}', mot_de_passe):
            raise ValueError("Le mot de passe doit comporter au moins 8 caractères et contenir des lettres, des chiffres et des symboles spéciaux")
        
        conn = sqlite3.connect('bdd')
        cursor = conn.cursor()

        #verifier si l'email existe deja 
        cursor.execute("SELECT * FROM utilisateurs WHERE email=?", (email,))
        utilisateur = cursor.fetchone()

        if utilisateur is not None: 
            raise ValueError("L'email est déjà utilisé")
        
        #Créez un nouvel utilisateur
        nouvel_utilisateur = cls(id, nom, prenom, email, mot_de_passe)
        cursor.execute("INSERT INTO utilisateurs VALUES (?, ?, ?, ?, ?)", (id, nom, prenom, email, mot_de_passe))

        conn.commit()
        conn.close()

    def se_connecter(self, email, mot_de_passe):
        #conn = sqlite3.connect('bdd')
        #cursor = conn.cursor()

        #cursor.execute("SELECT * FROM utilisateurs WHERE email=? AND mot_de_passe=?",(email, mot_de_passe))
        #utilisateur = cursor.fetchonne()
        #conn.close()

        if email == self.email and mot_de_passe == self.mot_de_passe:
            return True
        else:
            False

    def voir_ami(self):
        conn = sqlite3.connect('bdd')
        cursor = conn.cursor()

        cursor.execute("SELECT ami_id FROM amis WHERE utilisateur_id=?", (self.id,))
        amis = cursor.fetchall()

        conn.close()

        return [ami[0] for ami in amis]
    
    def ajouter_ami(self, nom_ami):
        conn = sqlite3.connect('ma_base_de_donnees.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO amis (utilisateur_id, ami_id) VALUES (?, ?)", (self.id, id_ami))

        conn.commit()
        conn.close()

    def supprimer_ami(self, nom_ami):
        conn = sqlite3.connect('ma_base_de_donnees.db')
        cursor = conn.cursor()

        cursor.execute("DELETE FROM amis WHERE utilisateur_id=? AND ami_id=?", (self.id, id_ami))

        conn.commit()
        conn.close()