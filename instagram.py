import tkinter as tk
from tkinter import ttk
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import datetime

lista_tipos = ['Sem Parar','Veloe']
lista_codigos = []

def codigo():
    login = entry_login.get()
    tipo = combobox_meio.get()
    data = datetime.datetime.now()
    data_criacao = data.strftime("%H/%M/%S")
    codigos = len(lista_codigos)+1
    codigo_str = "COD-{}".format(codigos)
    lista_codigos.append((codigo_str, login, tipo, data_criacao))

    texto_login["text"] = lista_codigos

def abrir_janela():
    janela2 = tk.Toplevel()
    janela2.title('Janela nova')
    label_nome = tk.Label(janela2, text="nome")
    label_nome.grid(row=0, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)
    botao3 = tk.Button(janela2, text="Fechar janela", command=janela2.destroy)
    botao3.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

janela = tk.Tk()

janela.title("Informações para o funcionamento do robo")

label_login = tk.Label(janela, text="Usuario")
label_login.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

entry_login = tk.Entry(janela)
entry_login.grid(row=1, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)

combobox_meio = ttk.Combobox(janela, values=lista_tipos)
combobox_meio.grid(row=2, column=1, padx=10, pady=10, sticky='nswe', columnspan=4)

botao = tk.Button(janela, text="Exibir dados", command=codigo)
botao.grid(row=3, column=1, padx=10, pady=10, sticky='nswe', columnspan=4)

texto_login = tk.Label(janela, text="")
texto_login.grid(row=4, column=1, padx=10, pady=10, sticky='nswe', columnspan=4)

botao2 = tk.Button(janela, text="Abrir outra janela", command=abrir_janela)
botao2.grid(row=5, column=1, padx=10, pady=10, sticky='nswe', columnspan=4)

janela.mainloop()

