from flask import Flask
from flask_ask import Ask, statement, request, context, question, session, convert_errors, version
import json
import requests
import time
import random

## https://developer.amazon.com/en-US/docs/alexa/alexa-design/adaptable.html

app = Flask(__name__)
ask = Ask(app, "/")

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
    
    frases_resposta = [ "Muito bem! Soletre: Casa!",
                        "Legal! Agora soletre: Teclado!",
                        "Okay! Soletre: Computador!"]

    if 'level_word' in convert_errors:
        return question(random.choice(frases_duvida))
    
    if level_word is None:
        return question(random.choice(frases_solicitar_idade))

    return statement(random.choice(frases_resposta).format(level_word))

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