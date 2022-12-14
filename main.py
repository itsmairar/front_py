import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = tk.Tk()

imagem = tk.PhotoImage(file="image.png")
w = tk.Label(root, image=imagem)
w.imagem = imagem
w.pack()

#funcoes dos botoes 
def saudacao(event=None):
   messagebox.showinfo("Insert","Registro efetuado com sucesso!!!")

def excluir(event=None):
   messagebox.askyesno("Delete","Deseja Excluir os dados?")



root.title('Copa do Mundo')

#Principal


root.geometry('940x800')




# inputs
left_frame = Frame(root, bd=3, relief=SOLID, padx=80, pady=24)

Label(left_frame, text="Digite o nome da equipe", font=('Times', 14)).grid(row=0, column=0, sticky=W, pady=10)
Label(left_frame, text="Digite o nome do técnico", font=('Times', 14)).grid(row=1, column=0, pady=10)
Label(left_frame, text="Digite o nome do árbitro", font=('Times', 14)).grid(row=2, column=0, pady=10)

#atribuicoes dos inputs e config
log_eq = Entry(left_frame, font=('Times', 14))
log_te = Entry(left_frame, font=('Times', 14))
log_ar = Entry(left_frame, font=('Times', 14))

#botoes 
confirmar_btn = Button(left_frame, width=10, text='Cadastrar', font=('Times', 14), command=saudacao)
excluir_btn = Button(left_frame, width=10, text='Excluir', font=('Times', 14), command=excluir)
editar_btn = Button(left_frame, width=10, text='Editar', font=('Times', 14), command=None)

# widgets config
log_eq.grid(row=0, column=1, pady=10, padx=20)
log_te.grid(row=1, column=1, pady=10, padx=20)
log_ar.grid(row=2, column=1, pady=10, padx=20)

#config botoes
confirmar_btn.grid(row=3, column=2, pady=10, padx=25)
excluir_btn.grid(row=3, column=0, pady=10, padx=23)
editar_btn.grid(row=3, column=1, pady=10, padx=20)

left_frame.place(x=420, y=300)


if __name__ == '__main__':
    root.mainloop()



root.mainloop()