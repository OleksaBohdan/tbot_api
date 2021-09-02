import requests
from conf import TOKEN
from time import sleep

token = TOKEN
URL = 'https://api.telegram.org/bot' + token + '/'

global last_update_id
last_update_id = 0

# https://api.telegram.org/bot1919314620:AAEYMW9HBZodAaHO9sTBTs1Qma_eUCItvn4/getUpdates


def get_updates():
    url = URL + 'getupdates'
    response = requests.get(url)
    return response.json()


def get_message():
    # Отвечаем только на новые сообщения
    # Получаем 'update_id' каждого обновления, записывать его в переменную
    # а затем сравнивать его с 'update_id' последнего элемента в списке 'result'
    data = get_updates()

    last_object = data['result'][-1]
    current_updade_id = last_object['update_id']

    global last_update_id
    if last_update_id != current_updade_id:
        last_update_id = current_updade_id

        chat_id = last_object['message']['chat']['id']
        message_text = last_object['message']['text']

        message = {'chat_id': chat_id,
                   'text': message_text}

        return message
    return None


def send_message(chat_id, text='Please wait...'):
    url = URL + f'sendmessage?chat_id={chat_id}&text={text}'
    requests.get(url)


def calc(chat_id, text):
    send_message(chat_id, 'Я готов считать! \nВведи числа, например "10.5"\n')
    send_message(chat_id, 'Введи конверт в регу %:')
# Берем % в регу
    while True:
        answer = get_message()
        if answer != None:
            text = answer['text']
            reg = float(text)
            # send_message(chat_id, f'Процент в регу = {reg}%')
            if reg > 0:
                break
# Берем % в деп
    send_message(chat_id, 'Введи конверт в деп %:')
    while True:
        answer = get_message()
        if answer != None:
            text = answer['text']
            dep = float(text)
            # send_message(chat_id, f'Процент в деп = {dep}%')
            if dep > 0:
                break
# Сумма выплаты
    send_message(chat_id, 'Введи сумму выплаты в $:')
    while True:
        answer = get_message()
        if answer != None:
            text = answer['text']
            cpa = float(text)
            #send_message(chat_id, f'Сумма выплаты = {cpa}$')
            if dep > 0:
                break

# Производим вычисления:
    inst_in_reg = 100 / reg
    reg_in_dep = 100 / dep
    inst_in_dep = reg_in_dep * inst_in_reg
    roi_null = cpa / inst_in_dep
    roi_sto = roi_null / 2

    send_message(chat_id, f"Количество инсталлов на 1 деп = {round(inst_in_dep)}\n"
                          f"Максимальная цена инсталла для ROI 0% = {round(roi_null, 2)}$\n"
                          f"Максимальная цена инсталла для ROI 100% = {round(roi_sto, 2)}$")

# Завершение программы
    send_message(chat_id, 'Что бы завершить программу введите 9')
    while True:
        answer = get_message()
        if answer != None:
            text = answer['text']
            finish = text
            if finish == '9':
                send_message(chat_id, 'Удачи! Программа завершена.\n'
                                      'Что бы начать сначала введите /start')
                main()
            else:
                calc(chat_id, text)


def main():

    while True:
        answer = get_message()

        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']
           # send_message(chat_id, text)
            if text == '/start':
                send_message(chat_id, 'Добро пожаловать!\n')
                calc(chat_id, text)
        else:
            continue
        sleep(2)

if __name__ == '__main__':
    main()

        # chat_id = answer['chat_id']
        # text = answer['text']
        #
        #
        # send_message(chat_id, 'Я готов считать! \nВведи числа, например "10.5"\n')
        # send_message(chat_id, 'Конверт в регу %:')
        #
        #
        # reg = text
        # send_message(chat_id, reg)



    # while True:
    #     answer = get_message()
    #
    #     if answer != None:
    #         chat_id = answer['chat_id']
    #         text = answer['text']
    #
    #         if 'Привет' in text:
    #             send_message(chat_id, 'Привет, что ты хочешь? ')
    #     else:
    #         continue
    #
    #     sleep(2)



# while flag:
#     print('Я готов считать! \nВведи числа, например "10.5"\n')
#     reg = input('Конверт в регу %: ')
#     dep = input('Конверт в деп %: ')
#     cpa = input('Сумма выплаты в $: ')
#
#     while type(reg) != float and type(dep) != float and type(cpa) != float:
#         try:
#             reg = float(reg)
#             dep = float(dep)
#             cpa = float(cpa)
#         except ValueError:
#             print('Ошибка ввода. Введите только числа заново:')
#             reg = input('Конверт в регу %: ')
#             dep = input('Конверт в деп %: ')
#             cpa = input('Сумма выплаты в $: ')
#
#     inst_in_reg = 100 / reg
#     reg_in_dep = 100 / dep
#     inst_in_dep = reg_in_dep * inst_in_reg
#
#     print()
#     print('Количество инсталлов на 1 деп = ', round(inst_in_dep))
#     roi_null = cpa / inst_in_dep
#     print('Максимальная цена инсталла для ROI 0% = ', round(roi_null, 2), '$')
#     roi_sto = roi_null / 2
#     print('Максимальная цена инсталла для ROI 100% = ', round(roi_sto, 2), '$')
#     print('Рассчеты завершены.')
#     print()



