import os
from flask import Flask, request
from twilio.rest import Client
from time import sleep
from sender import reponse
#from math import random


"""
REMEBER!!!
In order for the app to run you have to open a separate terminal and run
./ngrok http 5000
Copy the server URL and paste it into your twilio with /sms at the end
APP WILL NOT RUN WITHOUT THAT
"""
app = Flask(__name__)

number = '+12015846799'
account_sid = "AC38d6122ad4440e455cd54b1e7fad40b5"
auth_token = "4094841d7226ed2e6877462772d137ee"
previous_received = ''
previous_sent = ''

@app.route('/sms', methods=['GET','POST'])



def sms():
    global previous_received, previous_sent
    okay = ['okay', 'ok', 'i\'m fine', 'alright', 'fine']
    not_okay = ['nothing', 'no', 'bad', 'awful', 'terrible']
    
    idk = ['idk', 'i don\'t know', 'i/m not sure', 'not sure', 'don\'t know']

    calming_message = [
        "",
        "",
        ""
    ]
    message = request.form.get('Body').lower()
    print(str(message))

    if message == 'hey':
        return reponse('Hey, how are you?')

    if message in okay:
        previous_received = message
        return reponse("What's on your mind?")
    if message in not_okay and previous_sent in okay:
        print("testing")
        previous_sent = "Are you sure you're okay?"
        return reponse(previous_sent)
    '''

    if message in not_okay and previous_received in okay:
        previous_sent = "Are you sure you're okay?"
        return reponse(previous_sent)

    if len(message) > 20 and previous_received in okay:
        previous_sent = "Are you sure you're okay?"
        return reponse(previous_sent)
    '''
    if previous_sent == "Are you sure you're okay?" and message == 'no':
        previous_sent = 'How are you feeling on a scale of one to ten?'
        return reponse(previous_sent)

    if previous_sent == "Are you sure you're okay?" and message in not_okay:
        previous_sent = 'How are you feeling on a scale of one to ten?'
        return reponse(previous_sent)

    if previous_sent == 'How are you feeling on a scale of one to ten?' and int(message) > 5:
        previous_sent == "What happened?"
        return reponse(previous_sent)
        
    elif previous_sent == 'How are you feeling on a scale of one to ten?' and int(message) < 5:        
        previous_sent = ""
        return reponse("I think you've had a long day, you deserve to relax. I think you'll be okay, you're trying your hardest. Just text me 'hey' if you need anything else buddy.")

    if previous_sent == "What happened?":
        previous_sent = "I'm sorry, I hope you'll be okay. Will this still matter in three days?"
        return reponse(previous_sent)

    if previous_sent == "I'm sorry, I hope you'll be okay. Will this still matter in three days?":
        if message == "yes":
            previous_sent = "Is there anything that could make you feel better?"
            return reponse(previous_sent)
        elif message == "no":
            previous_sent = ""
            return reponse("I think you've had a long day, you deserve to relax. I think you'll be okay, you're trying your hardest. Just text me 'hey' if you need anything else buddy.")
        elif message == "idk" or message in idk:
            previous_sent = ""
            return reponse("I think you've had a long day, you deserve to relax. I think you'll be okay, you're trying your hardest. Just text me 'hey' if you need anything else buddy.")
        
    if previous_sent == "Is there anything that could make you feel better?":
        return reponse("null")
        

    return str(message)
    


if __name__ == "__main__":
    app.run(debug=True)