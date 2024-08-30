from tkinter import Tk, Label, Button, Entry, StringVar, Checkbutton, IntVar
import string
import random
import pyperclip
import webbrowser

def copy_to_clipboard(text):
    pyperclip.copy(text)

def generate_password(length, use_specials):
    charset = string.ascii_letters + string.digits
    if use_specials:
        charset += string.punctuation
    password = ''.join(random.choice(charset) for _ in range(length))
    return password

def update_password():
    password_length = int(entry.get())
    use_specials = bool(specials.get())
    new_password = generate_password(password_length, use_specials)
    password.set('*' * len(new_password))  # Remplace le mot de passe par des astérisques
    copy_to_clipboard(new_password)

root = Tk()
root.geometry("400x155")
root.title("Générateur de mots de passe V2")

root.iconbitmap('D:/IA/generativepassw.ico')

password = StringVar(root)
password.set('*' * 20)  # Initialise avec des astérisques

Label(root, text="Longueur du mot de passe :").pack()
entry = Entry(root, show='')
entry.pack()
entry.insert(0, "15")

specials = IntVar()
Checkbutton(root, text="Inclure des caractères spéciaux", variable=specials).pack()

Button(root, text="Générer un nouveau mot de passe", command=update_password).pack()

Label(root, textvariable=password).pack()

Button(root, text='Mes projets Github', command=lambda: webbrowser.open('https://github.com/Gw3nhael51')).pack()

root.mainloop()
