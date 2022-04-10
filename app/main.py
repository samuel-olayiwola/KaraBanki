import requests
from flask import Flask, request



app= Flask(__name__)
@app.route('/')
def voice():
  session_id   = request.values.get("sessionId", None)
  isActive  = request.values.get("isActive", None)
  phone_number = request.values.get("callerNumber", None)

  response = '<Response> <GetDigits timeout="30" finishOnKey="#">'
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

