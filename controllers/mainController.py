import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from models.Projet import Projet
# Fenetre
fenetre = tk.Tk()

# Folder
tfFolder = tk.Entry(fenetre)

# Type
options = ["symfoni", "django", "react"]
lType = tk.Label(text="Please select a type:")
cbType = ttk.Combobox(fenetre, values=options, state='readonly')

# Name
lName = tk.Label( fenetre, text = "project name" )
tfName = tk.Entry(fenetre)
btnVerif = tk.Button(fenetre,text="verifier")

def creer_fenetre():
    # Fenetre
    fenetre.title("Ma fenêtre Tkinter")
    fenetre.geometry("400x300")

    # Folder apres select, affiche Type
    tfFolder.pack()
    btnFolderChooser = tk.Button(fenetre,text="Choisie le répertoire", command=pickFolder)
    btnFolderChooser.pack()

    # Type apres select, affiche Name
    def typeChanged(event):
        lName.pack()
        tfName.pack()
        btnVerif.pack()
    cbType.bind('<<ComboboxSelected>>', typeChanged)

    btnCreate = tk.Button(fenetre, text="créé", command=createProject)
    btnCreate.pack()
    fenetre.mainloop()
def pickFolder():
    tfFolder.delete(0, tk.END)
    tfFolder.insert(0, filedialog.askdirectory())
    lType.pack()
    cbType.pack()

def createProject():
    proj = Projet(tfFolder.get(),cbType.get(),tfName.get())
    print(proj)
