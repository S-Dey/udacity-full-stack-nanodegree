from twilio.rest import Client

account_sid = "AC3e4c8a064ab530f38f73736fd182d5d9"
auth_token = "608293f8d3423704f19488dda88e178bc"
client = Client(account_sid, auth_token)
client.messages.create(
  to="+91950xxxxx",     #Change to your own.
  from_="+1720xxxxx",   #Change to your own.
  body="Tomorrow's forecast in Financial District, San Francisco is Clear",
  media_url="https://climacons.herokuapp.com/clear.png")