###################
# MI TD1
# Zachary MARIANI
# Lenny BARBE
# William BRASSART
# https://github.com/LennyTheSniper/projet_puissance_4
###########################################

############ IMPORTATION DES MODULES #############

from glob import glob
import tkinter as tk
import random as rd

############### VARIABLES GLOBALES ###############

CANVAS_HEIGHT, CANVAS_WIDTH = 600, 700
CANVAS2_HEIGHT, CANVAS2_WIDTH = 75, 700
grid_height, grid_width = 6, 7
taille_case_height, taille_case_width = CANVAS_HEIGHT/grid_height, CANVAS_WIDTH/grid_width
#                    0         1         2
liste_couleur = ["#FFFFFF","#FF0000","#FFFF00"]
player = rd.randint(1,2)
Win = 0 ; coups = []

################### FONCTIONS ####################

root = tk.Tk()
root.title("Puissance 4")
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="#2B2FDD")
canvas2 = tk.Canvas(root, width=CANVAS2_WIDTH, height=CANVAS2_HEIGHT, bg="#000000")

def affiche_joueur():
    global player
    canvas2.delete("text")
    if Win == 1:
        title_text = canvas2.create_text(CANVAS2_WIDTH//2, CANVAS2_HEIGHT//2, text="Joueur 1 a gagné!", fill="#FF0000", font="Helvetica 30 bold", tag="text")
    elif Win == 2:
        title_text = canvas2.create_text(CANVAS2_WIDTH//2, CANVAS2_HEIGHT//2, text="Joueur 2 a gagné!", fill="#FFFF00", font="Helvetica 30 bold", tag="text")
    elif Win == -1:
        title_text = canvas2.create_text(CANVAS2_WIDTH//2, CANVAS2_HEIGHT//2, text="Égalité", fill="#D8D8D8", font="Helvetica 30 bold", tag="text")
    elif player == 1:
        title_text = canvas2.create_text(CANVAS2_WIDTH//2, CANVAS2_HEIGHT//2, text="Au tour du joueur 1", fill="#FF8080", font="Helvetica 30 bold", tag="text")
    elif player == 2:
        title_text = canvas2.create_text(CANVAS2_WIDTH//2, CANVAS2_HEIGHT//2, text="Au tour du joueur 2", fill="#FFFF80", font="Helvetica 30 bold", tag="text")

def plateau_vide():
    global plateau, player
    plateau = [[0]*grid_width for j in range (grid_height)]
    player = rd.randint(1,2)
plateau_vide()
affiche_joueur()

def win_detect():
    global plateau, Win
    # Check Horizontal
    
    for x in range(grid_width-3):
        for y in range(grid_height):
            if plateau[y][x] == player and plateau[y][x+1] == player and plateau[y][x+2] == player and plateau[y][x+3] == player:
                Win = player
                break
    # Check Vertical
    for x in range(grid_width):
        for y in range(grid_height-3):
            if plateau[y][x] == player and plateau[y+1][x] == player and plateau[y+2][x] == player and plateau[y+3][x] == player:
                Win = player
                break
    # Check Diagonale /
    for x in range(grid_width-3):
        for y in range(grid_height-3):
            if plateau[y][x] == player and plateau[y+1][x+1] == player and plateau[y+2][x+2] == player and plateau[y+3][x+3] == player:
                Win = player
                break
    # Check Diagonale \
    for x in range(grid_width-3):
        for y in range(3, grid_height):
            if plateau[y][x] == player and plateau[y-1][x+1] == player and plateau[y-2][x+2] == player and plateau[y-3][x+3] == player:
                Win = player
                break
    # Check Egalité
    check_deux = 0
    for x in range(grid_width):
        for y in range(grid_height):
            if plateau[y][x] == 0:
                check_deux = 1
    if check_deux == 0:
        Win = -1





def quadrillage():
    x = 0
    y = 0
    for i in range(max(grid_width,grid_height)+1):
        canvas.create_line(x, 0, x, y+CANVAS_HEIGHT, fill="#1012A2", width = 2)
        canvas.create_line(0, y, x+CANVAS_WIDTH, y, fill="#1012A2", width = 2)
        x += taille_case_width
        y += taille_case_height
quadrillage()

def affichage_couleur_quadrillage():
    canvas.delete("jetons")
    for x in range(grid_width):
        for y in range(grid_height):
            canvas.create_oval(x*taille_case_width+int(taille_case_width/20),
                                y*taille_case_height+int(taille_case_height/20),
                                (x+1)*taille_case_width-int(taille_case_width/20),
                                (y+1)*taille_case_height-int(taille_case_height/20),
                                fill=liste_couleur[plateau[y][x]],tag="jetons")
affichage_couleur_quadrillage()

def click(event):
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
    global coups, plateau, player
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



def sauvegarde () : 
    fic = open ("sauvegarde", "w")
    fic.write(str(player)+"\n"+str(grid_height)+"\n"+str(grid_width)+"\n")
    for j in range (grid_height):
        for i in range (grid_width):
            fic.write(str(plateau[j][i])+" ")
    fic.close()


def charge():
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













############# LISTE DE TOUS LES BOUTONS ############
sauvegarder = tk.Button(root, text = "Sauvegarde", command = sauvegarde, bg = 'grey')
charger = tk.Button(root, text = "Charger une sauvegarde", command = charge, bg = 'grey')
undo = tk.Button(root, text = "Annuler", command = undo, bg = 'grey')

############## CREATION DE LA FENETRE #############

canvas.grid(row=1, column=0, columnspan=3)
canvas2.grid(row=0, column=0, columnspan=3)
sauvegarder.grid(row=2, column=0)
charger.grid(row=2, column=2)
undo.grid(row=2, column=1)
canvas.bind('<Button-1>',click)
root.mainloop()