import tkinter as tk
from tkinter import messagebox
from utilisateur import Utilisateur  

class FenetreInscription:
    def __init__(self):
        self.utilisateur = Utilisateur()
        self.fenetre = tk.Tk()

        #Création de label pour les champs de saisie
        tk.Label(self.fenetre, text="Nom").grid(row=0)
        tk.Label(self.fenetre, text="Prénom").grid(row=1)
        tk.Label(self.fenetre, text="Email").grid(row=2)
        tk.Label(self.fenetre, text="Mot de passe").grid(row=3)

        #Créationn des champs de saisie
        self.nom = tk.Entry(self.fenetre)
        self.prenom = tk.Entry(self.fenetre)
        self.email = tk.Entry(self.fenetre)
        self.mot_de_passe = tk.Entry(self.fenetre, show="*")


        #Placement des champs de saisie dans la fenetre 
        self.nom.grid(row=0, column=1)
        self.prenom.grid(row=1, column=1)
        self.email.grid(row=2, column=1)
        self.mot_de_passe.grid(row=3, column=1)

        #Création du bouton s'inscrire avec la méthode associé 
        tk.Button(self.fenetre, text="S'inscrire", command=self.inscription).grid(row=4, column=1, pady=10)

    def inscription(self):
        # Appel de la méthode d'inscription de la classe Utilisateur avec les valeurs saisies
        success = self.utilisateur.inscription(self.nom.get(), self.prenom.get(), self.email.get(), self.mot_de_passe.get())

        # Affichage d'un message d'information ou d'erreur en fonction du résultat de l'inscription
        if success:
            messagebox.showinfo("Inscription", "Inscription réussie!")
        else:
            messagebox.showerror("Erreur d'inscription", "L'inscription a échoué. Vous êtes déja inscris.Veuillez réessayer.")
    def run(self):
        self.fenetre.mainloop()

fenetre_inscription = FenetreInscription()
fenetre_inscription.run()
