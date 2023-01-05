# Projet python Pasword generator 17/11/2022

# Import de modules

import secrets
import string
from tkinter import * #Pour la fenêtre graphique

# Definition des fonctions

fenetre = Tk()

# Definition de la taille de la fenetre 

fenetre.geometry('500x500')  
fenetre.resizable(width=False, height=False )

# Coleur background

fenetre.configure(bg='black') 

# Affichage du nom du programme
var = StringVar()
label = Label(fenetre, textvariable=var)
var.set("Password Generator")
label.pack(pady=20)

# Fonction qui recupere la valeur du champ texte

def recupere():

    # Recuperation de l'input de l'utiliateur 
    res = entree.get()
    
    # Ecriture de de la valeur dans un fichier txt
    fichier = open("temp.txt", "w")
    fichier.write(res)
    fichier.close()

    # On ouvre le fichier en mode 'read' :
    fichier = open("temp.txt", 'r')

    # On lis le fichier et on le stock dans un variable
    contenu_du_fichier = fichier.readlines()

    if (int(res) > 0 ):

        # Creation des différents alphabets
        letters = string.ascii_letters
        digits = string.digits
        special_chars = string.punctuation

        # Creation de l'alphabet
        alphabet = letters + digits + special_chars

        # Input permettant de demander à l'utilisateur de combien de caractères sont mots de passe doit-il faire
        nbcarac = contenu_du_fichier [0] [0]

        # Convertir nbcarac qui était en string en int
        nbcarac = int(nbcarac)

        # Dire la longueur du mots de passe à partir de nbcarac
        mdp_long = nbcarac

        # Générateur de mots de passe
        mdp = ''    #Empecher les espaces
        for i in range(mdp_long):   #pour i de longueur mdp_long (input utilisateur)
            mdp += ''.join(secrets.choice(alphabet)) # créer le mot de passe sans espace de façon aléatoire
        
        # Ecriture du mot de passe dans un fichier txt
        fichier = open("mdp.txt", "w")
        fichier.write("mot de passe : " + mdp)
        fichier.close()
        
        # Afficg¡hage du met de passe 
        texteLabel = Label(fenetre, text = mdp, width=30)
        texteLabel.pack(pady=20)

        # Buton de fermeture du programe
        Button(fenetre, text="Quit", command=fenetre.destroy).pack()

# Affichage du titre du champ text

var2 = StringVar()
label2 = Label(fenetre, textvariable=var2)
var2.set("Nombre de chiffres du mot de passe")
label2.pack()     

# Declaration du champ text 

value = StringVar() 
value.set(0)
entree = Entry(fenetre, textvariable=value, width=30)
entree.pack(pady=20)
entree.pack()

# Declaraton du buton valider
bouton = Button(fenetre, text="Valider", command=recupere)
bouton.pack()

# Indique à Python d'exécuter la boucle d'événements de Tkinter

fenetre.mainloop()























