from ast import Num, Return
import json
import requests
from flask import Flask, request




# africastalking.initialize(os.getenv("USERNAME"), os.getenv("API_KEY"))
# token_service = africastalking.Token
# service = africastalking.Voice



'''speak commands'''
def voiceComands():
    commands = []
    #transfer = voiceTransfer()
    deposit = voiceDeposit()
    airtime = voiceAirtime()
    complain = voiceComplain()
    exiting = exitInstruction()
    #commands.append(transfer)
    commands.append(deposit)
    commands.append(airtime)
    commands.append(complain)
    commands.append(exiting)
    return commands


'''play buy airtime command'''
def voiceAirtime():
   print("playing voiceairtime")
   return '<Say> For airtime, Press 1</Say>'
   return '<Play url="https://drive.google.com/file/d/1s-4UooIKrH1LhDp4MVdhNyFaJ6og9ezc/view?usp=sharing"/>'


'''play open account command'''
def voiceOpenAcct():
    print("playing openacct message")
    return '<Say> To register, Press 1 </Say>'
    return '<Play url="https://drive.google.com/file/d/1Ur37PMtVAE_ZD-eGbcx8hC-lTxfC4kFF/view?usp=sharing"/>'

'''play transfer to same account command'''
# def voiceTransfer():
#     print("playing transfer to same bank message")
#     return '<Say> For transfer, press 2</Say>'
#     return '<Play url="https://drive.google.com/file/d/16ZfZXfZmmR9-gcXOezGvqpa9Z3ALR1vW/view?usp=sharing"/>'
   
def balInstruction():
   print("playing transfer to same bank message")
   return '<Say> For balance, press 2</Say>'

    
def voiceDeposit():
    print("playing deposit message")
    return '<Say> For deposit, press 3</Say>'
    return '<Play url="https://drive.google.com/file/d/1-F6aLgRgnytTh3BZbv1dL9NbzZw1sYkD/view?usp=sharing"/>'
    
    
def voiceComplain():
    print("playing complaint message")
    return '<Say> For complaints, press 4</Say>'
    return '<Play url="karaBankiVoice\complain.mp3"/>'
    
def depositInstruction():
    print("playing deposit instruction message")
    return '<Play url="https://drive.google.com/file/d/11XHGpsYX5DzfJHJ9ocBw1ViCiY-FIYnY/view?usp=sharing"/>'

def exitInstruction():
    print("exiting........")
    return '<Say> For exit, press 5 or hang up now</Say>'
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
        
        return False

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


@app.post('/Pin')
def createPin():
   reply = request.values.get('dtmfDigits')
   phone_number = request.values.get("callerNumber",type=str)
   if(createAcct(phone_number.replace("+234",""),int(reply))):
         
         return  '''<Response>
               <Say> Your account has been created with your phone number as account number. You will recieve a sms containing the deatils  </Say>
               
               



               </Response>'''
   else:
         return '''<Response>
               <Say> An error occured, please try again</Say>
               
               
               </Response>'''



@app.post('/airtime')
def airtime():
   reply = request.values.get('dtmfDigits',type=int)
   phone_number = request.values.get("callerNumber",type=str)
   print("Register",reply,phone_number)
   if authenticate(phone_number,int(reply)):
      return '''<Response>
            <GetDigits timeout="5" callbackUrl="https://karabanki.herokuapp.com/buyairtime"> 
                  <Say> enter amount</Say>
                </GetDigits>
                  </Response>'''


@app.post('/buyairtime')
def buyairtime():
   reply = request.values.get('dtmfDigits',type=int)
   phone_number = request.values.get("callerNumber",type=str)
   if airtimeMe(phone_number,reply):
      return '''<Response>

             
                  <Say> Recharge Successful</Say>
                
             
                  </Response>'''
   else:
      return "<Response><Say> Recharge unsuccessful </Say> </Response>"


@app.post('/bal')
def bal():
   reply = request.values.get('dtmfDigits',type=int)
   phone_number = request.values.get("callerNumber",type=str)
   if authenticate(phone_number,reply):
      bal = balance(phone_number)
      if bal:

         return '''<Response>

             
                  <Say> Your balance is </Say>''' + bal + '''
                
             
                  </Response>'''
      else:
         return '''<Response>

             
                  <Say> An error occured </Say>
                
             
                  </Response>'''


@app.post('/transact')
def transact():
   reply = request.values.get('dtmfDigits',type=int)
   phone_number = request.values.get("callerNumber",type=str)
   print("Register",reply,phone_number)
   if int(reply) == 1:
      return '''<Response>
            <GetDigits timeout="5" callbackUrl="https://karabanki.herokuapp.com/airtime"> 
                  <Say> enter your 4 digit pin </Say>
                </GetDigits>
                  </Response>'''
   elif int(reply) == 2:
         return '''<Response>
            <GetDigits timeout="5" callbackUrl="https://karabanki.herokuapp.com/bal"> 
                  <Say> enter your 4 digit pin </Say>
                </GetDigits>
                  </Response>'''


@app.post('/Register')
def register():
   reply = request.values.get('dtmfDigits',type=int)
   phone_number = request.values.get("callerNumber",type=str)
   print("Register",reply,phone_number)
   if int(reply) == 1:
      return '''<Response>
            <GetDigits timeout="7" callbackUrl="https://karabanki.herokuapp.com/Pin"> 
                  <Say> Please create a 4 digit pin </Say>
                </GetDigits>
                  </Response>'''
      
   
@app.post('/')
def voice():
   session_id   = request.values.get("sessionId", None)
   isActive  = request.values.get("isActive", None)
   phone_number = request.values.get("callerNumber",type=str)
  # <Play url="https://drive.google.com/file/d/1Wnj-ukKcZ7lIiXGzuEDGjI9tshxbnO6D/view?usp=sharing"/>
   response =  '''<Response>
            <Say> Welcome to Karabanki </Say>
            '''
   print()
   # if isActive == 1:
   #    phone_number = request.values.get("callerNumber", None)
   
   
   if(isCustomer(phone_number.replace("+234",""))):
         commands = voiceComands()
         for command in commands:
            response += command +"\n"
         response += '''
                     <GetDigits timeout="5" callbackUrl="https://karabanki.herokuapp.com/transact"><Say>For balance, pres 7</Say></GetDigits>
                     </Response>'''
   else:
          
         response += '''
         <GetDigits timeout="5" callbackUrl="https://karabanki.herokuapp.com/Register">
         ''' + voiceOpenAcct() + '''
         </GetDigits>'''
            
         
         response += "</Response>"
   # else:
   #    response += "</Response>"
   print(response)
   return response
   
   # else:
   #    commands = VoiceAssistant.voiceOpenAcct()
   #    response += ' <GetDigits timeout="30" finishOnKey="#">'
   #    response += '<Say voice="man" playBeep="false">Please enter your account '
   #    response += 'number followed by the hash sign</Say></GetDigits> </Response>'

   # dtmfDigits = request.values.get("dtmfDigits", None)

   # if dtmfDigits == '1234':
   #    response = '<Response> <GetDigits timeout="30" finishOnKey="#">'
   #    response +=' <Say voice="man" playBeep="false"> Press 1 followed by a hash '
   #    response +='sign to get your account balance or 0 followed by a hash sign to'
   #    response += ' quit</Say></GetDigits></Response>'

   # elif dtmfDigits == '1':
   #    response = '<Response>'
   #    response += '<Say voice="man" playBeep="false" >Your balance is 1234 Shillings</Say>'
   #    response+= '<Reject/> </Response>'

   # elif dtmfDigits == '0':
   #    response = '<Response>'
   #    response += '<Say voice="man" playBeep="false" >Its been a pleasure, good bye </Say>'
   #    response+= '<Reject/> </Response>'
   # return response