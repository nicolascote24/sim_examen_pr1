import random

#ON/OFF pour arrêter le programme
programme_jeu = True

print("+---------------------------------------------------+")
print("| Examen pratique 1 introduction à la programmation |")
print("| bienvenue dans le programme éducatif de mini-jeux |")
print("+---------------------------------------------------+")

#boucle jusqu'à ce que l'utilisateur quitte
while programme_jeu == True:
    #impression du menu pincipal à chaque tour
    print("-----------------------------------------------------")
    print("voici les mini-jeux")
    print("(0) la devinette [10 pts]")
    print("(1) Lancé de dés [15 pts]")
    print("(2) course de cheval [15 pts]")
    print("(3) Jeu de la moyenne [25 pts]")
    print("(4) Chasse au dragon [25 pts] ")
    print("(5) Roche-papier-siceaux [10pts]")
    print("(6) quitter")
    #choix de l'utilisateur
    choix_jeu = int(input("choissez un mini-jeu : "))
    print("-----------------------------------------------------")
    
    #différentes options de jeux dans le match case
    match choix_jeu:
        case 0 :
            print("jeu la devinette")
            #mettre votre code en-dessous du commentaire
        case 1:
            print("jeu du lancé de dés")
            #mettre votre code en-dessous du commentaire
        case 2:
            print("jeu course de cheval")
            #mettre votre code en-dessous du commentaire     
        case 3:
            print("jeu de la moyenne")
            #mettre votre code en-dessous du commentaire
        case 4:
            print("jeu la chasse au dragon")
            vie_dragon = 45
            vie_joueur = 30
            #mettre votre code en-dessous du commentaire
        case 5:
            print("roche-papier-siceaux")
            #mettre votre code en-dessous du commentaire
        case 6:
            #Sortie de la boucle en mettant à OFF (FALSE)
            print("vous quittez le programme")
            programme_jeu = False
                    
            
            
            
            
            