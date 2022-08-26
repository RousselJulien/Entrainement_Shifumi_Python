from .choix_joueur import choix_joueur
import random
from .choix_joueur import pierre
from .choix_joueur import feuille
from .choix_joueur import ciseaux

#Délimitation des choix possibles pour Johnny:

possibilites_johnny = ["Pierre", "Feuille", "Ciseaux"]

#Fonction permettant de déterminer le vainqueur à chaque round et d'incrémenter ainsi le nombre de victoires respectives des deux joueurs:

def check():
    victoire_johnny = 0
    victoire_joueur = 0
    while victoire_johnny <= 2 or victoire_joueur <= 2 :
        choix_joueur1 = choix_joueur()
        choix_IA = random.choice(possibilites_johnny)

        if choix_joueur1 in pierre and choix_IA in feuille :
            print(f"Johnny a joué {choix_IA} et a gagné!! Vraiment trop fort ce Johnny.")
            victoire_johnny += 1
    
        if choix_joueur1 in feuille and choix_IA in ciseaux :
            print(f"Johnny a joué {choix_IA} et a gagné!! Vraiment trop fort ce Johnny.")
            victoire_johnny += 1
    
        if choix_joueur1 in ciseaux and choix_IA in pierre :
            print(f"Johnny a joué {choix_IA} et a gagné!! Vraiment trop fort ce Johnny.")
            victoire_johnny += 1
    
        if choix_joueur1 in pierre and choix_IA in ciseaux :
            print(f"Johnny a joué {choix_IA}! Vous avez gagné!! Johnny n'avait aucune chance...")
            victoire_joueur += 1
    
        if choix_joueur1 in feuille and choix_IA in pierre :
            print(f"Johnny a joué {choix_IA}! Vous avez gagné!! Johnny n'avait aucune chance...")
            victoire_joueur += 1
    
        if choix_joueur1 in ciseaux and choix_IA in feuille :
            print(f"Johnny a joué {choix_IA}! Vous avez gagné!! Johnny n'avait aucune chance...")
            victoire_joueur += 1

        if choix_joueur1 in pierre and choix_IA in pierre or choix_joueur1 in feuille and choix_IA in feuille or choix_joueur1 in ciseaux and choix_IA in ciseaux :
            print(f"Johnny a aussi joué {choix_IA}! Egalité!! C'EST UN COMBAT DE TITAAAAAANS!!!")

        print(f"{victoire_johnny} pour Johnny, {victoire_joueur} pour vous!!")
        

        if victoire_joueur >= 2 :
            print("BRAVO VOUS AVEZ VAINCU L'IMBATTABLE JOHNNY, vous avez gagné un briquet et des dictionnaires Larousse.")
            break
    
        if victoire_johnny >= 2 :
            print("MON DIEU JOHNNY REMPORTE UNE VICTOIRE DE PLUS, il est tout simplement ingwackable.")
            break
    return victoire_johnny and victoire_joueur
