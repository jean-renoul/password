import json
mdp = "1&Asqdqsdqsdqsfdssgfbbcvbd"
data = ["mot de passe", mdp]
with open("test.json", "w") as f:
    json.dump (data, f)