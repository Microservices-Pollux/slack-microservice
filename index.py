# from flask import Flask
from flask import Flask, request
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_bolt import App
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
import logging
logging.basicConfig(level=logging.DEBUG)

load_dotenv()

socket_token = os.environ["SOCKET_TOKEN"]
bot_token = os.environ["BOT_TOKEN"]

app = App(token=bot_token)


@app.message("hello")
def message_hello(message, say):
    say(f"Hey there <@{message['user']}>!")


@app.command("/hello")
def hello_command(ack, body):
    user_id = body["user_id"]
    ack(f"Hi <@{user_id}>!")


@app.command("/form")
def form_command(ack, body, command, say):
    ack()
    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Hey there <@{command['user_name']}>!"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Open Modal Form"},
                    "action_id": "button_click"
                }
            }
        ],
    )


@app.action("button_click")
def handle_button_click(ack, body, client):
    ack()
    client.views_open(
        trigger_id=body["trigger_id"],
        view={
            "type": "modal",
            "callback_id": "view_1",
            "title": {"type": "plain_text", "text": "Survey"},
            "submit": {"type": "plain_text", "text": "Submit"},
            "blocks": [
                {
                    "type": "input",
                    "block_id": "input_a",
                    "label": {"type": "plain_text", "text": "What is your name?"},
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "name_input"
                    }
                },
                {
                    "type": "input",
                    "block_id": "input_b",
                    "label": {"type": "plain_text", "text": "What is your favorite color?"},
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "color_input"
                    }
                },
                {
                    "type": "input",
                    "block_id": "input_c",
                    "label": {"type": "plain_text", "text": "What are your hopes and dreams?"},
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "dreamy_input",
                        "multiline": True
                    }
                }
            ]
        }
    )


# Handle a view_submission request
@app.view("view_1")
def handle_submission(ack, body, client, view, logger):
    # Assume there's an input block with `input_c` as the block_id and `dreamy_input`
    hopes_and_dreams = view["state"]["values"]["input_c"]["dreamy_input"]["value"]
    user = body["user"]["id"]
    # Validate the inputs
    errors = {}
    if hopes_and_dreams is not None and len(hopes_and_dreams) <= 5:
        errors["input_c"] = "The value must be longer than 5 characters"
    if len(errors) > 0:
        ack(response_action="errors", errors=errors)
        return
    # Acknowledge the view_submission request and close the modal
    ack()
    # Do whatever you want with the input data - here we're saving it to a DB
    # then sending the user a verification of their submission

    # Message to send user
    msg = ""
    try:
        # Save to DB
        msg = f"Your submission of {hopes_and_dreams} was successful"
    except Exception as e:
        # Handle error
        msg = "There was an error with your submission"

    # Message the user
    try:
        client.chat_postMessage(channel=user, text=msg)
    except e:
        logger.exception(f"Failed to post a message {e}")


if __name__ == "__main__":
    handler = SocketModeHandler(app, socket_token)
    handler.start()


client = MongoClient(os.environ["DB_URL"], server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
