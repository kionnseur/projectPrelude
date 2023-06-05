import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import re
import os
# Fenetre
fenetre = tk.Tk()

# Folder
tfFolder = tk.Entry(fenetre)

# Type
options = ["symfony", "django", "react"]
lType = tk.Label(text="Please select a type:")
cbType = ttk.Combobox(fenetre, values=options, state='readonly')

# Name
lName = tk.Label( fenetre, text = "project name" )
tfName = tk.Entry(fenetre)
btnVerif = tk.Button(fenetre,text="verifier")

#cree
btnCreate = tk.Button(fenetre, text="créé")

lError = tk.Label(fenetre)
def creer_fenetre():

    # Fenetre
    fenetre.title("Ma fenêtre Tkinter")
    fenetre.geometry("400x300")

    # Folder, apres select affiche Type
    tfFolder.pack()
    btnFolderChooser = tk.Button(fenetre,text="Choisie le répertoire", command=pickFolder)
    btnFolderChooser.pack()

    # Type, apres select affiche Name
    def typeChanged(event): #event pour la select du type
        lName.pack()
        tfName.pack()
        btnVerif.pack()
    cbType.bind('<<ComboboxSelected>>', typeChanged)

    # Name, apres verif affiche cree (check verifieName)
    btnVerif.config(command=verifieName)

    btnCreate.config(command=createProject)
    fenetre.mainloop()
def pickFolder():
    tfFolder.delete(0, tk.END)
    tfFolder.insert(0, filedialog.askdirectory())
    lType.pack()
    cbType.pack()

def verifieName():
    print("btn verif")
    if (re.match("^[a-zA-Z\d][\w-]{0,29}[a-zA-Z\d]$",tfName.get())):
        print(" pass")
        btnCreate.pack()
    else:
        btnCreate.forget()

def createProject():
    # proj = Projet(tfFolder.get(),cbType.get(),tfName.get())
    projName=tfFolder.get()+"/"+tfName.get()
    try:
        match cbType.get():
            case "react":
               if os.system("node -v")==0:
                    os.system(f"npx create-react-app {projName}")
               else:
                   lError.config(text="Node.js n'est pas installé. Veuillez le télécharger à partir de https://nodejs.org.")

            case "symfony":
                if os.system("php -v") != 0:
                    lError.config(text="PHP n'est pas installé. Veuillez l'installer.")
                elif os.system("composer --version") != 0:
                    lError.config(text="Composer n'est pas installé. Veuillez le télécharger à partir de https://getcomposer.org.")
                else:
                    os.system(f"composer create-project symfony/website-skeleton {projName}")

            case _:
                lError.config(text="error no type selected")
    except Exception as e:
        lError.config(text=str(e))

    lError.pack(side="bottom")