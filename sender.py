from twilio.twiml.messaging_response import MessagingResponse



def reponse(text):
    
    response = MessagingResponse()
    response.message(text)
    return str(response)
    
