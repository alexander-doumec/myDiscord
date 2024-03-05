import tkinter as tk
from tkinter import messagebox
from utilisateur import Utilisateur  
from interface import Interface

class FenetreConnexion:
    def __init__(self):
        #Initialisation de la fenetre de connexion
        self.utilisateur = Utilisateur() #instance de la classe Utilisateur
        self.fenetre = tk.Tk()
        self.fenetre.title("Connexion")
        self.fenetre.geometry("300x200")
        self.fenetre.configure(bg="lightblue")

        #Création des widgets (étiquettes, champs de saisie, bouton)
        tk.Label(self.fenetre, text="Email", bg="lightblue").grid(row=0)
        tk.Label(self.fenetre, text="Mot de passe", bg="lightblue").grid(row=1)

        self.email = tk.Entry(self.fenetre)
        self.mot_de_passe = tk.Entry(self.fenetre,show="*")

        self.email.grid(row=0, column=1)
        self.mot_de_passe.grid(row=1, column=1)

        tk.Button(self.fenetre, text="Se connecter", command=self.connexion, bg="lightgreen").grid(row=2, column=1, pady=10)

    def connexion(self):
        #Méthode appeler lors du clic sur le bouton "Se connecter"
        result = self.utilisateur.connexion(self.email.get(), self.mot_de_passe.get())

        if result:
            #Si connexion réussie, récupère contenu de saisie email et renvoie l'ID de l'utilisateur
            utilisateur_id = self.utilisateur.recuperer_utilisateur_id(self.email.get())
            messagebox.showinfo("Connexion", "Connexion réussie!")
            self.ouvrir_interface_messages(utilisateur_id)
            
        else:
            #Si connexion échoué
            messagebox.showerror("Erreur", "Email ou mot de passe incorrect")

    def ouvrir_interface_messages(self, utilisateur_id):
        #Méthode pour ouvrir l'interface des messages
        fenetre_messages = Interface(utilisateur_id = utilisateur_id, canal_id=1)
        fenetre_messages.run()

    def run(self):
        #Lancement de la boucle principale de la fenetre 
        self.fenetre.mainloop()

if __name__ == "__main__":
    #Création et éxécution de la fenetre de connexion
    fenetre_connexion = FenetreConnexion()
    fenetre_connexion.run()
