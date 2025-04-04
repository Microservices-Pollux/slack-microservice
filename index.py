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
    ack("Form command received!")
    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Hey there <@{command['user_name']}>!"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Click Me"},
                    "action_id": "button_click"
                }
            }
        ],
        text=f"Hey there <@{command['user_name']}>!"
    )


@app.action("button_click")
def handle_button_click(ack, body, say):
    ack()
    user_id = body["user"]["id"]
    say(f"Button clicked by <@{user_id}>!")


@app.command("/addField")
def add_field(ack, body):
    user_id = body["user_id"]
    channel_id = body["channel_id"]
    key = body["key"]
    value = body["value"]
    client.db.collection.insert_one(
        {"user_id": user_id, "channel_id": channel_id, "key": key, "value": value})
    ack(f"Added field to the database: {key} = {value}")


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
