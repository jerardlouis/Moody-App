import os
from twilio.rest import Client
#(201) 584-6799
import receive_sms
'''
account_sid = "AC38d6122ad4440e455cd54b1e7fad40b5"
auth_token = "4094841d7226ed2e6877462772d137ee"
'''
def send(text):
    account_sid = "AC38d6122ad4440e455cd54b1e7fad40b5"
    auth_token = "4094841d7226ed2e6877462772d137ee"
    client = Client(account_sid, auth_token)
    number = '+12015846799'
    client.messages.create(from_=number,
                        to='+12019815889',
                        body=text)

    message = client.messages(account_sid).fetch()
    return 0
print('Enter your message')
send(text = input())
print(message.to)