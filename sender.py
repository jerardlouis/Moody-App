from twilio.twiml.messaging_response import MessagingResponse
#(201) 584-6799



def reponse(text):
    
    response = MessagingResponse()
    response.message(text)
    return str(response)
    
