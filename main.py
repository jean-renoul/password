import hashlib
import json
import random
import string

# Caractères spéciaux possibles dans les mots de passe
caracteres_speciaux = string.punctuation

# Fonction de vérification du mot de passe
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

# Fonction de hachage du mot de passe
def hashage(mdp):
    global mdp_hashe
    mdp_hashe = hashlib.sha256(mdp.encode('utf-8')).hexdigest()
    return mdp_hashe

# Fonction de stockage du mot de passe dans un fichier JSON
def dump(i, h):
    data = i, h
    with open("passwords.json", "r") as f:
        data_file = f.read()
        if (i not in data_file) and (h not in data_file):
            with open ("passwords.json", "r") as f:
                data_file = json.load (f)
                data_file.append(data)
                with open("passwords.json","w") as f:
                    json.dump(data_file, f)
        else:
            print ("Echec : le mot de passe est déjà utilisé ou vous avez déjà un mot de passe enregistré pour ce site")

# Fonction d'affichage de tous les mots de passe stockés
def affichage():
    with open("passwords.json", "r") as f:
        data = json.load(f)
        print (data)

# Fonction de génération de mot de passe aléatoire
def mdp_aleatoire():
    global mdp
    minuscules = string.ascii_lowercase
    majuscules = string.ascii_uppercase
    chiffres = string.digits
    aleatoire = minuscules + majuscules + chiffres + caracteres_speciaux

    mdp = [
        random.choice (minuscules),
        random.choice (majuscules),
        random.choice (chiffres),
        random.choice (caracteres_speciaux),
    ]

    mdp.extend(random.choices(aleatoire, k=8))
    random.shuffle(mdp)
    mdp = "".join(mdp)
    return mdp

# Interface utilisateur
prompt_base = input ("Voulez-vous ajouter un mot de passe ? (oui/non)")

if prompt_base == "oui":
    prompt_aleatoire = input ("Voulez-vous créer vous-même un mot de passe ou en générer un aléatoirement (perso/aléatoire)")
    if prompt_aleatoire == "perso":
        prompt_mdp = input ("Veuillez entrer votre mot de passe : ")
        verification(prompt_mdp)
        hashage(prompt_mdp)
    elif prompt_aleatoire == "aléatoire":
        mdp_aleatoire()
        hashage(mdp)

    prompt_stockage = input ("Voulez-vous stocker votre mot de passe ? (oui/non)")    

    if prompt_stockage == "oui":
        prompt_nom_mdp = input ("Pour quel site / machine souhaitez-vous ajouter un mot de passe ? ")
        dump(prompt_nom_mdp, mdp_hashe)

prompt_affichage = input("Voulez-vous afficher vos mots de passe ? (oui/non)")

if prompt_affichage == "oui":
    affichage()

prompt_base
