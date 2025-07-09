from tkinter import Tk, Label, Button, Entry, StringVar, Checkbutton, IntVar
import string
import random
import pyperclip
import webbrowser

def copy_to_clipboard(text):
    pyperclip.copy(text)  # Copie le texte dans le presse-papiers

def generate_password(length, use_specials):
    charset = string.ascii_letters + string.digits  # Définit le jeu de caractères de base (lettres et chiffres)
    if use_specials:
        charset += string.punctuation  # Ajoute des caractères spéciaux si l'option est sélectionnée
    password = ''.join(random.choice(charset) for _ in range(length))  # Génère le mot de passe
    return password

def update_password():
    password_length = int(entry.get())  # Récupère la longueur du mot de passe depuis l'entrée utilisateur
    use_specials = bool(specials.get())  # Vérifie si l'option des caractères spéciaux est cochée
    new_password = generate_password(password_length, use_specials)  # Génère un nouveau mot de passe
    password.set('*' * len(new_password))  # Remplace le mot de passe par des astérisques pour l'affichage
    copy_to_clipboard(new_password)  # Copie le mot de passe dans le presse-papiers

root = Tk()
root.geometry("400x155")  # Définit la taille de la fenêtre principale
root.title("Générateur de mots de passe V2")  # Définit le titre de la fenêtre

root.iconbitmap('./images/generativepassw.ico')  # Définit l'icône de la fenêtre

password = StringVar(root)
password.set('*' * 20)  # Initialise avec des astérisques

Label(root, text="Longueur du mot de passe :").pack()  # Étiquette pour la longueur du mot de passe
entry = Entry(root, show='')  # Champ de saisie pour la longueur du mot de passe
entry.pack()
entry.insert(0, "15")  # Valeur par défaut de 15 caractères

specials = IntVar()
Checkbutton(root, text="Inclure des caractères spéciaux", variable=specials).pack()  # Permet à l'utilisateur de cocher pour les caractères spéciaux

Button(root, text="Générer un nouveau mot de passe", command=update_password).pack()  # Bouton pour générer un nouveau mot de passe

Label(root, textvariable=password).pack()  # Étiquette pour afficher le mot de passe (masqué par des astérisques)

Button(root, text='Mes projets Github', command=lambda: webbrowser.open('https://github.com/Gw3nhael51')).pack()  # Bouton pour ouvrir le lien vers les projets GitHub

root.mainloop()  # Lance la boucle principale de l'interface graphique
