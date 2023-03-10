from tkinter import *
from tkinter import Tk, ttk

#----------Cores---------------
cor0 = "#f0f3f5"  #black
cor1 = "#feffff"  #withe
cor2 = "#3fb5a3"  #green
cor3 = "#38576b"  #valor
cor4 = "#403d3d"  #letra

#--------frame----------------
janela = Tk()
janela.title('')
janela.geometry('310x300')
janela.configure(background=cor1)
janela.resizable(width=FALSE, height=FALSE)

#----------Dividindo a janela----------
Frame_cima = Frame(janela, width=310, height=50, bg=cor1, relief='flat')
Frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

Frame_baixo = Frame(janela, width=310, height=250, bg=cor1, relief='flat')
Frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)




janela.mainloop()


