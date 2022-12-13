#imports
from tkinter import *
from tkinter import messagebox

#funcoes dos botoes 
def saudacao(event=None):
   messagebox.showinfo("Insert","Registro efetuado com sucesso!!!")

def excluir(event=None):
   messagebox.askyesno("Delete","Deseja Excluir os dados?")


window = Tk()
window.title('Copa do Mundo')

#chamada das opcoes 
variable = StringVar()
gender = ('A', 'B', 'C', 'D')
variable.set(gender[0])

#Principal


window.geometry('940x800')
window.config(bg='#f7ef38')


# widgets
left_frame = Frame(window, bd=3, relief=SOLID, padx=80, pady=24)

#inputs
Label(left_frame, text="Digite o nome da equipe", font=('Times', 14)).grid(row=0, column=0, sticky=W, pady=10)
Label(left_frame, text="Partidas vencidas ", font=('Times', 14)).grid(row=1, column=0, pady=10)
Label(left_frame, text="Quantidade de gols", font=('Times', 14)).grid(row=2, column=0, pady=10)
Label(left_frame, text="Grupo", font=('Times', 14)).grid(row=6, column=0, sticky=W, pady=10)

#atribuicoes dos inputs e configs
log_eq = Entry(left_frame, font=('Times', 14))
log_te = Entry(left_frame, font=('Times', 14))
log_ar = Entry(left_frame, font=('Times', 14))
log_ge = OptionMenu(left_frame, variable, *gender)

#botoes
confirmar_btn = Button(left_frame, width=10, text='Cadastrar', font=('Times', 14), command=saudacao)
excluir_btn = Button(left_frame, width=10, text='Excluir', font=('Times', 14), command=excluir)
editar_btn = Button(left_frame, width=10, text='Editar', font=('Times', 14), command=None)

# widgets config
log_eq.grid(row=0, column=1, pady=17, padx=20)
log_te.grid(row=1, column=1, pady=10, padx=20)
log_ar.grid(row=2, column=1, pady=10, padx=20)
log_ge.grid(row=6, column=1, pady=10, padx=20)

#botopes config
confirmar_btn.grid(row=11, column=4, pady=10, padx=25)
excluir_btn.grid(row=11, column=8, pady=10, padx=23)
editar_btn.grid(row=11, column=9, pady=10, padx=20)

left_frame.place(x=200, y=230)




if __name__ == '__main__':
    window.mainloop()