import json
import os
from twilio.rest import Client

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
to_number = os.environ.get("TO_NUMBER")
from_number = os.environ.get("FROM_NUMBER")

client = Client(account_sid, auth_token)

def lambda_handler(event, context):
    message = client.messages.create(
        body="Remember to make the overnight oats!",
        from_=from_number,
        to=to_number,
    )

    return {"status": message.status,
            "error_code": message.error_code,
            "error_message": message.error_message,
            "body": message.body}
