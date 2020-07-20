from tkinter import *
vtn=Tk()
vtn.title("Imagen en tkinter")
vtn.geometry("540x560")
vtn.iconbitmap("logo.ico")
imagen=PhotoImage(file="Happy.PNG")
fondo=Label(vtn,image=imagen).place(x=0,y=0)
vtn.mainloop()