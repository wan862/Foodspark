from twilio.rest import Client
from sms_conf import *

def send(to_number, sms_text):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+65"+to_number, 
        from_=from_number,
        body=sms_text)
