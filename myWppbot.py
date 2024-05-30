from flask import request, Flask, session
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
app.secret_key = "any random string"

menu = "*Digite a opção que você deseja:*\n1. Realizar matrícula\n2. Vestibular UNEX\n3. Financeiro\n4. SAIR"

@app.route('/message', methods=['POST'])
def messagebot():
  message = request.form['Body'].lower()
  response = MessagingResponse()
  
  if 'opcao' in session:
    opcao = session['opcao']
  else:
      if message == '1':
        session['opcao'] = '1'
        response.message("Ainda não implementado")
      elif message == '2':
        session['opcao'] = '2'
        response.message("Ainda não implementado")
      elif message == '3':
        session['opcao'] = '3'
        response.message("Ainda não implementado")
      elif message == '4':
        session['opcao'] = '4'
        response.message("Até logo, volte sempre!")
      else:
        boasVindas = "Opção não disponível, escolha novamente\n"
        response.message(boasVindas + menu)
      return str(response)

@app.route('/teste', methods=['GET'])
def teste():
  return 'Servidor funcionando'


