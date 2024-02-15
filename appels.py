import sqlite3

class Appel:
    def __init__(self, expediteur_id, destinataire_id):
        self.expediteur_id = expediteur_id
        self.destinataire_id = destinataire_id
        self.en_cours = False

    def passer_appel(self):
        self.en_cours = True
        print(f"Appel en cours de {self.expediteur_id} à {self.destinataire_id}")

        conn = sqlite3.connect('ma_base_de_donnees.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO appels (expediteur_id, destinataire_id, en_cours) VALUES (?, ?, ?)", 
                       (self.expediteur_id, self.destinataire_id, self.en_cours))

        conn.commit()
        conn.close()

    def decrocher(self):
        if self.en_cours:
            print(f"Appel décroché par {self.destinataire_id}")
        else:
            print("Aucun appel en cours")

    def raccrocher(self):
        if self.en_cours:
            self.en_cours = False
            print(f"Appel terminé entre {self.expediteur_id} et {self.destinataire_id}")

            conn = sqlite3.connect('ma_base_de_donnees.db')
            cursor = conn.cursor()

            cursor.execute("UPDATE appels SET en_cours = ? WHERE expediteur_id = ? AND destinataire_id = ?", 
                           (self.en_cours, self.expediteur_id, self.destinataire_id))

            conn.commit()
            conn.close()
        else:
            print("Aucun appel à raccrocher")
