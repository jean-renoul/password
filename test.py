import random
import string

def mdp_aleatoire():
    minuscules = string.ascii_lowercase
    majuscules = string.ascii_uppercase
    chiffres = string.digits
    caractere_special = string.punctuation
    aleatoire = minuscules + majuscules + chiffres + caractere_special

    random_mdp = [
        random.choice (minuscules),
        random.choice (majuscules),
        random.choice (chiffres),
        random.choice (caractere_special),
    ]

    random_mdp.extend(random.choices(aleatoire, k=8))
    random.shuffle(random_mdp)
    random_mdp = "".join(random_mdp)
    print (random_mdp)