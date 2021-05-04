from time import sleep

import requests, fake_useragent
banner ='''
 ____                        __                      
/\  _`\                     /\ \                     
\ \ \L\ \    ___     ___ ___\ \ \____     __   _ __  
 \ \  _ <'  / __`\ /' __` __`\ \ '__`\  /'__`\/\`'__
  \ \ \L\ \/\ \L\ \/\ \/\ \/\ \ \ \L\ \/\  __/\ \ \/ 
   \ \____/\ \____/\ \_\ \_\ \_\ \_,__/\ \____ \_\ 
    \/___/  \/___/  \/_/\/_/\/_/\/___/  \/____/ \/_/ 
'''


# colours
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
def dev():
    mode = int()
    print("""
Введите режим работы:
[1] - Термукс
[2] - Виндовс
[3] - Линукс
    """)
    mode = input()
    if mode == 1:
        def menu():
            mod = int()
            print("""
Введите режим работы:
[1] - Спамер
[2] - Обновить
[3] - Выход
            """)
            menu = input()
            if mod == 1:
                print('f')
            if mod == 2:
                print('Обновлений не найдено это последняя версия!')
                sleep(3)
                menu()
            if mod == 3:
                print('Спасибо, что выбрали нас!')
                sleep(3)
                end

        menu()

















    if mode == 2:
        print('f')

















    if mode == 3:
        print('Режим в разработке!')
        sleep(3)
        dev()
dev()
