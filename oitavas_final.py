#imports
import tkinter as tk
from tkinter import *
from tkinter import messagebox
 
window = tk.Tk()

window.title('Copa do mundo')
window.geometry('500x300')
window.configure(background="#ffffff")

#w = oeste
Label(window,text='Cadastro das oitavas de final', background='#ffffff', foreground='#009', anchor=W).place(x=10, y=10, width=200, height=30)

# imagem = tk.PhotoImage(file="image.png")
# w = tk.Label(window, image=imagem)
# window.configure(background='white')
# window.attributes('-alpha', 0.9)
# w.imagem = imagem
# w.pack()

#funcoes dos botoes 
def saudacao(event=None):
   messagebox.showinfo("Insert","Registro efetuado com sucesso!!!")

def excluir(event=None):
   messagebox.askyesno("Delete","Deseja Excluir os dados?")


window.title('Copa do Mundo')

#chamada das opcoes 
variable = StringVar()
gender = ('A', 'B', 'C', 'D')
variable.set(gender[0])

#Principal


window.geometry('940x800')



# widgets
left_frame = Frame(window, bd=3, relief=SOLID, padx=80, pady=24)

#inputs
Label(left_frame, text="Digite o código da equipe", font=('Times', 14)).grid(row=0, column=0, sticky=W, pady=10)
Label(left_frame, text="Digite o nome da equipe", font=('Times', 14)).grid(row=1, column=0, sticky=W, pady=10)
Label(left_frame, text="Gols da equipe titular ", font=('Times', 14)).grid(row=2, column=0, pady=10)
Label(left_frame, text="Nome da equipe oponente", font=('Times', 14)).grid(row=3, column=0, pady=10)
Label(left_frame, text="Gols da equipe oponente", font=('Times', 14)).grid(row=4, column=0, pady=10)
Label(left_frame, text="Local", font=('Times', 14)).grid(row=5, column=0, pady=10)
Label(left_frame, text="Data", font=('Times', 14)).grid(row=6, column=0, pady=10)
Label(left_frame, text="Grupo", font=('Times', 14)).grid(row=7, column=0, sticky=W, pady=10)

#atribuicoes dos inputs e configs
log_co = Entry(left_frame, font=('Times', 14))
log_eq = Entry(left_frame, font=('Times', 14))
log_te = Entry(left_frame, font=('Times', 14))
log_ar = Entry(left_frame, font=('Times', 14))
log_op = Entry(left_frame, font=('Times', 14))
log_lc = Entry(left_frame, font=('Times', 14))
log_dt = Entry(left_frame, font=('Times', 14))
log_ge = OptionMenu(left_frame, variable, *gender)


#botoes
confirmar_btn = Button(left_frame, width=10, text='Cadastrar', font=('Times', 14), command=saudacao)
excluir_btn = Button(left_frame, width=10, text='Excluir', font=('Times', 14), command=excluir)
editar_btn = Button(left_frame, width=10, text='Editar', font=('Times', 14), command=None)

# widgets config
log_co.grid(row=0, column=1, pady=10, padx=20)
log_eq.grid(row=1, column=1, pady=10, padx=20)
log_te.grid(row=2, column=1, pady=10, padx=20)
log_ar.grid(row=3, column=1, pady=10, padx=20)
log_op.grid(row=4, column=1, pady=10, padx=20)
log_lc.grid(row=5, column=1, pady=10, padx=20)
log_dt.grid(row=6, column=1, pady=10, padx=20)
log_ge.grid(row=7, column=1, pady=10, padx=20)


#botopes config
confirmar_btn.grid(row=11, column=4, pady=10, padx=25)
excluir_btn.grid(row=11, column=8, pady=10, padx=23)
editar_btn.grid(row=11, column=9, pady=10, padx=20)

left_frame.place(x=100, y=130)




if __name__ == '__main__':
    window.mainloop()
