caracteres_speciaux = "!@#$%^&*()-+?_=,<>/"
prompt_mdp = input ("Veuillez entrer votre mot de passe : ")

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
    

print (verification(prompt_mdp))
