import os
from db import get_con, add_word
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def get_connection_controller():
    return get_con()


@app.route('/addName', methods=['POST'])
def add_name_controller():
    values = request.json['values']
    for i in values:
        add_word(i)
    return "Done"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
