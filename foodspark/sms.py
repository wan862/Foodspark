import os
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
# Your Auth Token from twilio.com/console
auth_token  = os.getenv("TWILIO_AUTH_TOKEN")
# Your twilio number
from_number = "+17204632175"

def send(to_number, sms_text):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+65"+to_number, 
        from_=from_number,
        body=sms_text)
