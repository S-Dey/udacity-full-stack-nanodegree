from twilio.rest import Client

account_sid = "Your account SID"
auth_token = "Your authentication token"
client = Client(account_sid, auth_token)
client.messages.create(
  to="+91950xxxxx",     #Change to your own.
  from_="+1720xxxxx",   #Change to your own.
  body="Tomorrow's forecast in Financial District, San Francisco is Clear",
  media_url="https://climacons.herokuapp.com/clear.png")
