import os
import time

import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

AUTH_TOKEN = os.getenv('AUTH_TOKEN')
ACOUNT_SID = os.getenv('ACOUNT_SID')
client = Client(ACOUNT_SID, AUTH_TOKEN)

NUMBER_FROM = os.getenv('NUMBER_FROM')
NUMBER_TO = os.getenv('NUMBER_TO')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')


def get_status(user_id):
    params = {
        'user_ids': user_id,
        'access_token': ACCESS_TOKEN,
        'fields': 'online',
        'v': 5.92,
    }
    response = requests.post(
        'https://api.vk.com/method/users.get',
        params=params
    )
    user_status = response.json()['response'][0]['online']
    return user_status


def sms_sender(sms_text):
    message = client.messages.create(
        to=NUMBER_TO,
        from_=NUMBER_FROM,
        body=sms_text
    )
    return message.sid


if __name__ == '__main__':
    vk_id = input('Введите id ')
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
