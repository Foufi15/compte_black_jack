from customtkinter import *

def Buttonevent():
    print("Hello world")

app = CTk()
app.geometry("1000x600")
app.title("Black jack")
app._set_appearance_mode("system")

# frame= CTkFrame(master=app)
# frame.pack(expand="True")

# Configuration du nombre de colone avec grid_columncongigure (numero, poid (multiplicateur de taille))
for i in range(5):
    app.grid_columnconfigure(i,weight=1)

# Configuration du nombre de ligne avec grid_columncongigure (numero, poid (multiplicateur de taille))
for j in range(5):
    app.grid_rowconfigure(j,weight=1)

texte_explication_comptage="Compter les cartes au blackjack est une technique utilisée\n" \
" pour suivre la proportion de cartes hautes et basses restantes dans le sabot.\n " \
"L'objectif est de savoir quand les chances sont en faveur du joueur. \n" \
"La méthode la plus connue est le système Hi-Lo, qui attribue une valeur à chaque carte :\n " \
"+1 pour les cartes basses (2 à 6), \n" \
"0 pour les cartes neutres (7 à 9), \n" \
"et -1 pour les cartes hautes (10, Valet, Dame, Roi, As).\n " \
"En ajoutant ou soustrayant ces valeurs à chaque carte distribuée, on maintient un compte courant.\n " \
"Un compte positif indique qu'il reste plus de cartes hautes, ce qui est favorable au joueur car cela augmente les chances de faire un blackjack.\n " \
"À l’inverse, un compte négatif signifie qu’il reste plus de cartes basses, ce qui avantage le croupier. \n" \
"Pour être encore plus précis, on peut convertir ce compte en true count en le divisant par le nombre de jeux de cartes restants. \n" \
"La clé de cette stratégie est la discrétion, la concentration et une bonne mémoire. \n" 


titre=CTkLabel(app, text="COMMENT CONTER AU BLACK JACK")
titre.grid(row=0,column=2, sticky="")

tst=CTkLabel(app, text=f"{texte_explication_comptage}")
tst.grid(row=1, column=1, columnspan=3,rowspan=3,sticky="ew")

jt=CTkButton(app, text="Jouer", command=Buttonevent)
jt.grid(row=4, column=1, columnspan=3, sticky="ew")

app.mainloop()