from ensurepip import version

version = "1.4"

def intro():
    msg = "Assistente = versão {} / Developed by: Samuel Oliveira".format(version)
    print("-" * len(msg) + "\n{}\n".format(msg) + "-" * len(msg))

lista_erros = [
                "Não entendi nada",
                "Desculpe, não entendi",
                "Repita novamente por favor"
                ]

comandos = {
    "desligar": "desligando",
    "reiniciar": "reiniciando"
}

conversas = {
    "Olá": "Oi, tudo bem?",
    "sim e você": "Estou bem, obrigado por perguntar"
}

def verifica_nome(user_name):
    if user_name.startswith("Meu nome é "):
        user_name = user_name.replace("Meu nome é", "")
    if user_name.startswith("Eu me chamo "):
        user_name = user_name.replace("Eu me chamo ", "")
    if user_name.startswith("Eu sou o "):
        user_name = user_name.replace("Eu sou o", "")
    if user_name.startswith("Eu sou a "):
        user_name = user_name.replace("Eu sou a ", "")
    
    return user_name

def verifica_nome_exist(nome):
    dados = open("dados/nomes.txt", "r")
    nome_list = dados.readlines()
    
    if not nome_list:
        vazio = open("dados/nomes.txt", "r")
        conteudo = vazio.readlines()
        conteudo.append("{}".format(nome))
        vazio = open("dados/nomes.txt", "w")
        vazio.writelines(conteudo)
        vazio.close()
        
        return "Ola {}, prazer em te conhecer!".format(nome)
    
    for linha in nome_list:
        if linha == nome:
            return "Ola {}, acho que já nos conhecemos!!".format(nome)
        
        
    nomes_lista = open("dados/nomes.txt", "r")
    conteudo = vazio.readlines()
    conteudo.append("\n{}".format(nome))
    vazio = open("dados/nomes.txt", "w")
    vazio.writelines(conteudo)
    vazio.close()
    
    return "Oi {}, é a primeira vez que nos falamos".format(nome)

def name_list():
    try:
        nomes = open("dados/nomes.txt", "r")
        nomes.close
        
    except FileNotFoundError:
        nomes = open("dados/nomes.txt", "w")
        nomes.close()