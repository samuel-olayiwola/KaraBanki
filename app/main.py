import requests
from flask import Flask, request
import VoiceAssistant
import africastalking
import os



africastalking.initialize(os.getenv("USERNAME"), os.getenv("API_KEY"))
token_service = africastalking.Token
service = africastalking.Voice


app= Flask(__name__)
@app.route('/')
def voice():
  session_id   = request.values.get("sessionId", None)
  isActive  = request.values.get("isActive", None)
  phone_number = request.values.get("callerNumber", None)
  response =  '<Response> <Play url="/KaraBankVoice/Welcome.mp3"/>'
  
  if(VoiceAssistant.isCustomer(phone_number.replace("+234",""))):
    commands = VoiceAssistant.voiceComands()
    for command in commands:
      response += command
  else:
    VoiceAssistant.voiceOpenAcct()
  response += ' <GetDigits timeout="30" finishOnKey="#">'
  response += '<Say voice="man" playBeep="false">Please enter your account '
  response += 'number followed by the hash sign</Say> </GetDigits> </Response>'

  dtmfDigits = request.values.get("dtmfDigits", None)

  if dtmfDigits == '1234':
    response = '<Response> <GetDigits timeout="30" finishOnKey="#">'
    response +=' <Say voice="man" playBeep="false"> Press 1 followed by a hash '
    response +='sign to get your account balance or 0 followed by a hash sign to'
    response += ' quit</Say> </GetDigits></Response>'

  elif dtmfDigits == '1':
    response = '<Response>'
    response += '<Say voice="man" playBeep="false" >Your balance is 1234 Shillings</Say>'
    response+= '<Reject/> </Response>'

  elif dtmfDigits == '0':
    response = '<Response>'
    response += '<Say voice="man" playBeep="false" >Its been a pleasure, good bye </Say>'
    response+= '<Reject/> </Response>'

  return response

