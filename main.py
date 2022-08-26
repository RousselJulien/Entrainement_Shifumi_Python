from config.check import check

#Message de présentation du jeu:

print("=========================================================================================================================")
print("BIENVENUE")
print("Voici la finale du monde du championnat extrême de shifumi Rouennais, en présence ici de ntore champion en titre JOHNNY!!")
print("Préparez vous à l'affrontaire dans un duel en 2 manches gagnantes palpitantes de SHIFUMI!")
print("Attention C'EST PARTI, QUE LA FÊTE COMMENCE!!!")
print("=========================================================================================================================")
print("")

#Lancement de la boucle:

jouer = "o"

#Lancement du jeu:

while jouer == "o" :
    check()
    print("Une p'tite der'?")
    print("")
    jouer = input("o/n : ")
    if jouer != "o" :
        print("")
        print("Très bien! Merci d'avoir joué et à bientôt!!")
        print("=========================================================================================================================")
        break
