import tkinter as tk
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def seguidores():
    usuario = user.get()
    senha = password.get()
    pessoa = link.get()
    numero = int(num.get())

    # Entrando no Instagram
    navegador = webdriver.Chrome()
    navegador.get('https://www.instagram.com/')
    time.sleep(3)

    # Fazendo login no instagram
    navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(usuario)
    time.sleep(2)
    navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(senha)
    time.sleep(2)
    navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()

    # acessando os seguidores da outra pessoa
    time.sleep(3)
    navegador.get(pessoa)
    time.sleep(2)
    navegador.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div').click()

    # Seleciona o popup e desce com o scroll
    time.sleep(5)
    fBody = navegador.find_element_by_xpath("//div[@class='isgrP']")
    scroll = 0
    while scroll < 1:
        navegador.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
        scroll += 1

    # Clica nos botões de seguir
    for item in range(numero):
        followButton = navegador.find_element_by_class_name("sqdOP.L3NKy.y3zKF")
        followButton.click()
        navegador.find_element_by_xpath('/html/body/div[6]/div/div/div/div[1]/div/div[3]/div/button').click()
        time.sleep(3)
        navegador.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div').click()
        time.sleep(2)

# Tela do tKinter
janela = tk.Tk()
janela.title("Coloque seus dados abaixo para funcionamento do robo")

label_user = tk.Label(janela, text="Usuario do Instagram")
label_user.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)
user = tk.Entry(janela)
user.grid(row=1, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)

label_password = tk.Label(janela, text="Senha do Instagram")
label_password.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)
password = tk.Entry(janela)
password.grid(row=2, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)

label_link = tk.Label(janela, text="Link")
label_link.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)
link = tk.Entry(janela)
link.grid(row=3, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)

label_num = tk.Label(janela, text="Quantas pessoas seguir?")
label_num.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)
num = tk.Entry(janela)
num.grid(row=4, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)

botao = tk.Button(janela, text="Buscar seguidores", command=seguidores)
botao.grid(row=5, column=1, padx=10, pady=10, sticky='nswe', columnspan=4)
janela.mainloop()
