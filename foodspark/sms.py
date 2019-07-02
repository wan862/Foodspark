from twilio.rest import Client
import sms_conf

def send(to_number, sms_text):
    client = Client(sms_conf.account_sid, sms_conf.auth_token)
    message = client.messages.create(
        to="+65"+to_number, 
        from_=sms_conf.from_number,
        body=sms_text)
