#Définition des réponses possible du joueur:

pierre = ["Pierre", "pierre", "Cailloux", "cailloux"]
feuille = ["Feuille", "feuille", "Papier", "papier"]
ciseaux = ["Ciseaux", "ciseaux", "ciseau", "Ciseau"]

#Récupération du choix du joueur:

def choix_joueur():
    choix = input("Voulez vous jouer Pierre, Feuille ou Ciseaux? : ")

    while choix not in pierre and choix not in feuille and choix not in ciseaux :
        print("Nous n'avons pas compris votre coup de génie, veuillez choisir à nouveau parmis Pierre, Feuille ou Ciseaux.")
        choix = input()
    return choix