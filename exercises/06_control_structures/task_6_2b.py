# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


ip_is_good = 0
while ip_is_good == 0:
    # Запрос ввода данных
    ip = input('Введите ip адрес в формате x.x.x.x: ')

    ######################################
    # Проверка правильности формата ввода
    ######################################

    octet_list = ip.split('.')

    # Проверка, что состоит из 4 чисел (а не букв или других символов)
    ## Проверка, что состоит из 4 элементов (а не букв или других символов)
    try:
        if len(octet_list) != 4:
            raise ValueError
            #raise ValueError('Неправильный IP-адрес - в адресе не 4 отета')
    except ValueError:
        print('Неправильный IP-адрес - в адресе не 4 октета')
    else:
        ## Проверка, что состоит из 4 элементов (а не букв или других символов)
        try: 
            for i in octet_list:
                int(i)
        except ValueError:
            print('Неправильный IP-адрес - в нем присутствуют буквы или символы')
        else:
            # Проверка, что каждое число в диапазоне от 0 до 255
            try:
                for i in octet_list:
                    if int(i) < 0 or int(i) > 255:
                        raise ValueError
                        #raise ValueError('Неправильный IP-адрес число не в диапазоне от 0 до 255')
            except ValueError:
                print('Неправильный IP-адрес число не в диапазоне от 0 до 255')
            else:
                ip_is_good = 1

# формат ip адреса проверен ( данные введены корректно), теперь можно выполнять работу с ним

first_octet = int(octet_list[0])

if (first_octet > 0) and (first_octet < 223):
    print('{} - Это unicast'.format(ip))
elif (first_octet > 224) and (first_octet < 239):
    print('{} - Это multicast'.format(ip))
elif (int(octet_list[0]) == 255) and (int(octet_list[1]) == 255) and (int(octet_list[2]) == 255) and (int(octet_list[3]) == 255):
    print('{} - Это local broadcast'.format(ip))
elif (int(octet_list[0]) == 0) and (int(octet_list[1]) == 0) and (int(octet_list[2]) == 0) and (int(octet_list[3]) == 0):
    print('{} - Это local broadcast'.format(ip))
else: 
    print('{} - Это unused'.format(ip))