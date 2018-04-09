from flask import Flask, request
app = Flask(__name__)


def get_sender_name(form_data):
    return form_data['sender_name']


def get_response_message(form_data):
    sender_name = get_sender_name(form_data)
    friends = get_friend_list(form_data)
    return 'Hi {}! I have invited {}.'.format(sender_name, friends)


def get_friend_list(form_data):
    return form_data['text']


@app.route("/caffeinetrip", methods=["post"])
def caffeinetrip():
    form_data = request.form
    response_message = get_response_message(form_data)
    return response_message, 200
