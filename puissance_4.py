###################
# MI TD1
# Zachary MARIANI
# Lenny BARBE
# William BRASSART
# https://github.com/LennyTheSniper/projet_puissance_4
###########################################

############ IMPORTATION DES MODULES #############

import tkinter as tk

############### VARIABLES GLOBALES ###############

CANVAS_HEIGHT, CANVAS_WIDTH = 600, 700
grid_height, grid_width = 6, 7
taille_case_height, taille_case_width = CANVAS_HEIGHT/grid_height, CANVAS_WIDTH/grid_width
#                    0         1         2
liste_couleur = ["#FFFFFF","#FF0000","#FFFF00"]

################### FONCTIONS ####################

root = tk.Tk()
root.title("Puissance 4")
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="#2B2FDD")


def plateau_vide():
    global plateau
    plateau = [[0]*grid_width]*grid_height
plateau_vide()
print(plateau)

def quadrillage(grid_height, grid_width):
    x = 0
    y = 0
    for i in range(max(grid_width,grid_height)+1):
        canvas.create_line(x, 0, x, y+CANVAS_HEIGHT, fill="#1012A2", width = 2)
        canvas.create_line(0, y, x+CANVAS_WIDTH, y, fill="#1012A2", width = 2)
        x += taille_case_width
        y += taille_case_height
quadrillage(grid_height, grid_width)

def affichage_couleur_quadrillage(grid_height, grid_width):
    for x in range(grid_width):
        for y in range(grid_height):
            canvas.create_oval(x*taille_case_width+int(taille_case_width/20),
                                y*taille_case_height+int(taille_case_height/20),
                                (x+1)*taille_case_width-int(taille_case_width/20),
                                (y+1)*taille_case_height-int(taille_case_height/20),
                                fill=liste_couleur[plateau[y][x]])
affichage_couleur_quadrillage(grid_height, grid_width)

def click(event):
    print(int(event.x // taille_case_width))



def sauvegarde () : 
    fic = open ("sauvegarde", "w")
    fic.write(str(taille_plateau)+"\n")
    for i in range (taille_plateau):
        for j in range (taille_plateau):
            fic.write(str(plateau[i][j])+" ")
    fic.close()


def charge () :
    global taille_plateau, plateau
    fic = open ("sauvegarde", "r")
    while True:
        ligne = fic.readline()
        if ligne == "":
            affichage_couleur_quadrillage(taille_plateau)
            break
        else:
            if " " not in ligne:
                taille_plateau = int(ligne)
            else:
                split = ligne.split()
                for i in range (taille_plateau):
                    for j in range (taille_plateau):
                        plateau[i][j] = int(split[i*taille_plateau+j])













############# LISTE DE TOUS LES BOUTONS ############
sauvegarder = tk.Button(root, text = "sauvegarder", command = sauvegarde, bg = 'grey')
charger = tk.Button(root, text = "charger une sauvegarde", command = charge, bg = 'grey')


############## CREATION DE LA FENETRE #############

canvas.grid(row=0, column=1, columnspan=2)
sauvegarder.grid(row=1, column=1)
charger.grid(row=1, column=2)
canvas.bind('<Button-1>',click)
root.mainloop()