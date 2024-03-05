import tkinter as tk 
from tkinter import messagebox, scrolledtext
from message import Message
from appels import Appel
from utilisateur import Utilisateur

class Interface: 
    def __init__(self, utilisateur_id, canal_id):
        #Initialise la classe Interface avec les informations utilisateur et canal
        self.utilisateur_id = utilisateur_id
        self.canal_id = canal_id
        self.message = Message()
        self.appel = Appel()
        self.utilisateur = Utilisateur()

        #Créer une fenetre Tkinter
        self.fenetre = tk.Tk()
        self.fenetre.title("Interface")

        #Zone de texte déroulante pour afficher les messages 
        self.texte_messages = scrolledtext.ScrolledText(self.fenetre)
        self.texte_messages.pack()

        #Champ de saisie pour entrer le message
        self.entry_message = tk.Entry(self.fenetre)
        self.entry_message.pack()

        #Bouton pour envoyer le message 
        self.bouton_envoyer = tk.Button(self.fenetre, text="Envoyer", command=self.envoyer_message)
        self.bouton_envoyer.pack()

        #Bouton pour supprimer le message sélectionné
        self.bouton_supprimer = tk.Button(self.fenetre, text="Supprimer le message sélectionné", command=self.supprimer_message)
        self.bouton_supprimer.pack()

        #Liste pour stocker les boutons des messages
        self.messages = []
        self.message_selectionne = None

        # Boutton de déconnexion
        self.button_deconnexion = tk.Button(self.fenetre, text="Deconnexion", command=self.fenetre.quit)
        self.button_deconnexion.pack()
    

    def envoyer_message(self):
        #Récupère le contenue du champs saisie
        contenu = self.entry_message.get()

        #Vérifier l'existence du canal
        if self.utilisateur.verifier_existence_canal(self.canal_id):

            #ENvoie du message 
            self.message.envoyer(self.utilisateur_id, self.canal_id, contenu)
            self.entry_message.delete(0, tk.END)
            self.afficher_messages()
        else:
            print("Erreur : Le canal n'existe pas.")
        

    def supprimer_message(self):
        #Supprime le message sélectionné
        if self.message_selectionne is not None : 
          self.message.supprimerMessage(self.message_selectionne['ID']) 
          self.message_selectionne = None
          self.afficher_messages() 
    
    def selectionner_message(self, message):
        #sélectionne un message lorsqu'on clique dessus
        self.message_selectionne = message

    def afficher_messages(self):
        #Affiche tous les messages du canal de la fenetre 
        for bouton in self.messages:
            bouton.destroy()

        self.messages = []
        messages = self.message.lire(self.canal_id)
        for message in messages:
            bouton = tk.Button(self.fenetre, text=f"{message['UtilisateurID']}: {message['Contenu']} (envoyé à {message['Timestamp']})", command=lambda m=message: self.selectionner_message(m))
            bouton.pack()
            self.messages.append(bouton)

    def run(self):
        #Lance la boucle principale de la fenetre Tkinter
        self.fenetre.mainloop()

        
if __name__ == "__main__":
    # Crée une instancede l'interface de la fenetre et la lance
    interface = Interface(utilisateur_id=1, canal_id=1)
    interface.run()
