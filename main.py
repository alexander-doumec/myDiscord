import tkinter as tk
from inscription import FenetreInscription  
from connexion import FenetreConnexion  

class FenetrePrincipale:
    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.title("Accueil")
        self.fenetre.geometry("300x200")


        #Création d'un bouton pour ouvrir la fenetre d'inscription
        self.bouton_inscription = tk.Button(self.fenetre, text="Inscription", command=self.ouvrir_inscription)
        self.bouton_inscription.pack(expand=True)

        #Création d'un bouton pour ouvrir la fenetre de connexion
        self.bouton_connexion = tk.Button(self.fenetre, text="Connexion", command=self.ouvrir_connexion)
        self.bouton_connexion.pack(expand=True)


    #Méthode pour ouvrir la fenetre d'inscription
    def ouvrir_inscription(self):
        self.fenetre_inscription = FenetreInscription()
        self.fenetre_inscription.run()

    #Méthode pour ouvrir la fenetre de connexion
    def ouvrir_connexion(self):
        self.fenetre_connexion = FenetreConnexion()
        self.fenetre_connexion.run()

    def run(self):
        self.fenetre.mainloop()

if __name__ == "__main__":
    fenetre_principale = FenetrePrincipale()
    fenetre_principale.run()
