import hashlib
import json

caracteres_speciaux = "!@#$%^&*()-+?_=,<>/"


def verification(mdp):
    erreur = 0
    while True:
        if len(mdp) < 8:
            print ("Votre mot de passe doit comporter au moins 8 caractères")
            erreur +=1
        if mdp.islower():
            print ("Votre mot de passe doit comporter au moins une lettre majuscule")
            erreur +=1
        if mdp.isupper():
            print ("Votre mot de passe doit comporter au moins une lettre minuscule")
            erreur +=1
        res = any(caractere in caracteres_speciaux for caractere in mdp)
        if res == False:
            print ("Votre mot de passe doit comporter au moins un caractère spécial")
            erreur +=1
        res2 = any(caractere.isdigit() for caractere in mdp)
        if res2 == False:
            print ("Votre mot de passe doit contenir au moins un chiffre")
            erreur +=1
        if erreur == 0:
            print ("Votre mot de passe est valide")
            return mdp
        erreur = 0
        mdp = input ("Veuillez entrer votre mot de passe : ")


def hashage(mdp):
    global mdp_hashe
    mdp_hashe = hashlib.sha256(mdp.encode('utf-8')).hexdigest()
    return mdp_hashe

def dump(i,h):
    data = [i,h]
    with open("test.json", "r") as f:
        data_file = json.load (f)
        data_file.append(data)
    with open("test.json","w") as f:
        json.dump(data_file, f)

def affichage():
    with open("test.json", "r") as f:
        data = json.load(f)
        print (data)

prompt_base = input ("Voulez vous ajouter un mot de passe ? (oui/non)")

if prompt_base == "oui":
    prompt_mdp = input ("Veuillez entrer votre mot de passe : ")
    verification(prompt_mdp)

prompt_hashage = input("Voulez vous hasher votre mot de passe ? (oui/non)")

if prompt_hashage == "oui":
    print (hashage(prompt_mdp))

prompt_stockage = input ("Voulez vous stocker votre mot de passe ? (oui/non)")
prompt_nom_mdp = input ("Quel est le mot de passe que vous souhaitez ajouter ? ")

if prompt_stockage == "oui":
    dump(prompt_nom_mdp, mdp_hashe)

prompt_affichage = input("Voulez vous afficher vos mots de passe ? (oui/non)")

if prompt_affichage == "oui":
    affichage()