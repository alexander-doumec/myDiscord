import sqlite3 


class Notification: 
    def __init__(self, utilisateur_id):
        self.utilisateur_id = utilisateur_id

    def notifier_message(self):
        conn = sqlite3.connect('ma_base_de_donnees.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM messages WHERE destinataire_id=? AND vu=0", (self.utilisateur_id,))
        messages_non_lus = cursor.fetchall()

        for message in messages_non_lus:
            print(f"Vous avez un nouveau message de {message[1]}: {message[3]}")

        conn.close()

    def notifier_appel(self):
        conn = sqlite3.connect('ma_base_de_donnees.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM appels WHERE destinataire_id=? AND en_cours=1", (self.utilisateur_id,))
        appels_en_cours = cursor.fetchall()

        for appel in appels_en_cours:
            print(f"Vous avez un appel entrant de {appel[1]}")

        conn.close()