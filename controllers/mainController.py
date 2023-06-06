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
options = ["symfony", "django", "react","angular","vue","laravel","flask","express"]
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
    lError.pack(side="bottom")
    try:
        match cbType.get():
            case "react":
               if os.system("node -v")!=0:
                   lError.config(text="Node.js n'est pas installé. Veuillez le télécharger à partir de https://nodejs.org.")
               else:
                   os.system(f"npx create-react-app {projName}")

            case "symfony":
                if os.system("php -v") != 0:
                    lError.config(text="PHP n'est pas installé. Veuillez l'installer.")
                elif os.system("composer --version") != 0:
                    lError.config(text="Composer n'est pas installé. Veuillez le télécharger à partir de https://getcomposer.org.")
                else:
                    os.system(f"composer create-project symfony/website-skeleton {projName}")

            case "django":
                try:
                    os.chdir(tfFolder.get())
                    import django
                except OSError as e:
                    lError.config(text=f"Erreur lors de la création du répertoire : {e}")
                except ImportError:
                    try:
                        os.system("pip install Django")
                    except Exception as e:
                        lError.config(text="Erreur lors de l'installation de Django : " + str(e))
                os.system(f"django-admin startproject {tfName.get()}")

            case "angular":
                os.chdir(tfFolder.get())
                if os.system("ng version") != 0:
                    lError.config(text="Installation de Angular CLI.")
                    os.system("npm install -g @angular/cli")
                os.system(f"ng new {tfName.get()} --skip-git")

            case "vue":
                os.chdir(tfFolder.get())
                if os.system("vue --version") != 0:
                    lError.config(text="Installation de Vue CLI.")
                    os.system("npm install -g @vue/cli")
                os.system(f"vue create {tfName.get()} --no-git --registry=https://registry.npmjs.org --default")#--skip-install pour retirer yarn

            case "laravel":
                os.chdir(tfFolder.get())
                if os.system("laravel --version") != 0:
                    lError.config(text="Installation de Laravel CLI.")
                elif os.system("composer --version") != 0:
                    lError.config(text="Composer n'est pas installé. Veuillez le télécharger à partir de https://getcomposer.org.")
                else:
                    os.system(f"laravel new {tfName.get()}")

            case "flask":
                try:
                    import flask
                except ImportError:
                    try:
                        os.system("pip install Flask")
                    except Exception as e:
                        lError.config(text="Erreur lors de l'installation de Flask : " + str(e))
                else:
                    lError.config(text="Flask est déjà installé.")
                os.chdir(tfFolder.get())
                os.mkdir(tfName.get())
                os.chdir(tfName.get())
                with open("app.py", "w") as file:
                    file.write("from flask import Flask\n\napp = Flask(__name__)\n\n@app.route('/')\ndef index():\n    "
                               "return 'Hello, Flask!'\n\nif __name__ == '__main__':\n    app.run()")

            case "express":
                if os.system("express --version") != 0:
                    lError.config(text="Installation de Express.js.")
                os.system("npm install -g express-generator")
                os.system(f"express --view=pug {projName}")

            case _:
                lError.config(text="error no type selected")
    except Exception as e:
        lError.config(text=str(e))


    if lError.cget("text")=="":
        lError.config(text="Projet créé avec succès !")