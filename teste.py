from customtkinter import *

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

tst=CTkLabel(app, text="Nom")
tst.grid(row=0, column=1, sticky="")

ls=CTkLabel(app, text="Prenom")
ls.grid(row=0, column=3, sticky="")

jt=CTkButton(app, text="appuyer")
jt.grid(row=4, column=1, columnspan=3, sticky="ew")

box1 = CTkEntry(master=app, placeholder_text="nom").grid(row=2,column=1, sticky="")
box2 = CTkEntry(master=app, placeholder_text="prenom").grid(row=2,column=3, sticky="")


app.mainloop()