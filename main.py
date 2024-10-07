from customtkinter import *
import random
import string

window = CTk(fg_color='#1F1F1F')
window._set_appearance_mode('dark')
window.title("Gerador de Senha")
window.iconbitmap(r'key.ico')
window.geometry("300x350")
window.resizable(False, False)

def windowPosition():
    window.update()
    screenX = window.winfo_screenwidth()
    screenY = window.winfo_screenheight()
    WindowX = window.winfo_width()
    WindowY = window.winfo_height()
    PosX = (screenX//2) - (WindowX//2)
    PosY = (screenY//2) - (WindowY//2)
    window.geometry(f"{WindowX}x{WindowY}+{PosX}+{PosY}")
windowPosition()

allCharc =  string.ascii_letters + string.hexdigits + string.punctuation
def criaSenha():
    resultado.configure(state=NORMAL)
    resultado.configure(justify="center")
    Senha = ''
    number = Input.get()
    if number.isdigit() == False:
        Input.delete(0, END)
        resultado.delete(0,END)
        resultado.insert(0,'VALOR INVALIDO')
        resultado.configure(text_color="red" )
        return
    else:
        resultado.configure(text_color="white" )
        number = int(Input.get())
        if number > 50:
            Input.delete(0,END)
            Input.insert(0, 49)
            resultado.delete(0,END)
        else:
            for N in range(number):
                number = int(Input.get())
                Senha += random.choice(allCharc)
            resultado.configure(justify="center")
            resultado.delete(0,END)
            Input.delete(0, END)
            resultado.insert(0,Senha)
            resultado.configure(state='readonly')

Title = CTkLabel(window, text="Gerador de Senhas", font=("Arial", 20), bg_color='#1F1F1F',text_color='white')
Title.pack(side="top", pady="20")

Label = CTkLabel(window, text="Quantos caracteres  sua senha deve ter?", font=("Arial",15),bg_color='#1F1F1F',text_color='white')
Label.pack(pady="20")

Input = CTkEntry(window, placeholder_text="Digite aqui...",justify="center",bg_color='#1F1F1F', fg_color='#1F1F1F', text_color='white')
Input.pack(pady=20)

button =  CTkButton(window, text="Gerar Senha", command=criaSenha,bg_color='#1F1F1F')
button.pack()

resultado = CTkEntry(window,width=200,bg_color="#1F1F1F",fg_color="#242424")
resultado.configure(state='readonly') 
resultado.pack(pady=40)

window.mainloop()