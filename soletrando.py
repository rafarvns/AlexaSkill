from flask import Flask
from flask_ask import Ask, statement, request, context, question, session, convert_errors, version
from mysql_con import get_a_random_word
import json
import requests
import time
import random

## https://developer.amazon.com/en-US/docs/alexa/alexa-design/adaptable.html

app = Flask(__name__)
ask = Ask(app, "/")
palavra_comp = "TECLADO"
palavra = "t. e. c. l. a. d. o."

@ask.launch
def start_skill():
    welcome_message = "Olá! Vamos soletrar? Faça um pedido de uma palavra e tente soletrá-la!"
    return question(welcome_message).reprompt("Você pode pedir por níveis como por exemplo: Me dê uma palavra fácil, normal ou difícil!")


@ask.intent('WordIntent', convert={'level_word': str})
def get_word(level_word):

    frases_duvida = ["Não entendi, poderia fazer um pedido novamente?",
                    "Desculpe, não consegui entender... Poderia pedir uma palavra de novo?"]

    frases_solicitar_palavra = [  "Vamos, peça uma palavra para mim!",
                                "Me peça uma palavra!",
                                "Peça uma palavra, como por exemplo: Me dê uma palavra fácil!"]
    
    frases_resposta = [ "Muito bem! Diga iniciar e soletre a palavra: ",
                        "Legal! Diga iniciar e já soletre a palavra: ",
                        "Okay! Diga iniciar e em seguida soletre a palavra: "]

    if 'level_word' in convert_errors:
        return question(random.choice(frases_duvida))
    
    if level_word is None:
        return question(random.choice(frases_solicitar_idade))

    word = get_a_random_word()
    for w in word:
        palavra_comp = w[0]
        palavra = w[1]

    palavra_ = palavra_comp+"!"
 
    frase_resposta = random.choice(frases_resposta) + palavra_

    return statement(frase_resposta.format(level_word))

@ask.intent('SoletraIntent', convert={'soletracao': str})
def get_word(soletracao):

    if(soletracao == palavra_comp):
        return statement("Parabéns, você acertou!")
    
    return statement("Oh não! você errou! A resposta correta é: " + palavra)

@ask.intent('AMAZON.StopIntent')
def stop():
    return statement("Até mais")


@ask.intent('AMAZON.CancelIntent')
def cancel():
    return statement("Até mais")


@ask.session_ended
def session_ended():
    return "{}", 200

if __name__ == "__main__":
    app.run(debug=True)