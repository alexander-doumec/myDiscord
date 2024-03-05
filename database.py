import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user 
        self.password = password 
        self.database = database
        self.connection = None
        self.cursor = None

    #Méthode pour établir la connexion à la bdd
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database,
                auth_plugin='mysql_native_password'
            )
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as err:
            print(f"Error connection: {err}")


    #Méthode pour fermer la connexion a la bdd
    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    #Méthode pour éxécuter une requete sans résiltat(INSERT, UPDATE, DELETE)
    def executeQuery(self, query, params=None):
        self.connect()
        try:
            self.cursor.execute(query, params or ())
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Erreur lors de l'exécution de la requête : {err}")
            self.connection.rollback()
        finally:
            self.disconnect()


    #Méthode pour éxécuter une requete avec plusieurs résultats (SELECT)
    def fetch(self, query, params=None):
        self.connect()
        try:
            self.cursor.execute(query, params or ())
            result = self.cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print(f"Erreur lors de l'exécution de la requête : {err}")
        finally:
            self.disconnect()

    #Méthode pour exécuter une requete avec un seule resultat 
    def fetchone(self, query, params=None):
        self.connect()
        try:
            self.cursor.execute(query, params or ())
            result = self.cursor.fetchone()
            return result
        except mysql.connector.Error as err:
            print(f"Erreur lors de l'exécution de la requête : {err}")
        finally:
            self.disconnect()

            

if __name__ == '__main__':
    db = Database(host='localhost', user='root', password='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', database='mydiscord')
    print(db.fetch('SHOW TABLES'))
