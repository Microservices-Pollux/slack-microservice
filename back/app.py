from flask import Flask, request

import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)


@app.route('/')
def index():
    return {
        "hello": "world"
    }
