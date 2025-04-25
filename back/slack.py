from dotenv import load_dotenv
import os
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_bolt import App
from  mongo import get_mongo_client


load_dotenv()

bot_token = os.environ["BOT_TOKEN"]
socket_token = os.environ["SOCKET_TOKEN"]

app = App(token=bot_token)


@app.message("hello")
def message_hello(message, say):
    say(f"Hey there <@{message['user']}>!")


@app.command("/hello")
def hello_command(ack, body):
    user_id = body["user_id"]
    ack(f"Hi <@{user_id}>!")


@app.command("/form")
def form_command(ack, body, command, say, client):
    ack()
    mongo_client = get_mongo_client()
    db = mongo_client["slack"]
    collection = db["forms"]
    form = collection.find_one({"name": command["text"]})

    if not form:
        say(f"Form {command['text']} not found.")
        return
    
    result = []
    for map in form["fields"]:
        result.append({
            "key": map["key"],
            "type": map["type"],
            "value": map["value"],
        })

    blocks = []
    for field in result:
        if field["type"] == "text":
            blocks.append({
                "type": "input",
                "block_id": field["key"],
                "label": {"type": "plain_text", "text": field["key"]},
                "element": {
                    "type": "plain_text_input",
                    "action_id": field["key"]
                }
            })
        elif field["type"] == "file":
            blocks.append({
                "type": "input",
                "block_id": field["key"],
                "label": {"type": "plain_text", "text": field["key"]},
                "element": {
                    "type": "file_input",
                    "action_id": field["key"]
                }
            })
        elif field["type"] == "number":
            blocks.append({
                "type": "input",
                "block_id": field["key"],
                "label": {"type": "plain_text", "text": field["key"]},
                "element": {
                    "type": "number_input",
                    "action_id": field["key"],
                    "is_decimal_allowed": True,
                    "placeholder": {"type": "plain_text", "text": field["value"]}
                }
            })
        elif field["type"] == "date":
            blocks.append({
                "type": "input",
                "block_id": field["key"],
                "label": {"type": "plain_text", "text": field["key"]},
                "element": {
                    "type": "datepicker",
                    "action_id": field["key"],
                    "placeholder": {"type": "plain_text", "text": field["value"]}
                }
            })
        elif field["type"] == "multiline":
            blocks.append({
                "type": "input",
                "block_id": field["key"],
                "label": {"type": "plain_text", "text": field["key"]},
                "element": {
                    "type": "plain_text_input",
                    "action_id": field["key"],
                    "multiline": True,
                    "placeholder": {"type": "plain_text", "text": field["value"]}
                }
            })
        elif field["type"] == "checkbox":
            blocks.append({
                "type": "input",
                "block_id": field["key"],
                "label": {"type": "plain_text", "text": field["key"]},
                "optional": True,
                "element": {
                    "type": "checkboxes",
                    "action_id": field["key"],
                    "options": [
                        {
                            "text": {"type": "plain_text", "text": field["key"]},
                            "value": field["value"]
                        }
                    ],
                }
            })

    client.views_open(
        trigger_id=body["trigger_id"],
        view={
            "type": "modal",
            "callback_id": "view_1",
            "title": {"type": "plain_text", "text": form["name"]},
            "submit": {"type": "plain_text", "text": "Submit"},
            "blocks": blocks,
        }
    )

# Handle a view_submission request
@app.view("view_1")
def handle_submission(ack, body, client, view, logger):
    ack()
    user = body["user"]["id"]

    # TODO - Send to some micro service
    print(str(view["state"]["values"]))

    msg = f"Your submission was successful"

    # Message the user
    client.chat_postMessage(channel=user, text=msg)


def execute_slack_socket_mode():
    handler = SocketModeHandler(app, socket_token)
    handler.start()

execute_slack_socket_mode()