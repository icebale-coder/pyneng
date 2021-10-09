# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input('Введите ip адрес в формате x.x.x.x: ')

octet_list = ip.split('.')

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
