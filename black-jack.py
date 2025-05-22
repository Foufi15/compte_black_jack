import os
import sys
import pygame 
import random
import time
import tkinter as tk
from tkinter.simpledialog import askinteger
from tkinter.messagebox import askyesno, showinfo
from tkinter.messagebox import showinfo

def recomence(vitesse_ms):
    root = tk.Tk()
    root.withdraw()

    d = askyesno("Fin", "Voulez-vous arrêter ?")
    if d:
        return False, vitesse_ms
    else:
        z = askyesno("Temps", "Voulez-vous changer le temps d'apparition des cartes ?")
        if z:
            y_sec = askinteger("Vitesse", "Nouvelle vitesse (en secondes)")
            if y_sec is not None:
                vitesse_ms = y_sec * 1000  # conversion en millisecondes
        return True, vitesse_ms


# --------- Lancement de la boucle principale ---------
Repet = True
vitesse = 100

while Repet:

    valeurs = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "D", "R"]
    couleurs = ["carreau", "pique", "trefle", "coeur"]
    sup = ["2", "3", "4", "5", "6"]
    inf = ["As", "10", "J", "D", "R"]

    packet = {}
    repertoire_carte = r"../projet"  # assurez-vous que ce chemin est correct
    fichiers_cartes = os.listdir(repertoire_carte)

    for valeur in valeurs:
        for couleur in couleurs:
            nom_fichier = f"{valeur} de {couleur}.jpg"
            carte = os.path.join(repertoire_carte, nom_fichier)
            image_carte = pygame.image.load(carte)
            image_carte = pygame.transform.scale_by(image_carte, 0.50)

            if valeur in sup:
                compte = 1
            elif valeur in inf:
                compte = -1
            else:
                compte = 0

            packet[(valeur, couleur)] = [f"{valeur} de {couleur}", image_carte, compte]

    dec = list(packet.values())
    random.shuffle(dec)

    pygame.init()
    pygame.display.init()
    fenetre = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Affichage des cartes")

    x = 0

    for i in range(random.randint(0, len(dec) - 1)):
        fenetre.fill((255, 255, 255))
        x += dec[i][2]
        image = dec[i][1]
        fenetre.blit(image, image.get_rect(center=fenetre.get_rect().center))
        pygame.display.flip()
        pygame.time.delay(1000 + vitesse)

    pygame.time.delay(1000 + vitesse)
    pygame.display.quit()
    pygame.quit()

    # Demande du résultat utilisateur via tkinter
    root = tk.Tk()
    root.withdraw()
    a = askinteger("Résultat", "À combien est votre compte ?")

    if a == x:
        showinfo("Résultat", "Bravo ! Tu as le bon compte.")
    else:
        showinfo("Résultat", f"Tu as le mauvais compte. Le bon était : {x}")

    time.sleep(1)

    # Redemande si on recommence
    Repet, vitesse = recomence(vitesse)
