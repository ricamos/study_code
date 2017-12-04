# https://www.twilio.com/docs/libraries/python
# https://www.twilio.com/console

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACadc03583a800cc0f5ac151665a7f22ce"
# Your Auth Token from twilio.com/console
auth_token  = "65e1411e0f04988788866b30fb60c950"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5521992689195",
    from_="+17752048382",
    body="My first project with Twilio. Hello from Python!")

print(message.sid)