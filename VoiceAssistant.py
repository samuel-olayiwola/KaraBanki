# import json
# from logging import exception
# from time import sleep
# from click import command
# import pyttsx3
# import os
# import speech_recognition as sr
# from inputimeout import inputimeout, TimeoutOccurred
# from playsound import playsound
# import requests




# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

# '''speak commands to the user'''
# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# '''take an input from user with time constraint'''
# def takeTextCmd():
#     count = 0
#     if count > 3:
#         exitInstruction()
#         exit()
#     try:
#         reply = inputimeout(prompt='>>', timeout=10).strip()
#         return reply
#     except TimeoutOccurred:
#         speak("No input received,please try again")#reply in hausa and commands
#         reply = takeTextCmd()
#         count += 1
#         return reply
#     except exception as e:
#         speak("I do not understand your input,Listen and try again")#speak hausa and commands
#         reply = takeTextCmd()
#         return reply

# '''create an account for a new user'''
# def createAcct(phoneNum,pin):
#     url= "https://kara-banking.herokuapp.com/api/v1/auth/register"
#     payload = {
#         "phone": str(phoneNum),
#         "pin": int(pin)


#     }
#     headers = {
#         "content-type":"application/json"
#     }
#     response = requests.request("POST",url,headers = headers ,data = json.dumps(payload))
#     if response.status_code == 201:
#         speak("succesfull")
#     else:
#         speak("unsuccesfull, try again please")
        
#     voiceComands()

        
# """aunthenticate user for any transaction,returns bool"""
# def authenticate(phone,pin):
#     url= "https://kara-banking.herokuapp.com/api/v1/auth/authenticate"
#     payload = {
#         "phone": str(phone),
#         "pin": int(pin)


#     }
#     headers = {
#         "content-type":"application/json"
#     }
#     response = requests.request("POST",url,headers = headers ,data = json.dumps(payload))
#     if response.status_code == 201:
#         speak("Pin correct")
#         return True
#     else:
#         speak("Incorrect Pin")
#         return False



# """process airtime transaction for self"""
# def airtimeMe(phone,amount):

#     url= "https://kara-banking.herokuapp.com/api/v1/transaction/airtime"
#     payload = {
#         "phone": str(phone),
#         "amount": int(amount)


#     }
#     headers = {
#         "content-type":"application/json"
#     }
#     response = requests.request("POST",url,headers = headers ,data = json.dumps(payload))
#     if response.status_code == 201:
#         speak("Recharge succesfull")
#         return True
#     else:
#         speak("Recharge unsuccesful")
#         return False

# """process airtime transaction for others"""
# def airtimeOthers(reciepient,phone,amount,pin):

#     url= "https://kara-banking.herokuapp.com/api/v1/transaction/airtime/others"
#     payload = {
#         "phone": str(reciepient),
#         "amount": int(amount),
#         "pin": pin,
#         "from": str(phone)


#     }
#     headers = {
#         "content-type":"application/json"
#     }
#     response = requests.request("POST",url,headers = headers ,data = json.dumps(payload))
#     if response.status_code == 201:
#         speak("Recharge succesfull")
#         return True
#     else:
#         speak("Recharge unsuccesful")
#         return False


# def complain():
#     pass

# def withdraw(phone,amount,pin):
#     url= "https://kara-banking.herokuapp.com/api/v1/transaction/withdraw"
#     payload = {
#         "phone": str(phone),
#         "amount": int(amount),
#         "pin": pin,
        


#     }
#     headers = {
#         "content-type":"application/json"
#     }
#     response = requests.request("POST",url,headers = headers ,data = json.dumps(payload))
#     if response.status_code == 201:
#         speak("Withdrawal initiated")
#         return True
#     else:
#         speak("Withdrawal unsuccesful")
#         return False


# """process transfer returns bool"""
# def transfer(to,frm,amount,pin):
#     url= "https://kara-banking.herokuapp.com/api/v1/transaction/transfer"
#     payload = {
        
#         "to": str(to),
#         "from": str(frm),
#         "amount": int(amount),
#         "pin": int(pin)


#     }
#     headers = {
#         "content-type":"application/json"
#     }
#     response = requests.request("POST",url,headers = headers ,data = json.dumps(payload))
#     if response.status_code == 201:
#         speak("succesfull")
#         return True
#     else:
#         speak("unsuccesful")
#         return False


# """process deposit returns bool"""
# def deposit(to,amount):
#     url= "https://kara-banking.herokuapp.com/api/v1/transaction/deposit"
#     payload = {
        
#         "to": str(to),
#         "amount": int(amount),
        


#     }
#     headers = {
#         "content-type":"application/json"
#     }
#     response = requests.request("POST",url,headers = headers ,data = json.dumps(payload))
#     if response.status_code == 201:
#         speak("succesfull")
#         return True
#     else:
#         speak("unsuccesful")
#         return False


# """get balance"""
# def balance(phone):
#     url= "https://kara-banking.herokuapp.com/api/v1/transaction/balance/" + phone
#     payload = {
      
#     }
#     headers = {
#         "content-type":"application/json"
#     }
#     response = requests.request("Get",url,headers = headers ,data = json.dumps(payload))
#     if response.status_code == 200:
#         bal = json.loads(response.content.decode('UTF-8'))["balance"]
#         speak("your balance is " + str(bal))
#         return
#     else:
#         speak("unsuccesful")
#         return

# '''check if customer is registered.Returns a boolean'''
# def isCustomer(phone):
#     isCustomer = False
#     url= "https://kara-banking.herokuapp.com/api/v1/transaction/customers"
#     payload = {
     
#     }
#     headers = {
#         "content-type":"application/json"
#     }
#     response = requests.request("GET",url,headers = headers ,data = payload)
#     if response.status_code == 200:
#         for customer in (json.loads(response.content.decode('UTF-8'))):
#             if customer["phone"] == phone:
#                 isCustomer = True
#         return isCustomer
#     else:
#         return False


# '''welcome the user and check if new'''
# def welcome(phone):
#     print("playing welcome message.....")
#     playsound("karaBankiVoice\welcome.mp3")
#     speak("please wait")
#     if(isCustomer(phone)):
#         return
#     else:
#         voiceOpenAcct()
#         reply = takeTextCmd()
#         if reply == "1":
#             speak("enter a 4 digit pin")#create a 4 digit pin
#             pin = takeTextCmd()
#             speak("enter your 4 pin again")#confirm pin
#             pinRpt = takeTextCmd()
#             if pin == pinRpt:
#                 createAcct(phone,pin)
#                 speak("your account has been created.Details would be sent to you via sms")
#                 return
#             else:
#                 speak("pin do not match,try again")
#                 welcome(phone)
        
#         else:
#             voiceOpenAcct()


# '''speak commands'''
# def voiceComands():
#     commands = []
#     transfer = voiceTransfer()
#     deposit = voiceDeposit()
#     airtime = voiceAirtime()
#     complain = voiceComplain()
#     commands.append(transfer,deposit,airtime,complain)
#     return command


# '''play buy airtime command'''
# def voiceAirtime():
#     return '<Play url="playing airtime message"/>'
#     #playsound('karaBankiVoice/airtime.mp3')


# '''play open account command'''
# def voiceOpenAcct():
#     print("playing openacct message")
#     return '<Play url="karaBankiVoice\openAcct.mp3"/>'

# '''play transfer to same account command'''
# def voiceTransfer():
#     print("playing transfer to same bank message")
#     return '<Play url="karaBankiVoice/transfer2same.mp3"/>'
    

# # def voiceTransfer2Another():
# #     print("playing transfer to another message")
# #     playsound('karaBankiVoice/transfer2Another.mp3')
    
# # def voiceWithdraw():
# #     print("playing withdraw message")
# #     playsound('karaBankiVoice\withdraw.mp3')
    
# def voiceDeposit():
#     print("playing deposit message")
#     return '<Play url="karaBankiVoice\deposit.mp3"/>'
    
# def voiceComplain():
#     print("playing complaint message")
#     return '<Play url="karaBankiVoice\complain.mp3"/>'
    
# def depositInstruction():
#     print("playing deposit instruction message")
#     return '<Play url="karaBankiVoice\depositInstruction.mp3"/>'

# def exitInstruction():
#     print("exiting........")
#     return '<Play url="karaBankiVoice\exit.mp3"/>'

# isNewCustomer = False




# #if using vouce, requires pyaudio



# #using english
# # def wishMe():
# #     hour = int(datetime.datetime.now().hour)
# #     if hour>= 0 and hour<12:
# #         speak("Good Morning  !")
  
# #     elif hour>= 12 and hour<18:
# #         speak("Good Afternoon !")  
  
# #     else:
# #         speak("Good Evening Sir !") 
  
    
# #     speak("I am your Assistant")


# # def takeCommand():
     
# #     r = sr.Recognizer()
     
# #     with sr.Microphone() as source:
         
# #         print("Listening...")
        
# #         audio = r.listen(source)
        
  
# #     try:
# #         print("Recognizing...")   
# #         query = r.recognize_google(audio, language ='en-NG')
# #         print(f"User said: {query}\n")
  
# #     except Exception as e:
# #         print(e)   
# #         print("Unable to Recognize your voice.") 
# #         speak("Unable to Recognize your voice.") 
# #         return "None"
     
# #     return query



# #zero to end call

# commands = {
#     5:"balance",
#     1:"transfer",
#     #2:"withdraw",
#     3:"depositInstruction",
#     #4:"complain",
#     6:"airtimeTransaction"

# }

# if __name__ == '__main__':
#     clear = lambda: os.system('cls')
     
#     # This Function will clean any
#     # command before execution of this python file
#     clear()
#     #welcome customer and check if new or existing
#     phone = input("enter yout phone number:")
#     welcome(phone)
    
    
     
#     while True:
#         voiceComands()
#         query = int(takeTextCmd().lower())

#         if query == 5:
#             speak("enter your pin")
#             pin = int(takeTextCmd())
#             if(authenticate(phone,pin)):
#                 bal = balance(phone)
#                 speak(balance)

#         elif query == 3:
#             depositInstruction()

#         elif query == 2:
#             speak('How much do you want to withdraw')
#             amount = int(takeTextCmd())
#             speak("enter your pin")
#             pin = int(takeTextCmd())
#             if(authenticate(phone,pin)):
#                 withdraw(phone,amount,pin)
#             else:
#                 speak("try again")

#         elif query == 4:
#             complain()
            
#         elif query == 6:
#             speak("1 for airtime for self")
#             speak("2 for airtime for others")
#             reply = int(takeTextCmd())
#             speak("how much airtime do you wan to purchase")
#             amount = takeTextCmd()
           
#             if reply == 1:
#                 airtimeMe(phone)
#             elif reply == 2:
#                 speak("enter reciepient phone number")
#                 recieverPhone = takeTextCmd()
#                 speak("enter your pin")
#                 pin = takeTextCmd()
#                 if(authenticate(phone,pin)):
#                     airtimeOthers(recieverPhone,phone,amount,pin)
#                 else:
#                     speak("try again")

#         elif query == 0:
#             exitInstruction()
#             exit()

#         sleep(2)
        

