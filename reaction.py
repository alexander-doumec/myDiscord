from database import Database


class Reaction:
    def __init__(self) -> None:
        self.table = 'reactions'
        self.database = Database(host='localhost', user='root', password='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', database='mydiscord')

    def ajouter_emoji(self, message_id, utilisateur_id, emoji):
        query = f'INSERT INTO {self.table} (MessageID, UtilisateurID, Emoji) VALUES (%s,%s,%s)'
        params = (message_id, utilisateur_id, emoji)
        self.database.executeQuery(query, params)