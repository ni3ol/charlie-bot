import os
from flask import Flask, request
from slackclient import SlackClient
app = Flask(__name__)


SLACK_TOKEN = os.environ.get('SLACK_TOKEN')
slack_client = SlackClient(SLACK_TOKEN)


def send_message(user_id, message):
    slack_client.api_call(
        'chat.postMessage',
        user=user_id,
        text=message,
        username='charlie',
        icon_emoji=':coffee:'
    )


def get_user_name(form_data):
    return form_data['user_name']


def get_response_message(form_data):
    sender_name = get_user_name(form_data)
    friends = get_friend_list(form_data)
    return 'Hi {}! I have invited {}.'.format(sender_name, friends)


def get_friend_list(form_data):
    return form_data['text']


@app.route("/caffeinetrip", methods=["post"])
def caffeinetrip():
    form_data = request.form
    response_message = get_response_message(form_data)
    user_id = form_data['user_id']
    user_message = 'Do you want coffee?'
    send_message(user_id, user_message)
    return response_message, 200


def main():
    app.run()


if __name__ == '__main__':
    main()
