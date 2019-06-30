from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACecd566249532a05854e0b664697499db"
# Your Auth Token from twilio.com/console
auth_token  = "fa4757ca599b15790a4ed758009b18d7"
# Your twilio number
from_number = "+17204632175"

def send(to_number, sms_text):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+65"+to_number, 
        from_=from_number,
        body=sms_text)
