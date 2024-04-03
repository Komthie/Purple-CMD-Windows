import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import os
from tkinter.ttk import *
from time import strftime

def execute_command():
    user_command = entry2.get()
    output = os.popen(user_command).read()

    txt.delete('1.0', 'end')
    txt.insert('1.0', output)



# Crie a janela principal
painel = tk.Tk()
painel.geometry('550x350')
painel.title('cmd version=anime')
painel.configure(background='#16141a')
painel.resizable(False, False)
painel.iconbitmap('C:/Users/PEDRO MORAES/Downloads/brand_hello_kitty_icon_158867.ico')


path = 'C:/Users/PEDRO MORAES/Downloads/eye.jpg'
path2 = 'C:/Users/PEDRO MORAES/Downloads/k3.png'

img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(painel, image=img)
panel.pack(side="bottom", fill="both", expand="yes")

img2 = ImageTk.PhotoImage(Image.open(path2))
panel = tk.Label(painel, image=img2)
panel.place(x=510, y=5)

fontecust = font.Font(family="Courier", size=8)
fontecust2 = font.Font(family="Courier", size=13)
fontecust3 = font.Font(family="Courier", size=8)


# Crie o botão
botao = tk.Button(highlightthickness=5, text='COMMAND', font=fontecust, height=1, cursor="hand2", command=execute_command, borderwidth=3)
botao.config(highlightbackground="#180147", highlightcolor="#180147", background='black', foreground='#DF7CFA')
botao.place(x=5, y=6)

# Crie o campo de entrada
entry2 = tk.Entry(painel, width=41, borderwidth=7, background='black', foreground='#DF7CFA', font=fontecust2)
entry2.place(x=80, y=5)


txt = tk.Text(painel, height=10, width=50, borderwidth=5, bg='black', foreground='pink')
txt.place(x=80, y=110)

#Crie coded by komthe
coded = tk.Label(painel, text='coded by Komthe', background='black', font=fontecust3, foreground='#DF7CFA', cursor='hand2')
coded.place(x=435, y=330)







painel.mainloop()
