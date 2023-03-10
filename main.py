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



#----------------configurando frame acima---------------------
l_nome = Label(Frame_cima, text='LOGIN', anchor=NE, font=('Ivy 25'), bg=cor1, fg=cor4)
l_nome.place(x=5, y=5)

l_linha = Label(Frame_cima, text='', width=275, anchor=NW, font=('Ivy 1'), bg=cor2, fg=cor4)
l_linha.place(x=10, y=45)


#----------------configurando frame de baixo---------------------
l_nome = Label(Frame_baixo, text='Nome *', anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
l_nome.place(x=10, y=20)

e_nome = Entry(Frame_baixo, width=25, justify='left', font=("", 15),highlightthickness=1, relief='solid')
e_nome.place(x=14, y=50)

















janela.mainloop()


