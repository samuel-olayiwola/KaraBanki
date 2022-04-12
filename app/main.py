import json
import requests
from flask import Flask, request




# africastalking.initialize(os.getenv("USERNAME"), os.getenv("API_KEY"))
# token_service = africastalking.Token
# service = africastalking.Voice



'''speak commands'''
def voiceComands():
    commands = []
    transfer = voiceTransfer()
    deposit = voiceDeposit()
    airtime = voiceAirtime()
    complain = voiceComplain()
    commands.append(transfer,deposit,airtime,complain)
    return commands


'''play buy airtime command'''
def voiceAirtime():
   print("playing voiceairtime")
   return '<Play url="https://drive.google.com/file/d/1s-4UooIKrH1LhDp4MVdhNyFaJ6og9ezc/view?usp=sharing"/>'


'''play open account command'''
def voiceOpenAcct():
    print("playing openacct message")
    return '<Play url="https://drive.google.com/file/d/1Ur37PMtVAE_ZD-eGbcx8hC-lTxfC4kFF/view?usp=sharing"/>'

'''play transfer to same account command'''
def voiceTransfer():
    print("playing transfer to same bank message")
    return '<Play url="https://drive.google.com/file/d/16ZfZXfZmmR9-gcXOezGvqpa9Z3ALR1vW/view?usp=sharing"/>'
    

    
def voiceDeposit():
    print("playing deposit message")
    return '<Play url="https://drive.google.com/file/d/1-F6aLgRgnytTh3BZbv1dL9NbzZw1sYkD/view?usp=sharing"/>'
    
def voiceComplain():
    print("playing complaint message")
    return '<Play url="karaBankiVoice\complain.mp3"/>'
    
def depositInstruction():
    print("playing deposit instruction message")
    return '<Play url="https://drive.google.com/file/d/11XHGpsYX5DzfJHJ9ocBw1ViCiY-FIYnY/view?usp=sharing"/>'

def exitInstruction():
    print("exiting........")
    return '<Play url="https://drive.google.com/file/d/13UPIVf6IAvQcWCHguE_5PraQsAZUo55c/view?usp=sharing"/>'

'''create an account for a new user'''
def createAcct(phoneNum,pin):
    url= "https://kara-banking.herokuapp.com/api/v1/auth/register"
    payload = {
        "phone": str(phoneNum),
        "pin": int(pin)
    }
    headers = {
        "content-type":"application/json"
    }
    response = requests.request("POST",url,headers = headers ,data = json.dumps(payload))
    if response.status_code == 201:
       return True
        
    else:
        return False
        
    voiceComands()

        
"""aunthenticate user for any transaction,returns bool"""
def authenticate(phone,pin):
    url= "https://kara-banking.herokuapp.com/api/v1/auth/authenticate"
    payload = {
        "phone": str(phone),
        "pin": int(pin)


    }
    headers = {
        "content-type":"application/json"
    }
    response = requests.request("POST",url,headers = headers ,data = json.dumps(payload))
    if response.status_code == 201:
        
        return True
    else:
        
        return False



"""process airtime transaction for self"""
def airtimeMe(phone,amount):

    url= "https://kara-banking.herokuapp.com/api/v1/transaction/airtime"
    payload = {
        "phone": str(phone),
        "amount": int(amount)


    }
    headers = {
        "content-type":"application/json"
    }
    response = requests.request("POST",url,headers = headers ,data = json.dumps(payload))
    if response.status_code == 201:
        
        return True
    else:
       
        return False

"""process airtime transaction for others"""
def airtimeOthers(reciepient,phone,amount,pin):

    url= "https://kara-banking.herokuapp.com/api/v1/transaction/airtime/others"
    payload = {
        "phone": str(reciepient),
        "amount": int(amount),
        "pin": pin,
        "from": str(phone)


    }
    headers = {
        "content-type":"application/json"
    }
    response = requests.request("POST",url,headers = headers ,data = json.dumps(payload))
    if response.status_code == 201:
        
        return True
    else:
       
        return False


def complain():
    pass

def withdraw(phone,amount,pin):
    url= "https://kara-banking.herokuapp.com/api/v1/transaction/withdraw"
    payload = {
        "phone": str(phone),
        "amount": int(amount),
        "pin": pin,
        


    }
    headers = {
        "content-type":"application/json"
    }
    response = requests.request("POST",url,headers = headers ,data = json.dumps(payload))
    if response.status_code == 201:
     
        return True
    else:
        
        return False


"""process transfer returns bool"""
def transfer(to,frm,amount,pin):
    url= "https://kara-banking.herokuapp.com/api/v1/transaction/transfer"
    payload = {
        
        "to": str(to),
        "from": str(frm),
        "amount": int(amount),
        "pin": int(pin)


    }
    headers = {
        "content-type":"application/json"
    }
    response = requests.request("POST",url,headers = headers ,data = json.dumps(payload))
    if response.status_code == 201:
        
        return True
    else:
        
        return False


"""process deposit returns bool"""
def deposit(to,amount):
    url= "https://kara-banking.herokuapp.com/api/v1/transaction/deposit"
    payload = {
        
        "to": str(to),
        "amount": int(amount),
        


    }
    headers = {
        "content-type":"application/json"
    }
    response = requests.request("POST",url,headers = headers ,data = json.dumps(payload))
    if response.status_code == 201:
        
        return True
    else:
        
        return False


"""get balance"""
def balance(phone):
    url= "https://kara-banking.herokuapp.com/api/v1/transaction/balance/" + phone
    payload = {
      
    }
    headers = {
        "content-type":"application/json"
    }
    response = requests.request("Get",url,headers = headers ,data = json.dumps(payload))
    if response.status_code == 200:
        bal = json.loads(response.content.decode('UTF-8'))["balance"]
        return bal
    else:
        
        return

'''check if customer is registered.Returns a boolean'''
def isCustomer(phone):
    isCustomer = False
    url= "https://kara-banking.herokuapp.com/api/v1/transaction/customers"
    payload = {
     
    }
    headers = {
        "content-type":"application/json"
    }
    response = requests.request("GET",url,headers = headers ,data = payload)
    if response.status_code == 200:
        for customer in (json.loads(response.content.decode('UTF-8'))):
            if customer["phone"] == phone:
                isCustomer = True
        return isCustomer
    else:
        return False




app= Flask(__name__)
@app.post('/')
def voice():
   session_id   = request.values.get("sessionId", None)
   isActive  = request.values.get("isActive", None)
   phone_number = ""
   response =  '''<Response>
            <Play "url=https://drive.google.com/file/d/1Wnj-ukKcZ7lIiXGzuEDGjI9tshxbnO6D/view?usp=sharing"/>
            '''
   if isActive == 1:
      phone_number = request.values.get("callerNumber", None)
   
   if(phone_number != None):
      if(isCustomer(phone_number.replace("+234",""))):
         commands = voiceComands()
         for command in commands:
            response += command
         response += "</Response>"
      else:
         commands = voiceOpenAcct()
         response += "</Response>"
   return response
   # else:
   #    commands = VoiceAssistant.voiceOpenAcct()
   #    response += ' <GetDigits timeout="30" finishOnKey="#">'
   #    response += '<Say voice="man" playBeep="false">Please enter your account '
   #    response += 'number followed by the hash sign</Say> </GetDigits> </Response>'

   #  dtmfDigits = request.values.get("dtmfDigits", None)

   #  if dtmfDigits == '1234':
   #    response = '<Response> <GetDigits timeout="30" finishOnKey="#">'
   #    response +=' <Say voice="man" playBeep="false"> Press 1 followed by a hash '
   #    response +='sign to get your account balance or 0 followed by a hash sign to'
   #    response += ' quit</Say> </GetDigits></Response>'

   #  elif dtmfDigits == '1':
   #    response = '<Response>'
   #    response += '<Say voice="man" playBeep="false" >Your balance is 1234 Shillings</Say>'
   #    response+= '<Reject/> </Response>'

   #  elif dtmfDigits == '0':
   #    response = '<Response>'
   #    response += '<Say voice="man" playBeep="false" >Its been a pleasure, good bye </Say>'
   #    response+= '<Reject/> </Response>'
