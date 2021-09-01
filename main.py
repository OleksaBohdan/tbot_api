import requests
from conf import TOKEN

token = TOKEN
URL = 'https://api.telegram.org/bot' + token + '/'

# https://api.telegram.org/bot1919314620:AAEYMW9HBZodAaHO9sTBTs1Qma_eUCItvn4/getUpdates
# 42:00

def get_updates():
    url = URL + 'getupdates'
    response = requests.get(url)
    return response.json()


def get_message():
    data = get_updates()

    chat_id = data['result'][-1]['message']['chat']['id']
    message_text = data['result'][-1]['message']['text']

    message = {'chat_id': chat_id,
               'text': message_text}

    return message


def send_message(chat_id, text='Please wait...'):
    url = URL + f'sendmessage?chat_id={chat_id}&text={text}'
    requests.get(url)


def main():
    answer = get_message()
    chat_id = answer['chat_id']
    text = answer['text']
    if 'Привет' in text:
        send_message(chat_id, 'Привет, что ты хочешь? ')


if __name__ == '__main__':
    main()

