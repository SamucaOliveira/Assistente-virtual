import speech_recognition as sr
import pyttsx3
from random import choice
from config import *

reproducao = pyttsx3.init()

def sai_som(resposta):
    reproducao.say(resposta)
    reproducao.runAndWait()
    
def assistente():
    
    while True:
        resposta_erro_aleatorio = choice(lista_erros)
        rec = sr.Recognizer()
        
        with sr.Microphone()as s:
            rec.adjust_for_ambient_noise(s)
            while True:
                try:
                    audio = rec.listen(s)
                    user_name = rec.recognize_google(audio, language = "pt-br")
                    user_name = verifica_nome(user_name)
                    name_list()
                    apresentacao = "{}".format(verifica_nome_exist(user_name))
                    
                    sai_som("{}".format(resposta))
                
                except sr.UnknownValueError:
                    print(resposta_erro_aleatorio)
    
    print("="* apresentacao)
    print("Ouvindo")
    while True:
        resposta_erro_aleatorio = choice(lista_erros)
        rec = sr.Recognizer()
        
        with sr.Microphone()as s:
            rec.adjust_for_ambient_noise(s)
            while True:
                try:
                    audio = rec.listen(s)
                    entrada = rec.recognize_google(audio, language = "pt-br")
                    print("{}: {}".format(user_name, entrada))
                
                    resposta = conversas[entrada]
                
                    print("Assistente: {}".format(resposta))
                    sai_som("{}".format(resposta))
                except sr.UnknownValueError:
                    print(resposta_erro_aleatorio)
                
if __name__ == '__main__':
    intro()
    sai_som("Iniciando")
    assistente()