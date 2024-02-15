import sqlite3
from datetime import datetime

class Message: 
    def __init__(self, id, expediteur_id, destinataire_id, contenu, vu=False):
        self.id = id
        self.expediteur_id = expediteur_id
        self.destinataire_id = destinataire_id
        self.contenu = contenu
        self.date_envoi = datetime.now()
        self.vu = vu

    def envoyer_message(self):
        conn = sqlite3.connect('ma_base_de_donnees.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO messages (id, expediteur_id, destinataire_id, contenu, date_envoi, vu) VALUES (?, ?, ?, ?, ?, ?)", 
                       (self.id, self.expediteur_id, self.destinataire_id, self.contenu, self.date_envoi, self.vu))

        conn.commit()
        conn.close()

    def marquer_comme_vu(self):
        self.vu = True

        conn = sqlite3.connect('ma_base_de_donnees.db')
        cursor = conn.cursor()

        cursor.execute("UPDATE messages SET vu = ? WHERE id = ?", (self.vu, self.id))

        conn.commit()
        conn.close()
