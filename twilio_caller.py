# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
from env_vars_parser import get_env_var

class TwilioCaller:
    def call_user(self, voice_url):

        # Set the twilio auth token.
        twilio_auth_token = get_env_var("TWILIO_AUTH_TOKEN")

        account_sid = "ACb540d11bad0ecd2ec4ec372e0f2d186f"
        auth_token = get_env_var("TWILIO_AUTH_TOKEN")
        client = Client(account_sid, auth_token)

        call = client.calls.create(
          url="https://github.com/ibratanov/sleep-better/blob/feat_tts/voice.xml",
          to="+12017797747",
          from_="+18773953632"
        )

        print(call.sid)
      
        return call