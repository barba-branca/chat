import os

def processar_resposta (resposta,nome):
    if resposta == "1":
         print(f"{os.linesep}{nome} hjfdkjhf{os.linesep}")
        
    elif resposta == "2":
         print(f"{os.linesep}{nome} hjfdkjhf{os.linesep}")
    elif resposta == "3":
         print(f"{os.linesep}{nome} hjfdkjhf{os.linesep}")
    elif resposta == "4":
         print(f"{os.linesep}{nome} hjfdkjhf{os.linesep}")
    else:
        print("Digite apenas 1, 2, 3 ou 4")


def start():
# Apresentar o chatbot
    print ("Olá! Benvindo a MyLove.com.br")
# Pedir o nome
nome = input("digite o seu nome:")
# Pedir o e-mail
email = input("digite o seu email:")
while True:
# Oferecer o menu de opções
    resposta =input("f O que gostaria de saber hoje?{os.linesep}
        [1] - Vale a pena aprender Python?{os.linesep}
        [2] - Quanto tempo leva para conseguir um emprego com Python?{os.linesep}
        [3] - Quanto vou saber que estou BOM O suficiente para conseguir um emprego?{os.linesep}
        [4] - Onde me recomenda estudar Python para conseguir um emprego?{os.linesep})"
    # Processar a resposta enviada
    processar_resposta(resposta, nome)
    if_name_=='_main_'
    start()