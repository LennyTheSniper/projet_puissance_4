# TD de Python L1MIIN101N

Ce TD a été réalisé par:

    Zachary MARIANI
    Lenny BARBE
    William BRASSART

https://github.com/LennyTheSniper/projet_puissance_4


Ce TD en groupe a pour but de recréer le jeu du puissance 4.


Pour démarrer le projet, il faut simplement ouvrir le fichier "puissance_4.py" et appuyer sur la touche F5.
Parfois, il demande avant de commencer de sélectionner une configuration de débuggage. Sélectionnez "Fichier Python" ou "Python File"

Pour jouer, il faut simplement cliquer sur quelle collone votre pion doit se placer.
Il y a un second écran qui indique l'état du jeu (qui doit placer son pion, si qqun a gagné ou si il y a égalité)

Pour customiser une partie, vous pouvez modifier:
    "CANVAS_HEIGHT, CANVAS_WIDTH" (les dimentions en pixels du canvas du jeu) (par défaut = 600, 700)
    "CANVAS2_HEIGHT, CANVAS2_WIDTH" (les dimentions du petit écran au dessus du jeu) (par défaut = 75, 700)
    "grid_height, grid_width" (les dimentions de la grille de jeu en cases) (par défaut = 6, 7)
    "alignement" (le nombre de cases à aligner avant de gagner) (par défaut = 4)

    Merci de ne pas toucher aux autres variables, nous ne garantissons pas que cela fonctionnera en votre faveur.
    Merci de ne pas mettre "alignement" a une valeur plus grande que "grid_height" ou "grid_width", cela rend une partie très difficile voire impossible.
    Nous recommendons aussi de garder "CANVAS_HEIGHT, CANVAS_WIDTH" proportionnels à "grid_height, grid_width", ainsi que de garder "CANVAS_WIDTH" égal à "CANVAS2_WIDTH" pour éviter une distortion du plateau.

Amusez vous! :)