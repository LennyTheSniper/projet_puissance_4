#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
# MI TD1                                                #
# Zachary MARIANI                                       #
# Lenny BARBE                                           #
# William BRASSART                                      #
# https://github.com/LennyTheSniper/projet_puissance_4  #
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

############ IMPORTATION DES MODULES #############

from glob import glob
import tkinter as tk
import random as rd

############### VARIABLES GLOBALES ###############

# Les dimentions en pixels du canvas du jeu
CANVAS_HEIGHT, CANVAS_WIDTH = 600, 700
# Les dimentions en pixels du petit écran au dessus du jeu
CANVAS2_HEIGHT, CANVAS2_WIDTH = 75, 700
# Les dimentions en pixels de l'ecran du score
SCORE_HEIGHT, SCORE_WIDTH = 400, 200
# Les dimentions de la grille de jeu en cases
grid_height, grid_width = 6, 7
# Le nombre de cases à aligner avant de gagner
alignement = 4
# Calcule la taille d'une case en fonction de parametres mentionnés avant
taille_case_height, taille_case_width = CANVAS_HEIGHT/grid_height, CANVAS_WIDTH/grid_width
# Couleur d'une case en jeu en fonction de si elle appartien eu joueur X 
#                    0         1         2
liste_couleur = ["#FFFFFF","#FF0000","#FFFF00"]
# Choisis un joueur aléatoirement
player = rd.randint(1,2)
# Setup variables utile a certaines fontions
Win = 0 ; coups = []
win1 = 0
win2 = 0
# Création d'un plateau vide
plateau = [[0]*grid_width for j in range (grid_height)]

################### FONCTIONS ####################

# Création des différents canvas
root = tk.Tk()
root.title("Puissance 4")
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="#2B2FDD")
canvas2 = tk.Canvas(root, width=CANVAS2_WIDTH, height=CANVAS2_HEIGHT, bg="#000000")

def affiche_joueur():
    # Ce programe gère l'affichage du second écran en fonction de l'état de la partie
    global player, win1, win2
    canvas2.delete("text")
    if Win == 1:
        title_text = canvas2.create_text(CANVAS2_WIDTH//2, CANVAS2_HEIGHT//2, text="Joueur 1 a gagné!", fill="#FF0000", font="Helvetica 30 bold", tag="text")
        win1 += 1
        score()
    elif Win == 2:
        title_text = canvas2.create_text(CANVAS2_WIDTH//2, CANVAS2_HEIGHT//2, text="Joueur 2 a gagné!", fill="#FFFF00", font="Helvetica 30 bold", tag="text")
        win2 += 1
        score()
    elif Win == -1:
        title_text = canvas2.create_text(CANVAS2_WIDTH//2, CANVAS2_HEIGHT//2, text="Égalité", fill="#D8D8D8", font="Helvetica 30 bold", tag="text")
    elif player == 1:
        title_text = canvas2.create_text(CANVAS2_WIDTH//2, CANVAS2_HEIGHT//2, text="Au tour du joueur 1", fill="#FF8080", font="Helvetica 30 bold", tag="text")
    elif player == 2:
        title_text = canvas2.create_text(CANVAS2_WIDTH//2, CANVAS2_HEIGHT//2, text="Au tour du joueur 2", fill="#FFFF80", font="Helvetica 30 bold", tag="text")
affiche_joueur()

def win_detect():
    global plateau, Win
    # Ce programme vérifie toutes les directions sur toutes les cases si un joueur a aligné assez de pions + si il y a égalité
    # Check Horizontal
    for x in range(grid_width-(alignement-1)):
        for y in range(grid_height):
            check = 0
            for z in range(alignement):
                if plateau[y][x+z] != player:
                    check = 1
            if check == 0:
                Win = player
                break
    # Check Vertical
    for x in range(grid_width):
        for y in range(grid_height-(alignement-1)):
            check = 0
            for z in range(alignement):
                if plateau[y+z][x] != player:
                    check = 1
            if check == 0:
                Win = player
                break
    # Check Diagonal /
    for x in range(grid_width-(alignement-1)):
        for y in range(grid_height-(alignement-1)):
            check = 0
            for z in range(alignement):
                if plateau[y+z][x+z] != player:
                    check = 1
            if check == 0:
                Win = player
                break
    # Check Diagonal \
    for x in range(grid_width-(alignement-1)):
        for y in range((alignement-1), grid_height):
            check = 0
            for z in range(alignement):
                if plateau[y-z][x+z] != player:
                    check = 1
            if check == 0:
                Win = player
                break
    # Check Egalité
    check = 0
    for x in range(grid_width):
        for y in range(grid_height):
            if plateau[y][x] == 0:
                check = 1
    if check == 0:
        Win = -1

def quadrillage():
    # Ce programme dessine le quadrillage de la grille de jeu pour une meilleure visibilité
    x = 0
    y = 0
    for i in range(max(grid_width,grid_height)+1):
        canvas.create_line(x, 0, x, y+CANVAS_HEIGHT, fill="#1012A2", width = 2)
        canvas.create_line(0, y, x+CANVAS_WIDTH, y, fill="#1012A2", width = 2)
        x += taille_case_width
        y += taille_case_height
quadrillage()

def affichage_couleur_quadrillage():
    # Ce programme dessine les jetons sur le canvas en fonction de quel joueur occupe quelle case
    canvas.delete("jetons")
    for x in range(grid_width):
        for y in range(grid_height):
            canvas.create_oval(x*taille_case_width+int(taille_case_width/20),
                                y*taille_case_height+int(taille_case_height/20),
                                (x+1)*taille_case_width-int(taille_case_width/20),
                                (y+1)*taille_case_height-int(taille_case_height/20),
                                fill=liste_couleur[plateau[y][x]],tag="jetons")
affichage_couleur_quadrillage()

def plateau_vide():
    # Ce programme permet de recommencer une partie de 0
    global plateau, player, Win, coups
    plateau = [[0]*grid_width for j in range (grid_height)]
    player = rd.randint(1,2)
    coups = []
    Win = 0
    affiche_joueur()
    affichage_couleur_quadrillage()
plateau_vide()

def click(event):
    # Ce programme est appelé quand on clique sur le canvas de jeu, vérifie quelle collone du plateau on a cliqué,
    # ajoute un pion à l'emplacement correct, et enregistre le coup dans une liste
    global player, grid_height, plateau
    colone_click=int(event.x // taille_case_width)
    loop = 1
    y = 0
    while loop == 1:
        if Win == 0:
            if y == grid_height or (plateau[y][colone_click] != 0):
                if y != 0:
                    plateau[y-1][colone_click] = player
                    coups.append(colone_click)
                    win_detect()
                    affichage_couleur_quadrillage()
                    if player == 1:
                        player = 2
                    else:
                        player = 1
                    loop = 0
                    affiche_joueur()
                else:
                    break
            y += 1
        else:
            loop = 0

def undo ():
    # Ce programme permet d'annulé un coup si le jeu le permet
    global coups, plateau, player, Win
    if Win == 0:
        if coups != []:
            for y in range (grid_height):
                if plateau[y][coups[-1]] != 0:
                    plateau[y][coups[-1]] = 0
                    coups = coups[:-1]
                    if player == 1:
                        player = 2
                    else:
                        player = 1
                    affichage_couleur_quadrillage()
                    affiche_joueur()
                    break

def sauvegarde():
    # Ce programme enregistre l'état de la partie dans un fichier secondaire
    fic = open ("sauvegarde", "w")
    fic.write(str(player)+"\n"+str(grid_height)+"\n"+str(grid_width)+"\n")
    for j in range (grid_height):
        for i in range (grid_width):
            fic.write(str(plateau[j][i])+" ")
    fic.close()

def charge():
    # Ce programme charge l'état de la partie depuis un fichier secondaire
    global grid_height, grid_width, plateau, player, coups
    fic = open ("sauvegarde", "r")
    loop = 0 
    while True:
        loop += 1
        ligne = fic.readline()
        if ligne == "":
            affichage_couleur_quadrillage()
            win_detect()
            affiche_joueur()
            coups = []
            break
        else:
            if loop == 1:
                player = int(ligne)
            elif loop == 2:
                grid_height = int(ligne)
            elif loop == 3:
                grid_width = int(ligne)
            else:
                split = ligne.split()
                for i in range (grid_width):
                    for j in range (grid_height):
                        plateau[j][i] = int(split[i+j*grid_width])

def score(): 
    global Win, win1, win2
    compteur_win1['text'] = str(win1)
    compteur_win2['text'] = str(win2)
    plateau_vide()

def restart():
    global win1, win2
    plateau_vide()
    win1, win2 = 0, 0
    score()

def set_match(): 
    pass

############# LISTE DE TOUS LES BOUTONS ############

# Enregistre les boutons "Sauvegarde", "Charger une sauvegarde", "Annuler", "Reset" et "Restart"
sauvegarder = tk.Button(root, text = "Sauvegarde", command = sauvegarde, bg = 'grey')
charger = tk.Button(root, text = "Charger une sauvegarde", command = charge, bg = 'grey')
undo = tk.Button(root, text = "Annuler", command = undo, bg = 'grey')
reset = tk.Button(root, text = "Reset", command = plateau_vide, bg = 'grey')
restart = tk.Button(root, text = "Restart", command = restart, bg = 'grey')

############## CREATION DE LA FENETRE #############

# espacements
espacement_horizon = tk.Canvas(root, width=100, height=1, bg="white")
espacement_horizon.grid (row=0, column=6)

# Compteurs de points 
compteur_win1 = tk.Label(root, text=0, font=("Arial", 52), fg='#FF0000')
compteur_win2 = tk.Label(root, text=0, font=("Arial", 52), fg='#FFF000')
compteur_win1.grid (row=2,column=6)
compteur_win2.grid (row=3,column=6)
# Place les canvas en jeu
canvas.grid(row=1, column=0, columnspan=5, rowspan=4)
canvas2.grid(row=0, column=0, columnspan=5)
# Place les boutons en jeu
sauvegarder.grid(row=5, column=0)
charger.grid(row=5, column=3)
undo.grid(row=5, column=1)
reset.grid(row=5, column=2)
restart.grid(row=5, column=6)
# Créée le lien entre un clic gauche sur le canvas principal et le fonction "click"
canvas.bind('<Button-1>',click)
# Check constant des inputs du joueur
root.mainloop()