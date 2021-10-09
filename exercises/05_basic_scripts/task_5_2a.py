#!/usr/bin/python3.8

# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску,
как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24, вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000


Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)


Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит
адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28 в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего
в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ip_str = input('Введите ip адрес в формате xxx.xxx.xxx.xxx/yy: ')

template = '''
Network:
{0:<10}{1:<10}{2:<10}{3:<10}
{0:<08b}  {1:<08b}  {2:<08b}  {3:<08b}


Mask:
/{4:}
{5:<10}{6:<10}{7:<10}{8:<10}
{5:<08b}  {6:<08b}  {7:<08b}  {8:<08b}
'''

# Переобразуем введенный адрес 'xxx.xxx.xxx.xxx/yy' в список ip вида ['xxx', 'xxx', 'xxx', 'xxx'] 
# и 
# маску сети в виде целого числа
ip = ip_str.split('.')
temp = ip[3].split('/')
mask = int(temp[1])
ip[3] = temp[0]

# Преобразуем ip адрес и маску в бинарный вид  
'''
ip_bin = '00001010000000010000000111000011'
mask_bin = '00001010000000010000000111000000'
'''

ip_bin_list = []
for i in ip:
  ip_bin_list.append('{:08b}'.format(int(i)))
  
ip_bin = ''.join(ip_bin_list)

mask_bin = "1" * mask + "0" * (32-mask)

# поиск по ip и mask адреса сети - net 
ip_bin_list = []
for i in range(0, len(ip_bin)):
  ip_bin_list.append(ip_bin[i])

mask_bin_list = []
for i in range(0, len(mask_bin)):
  mask_bin_list.append(mask_bin[i])

net_bin_list = []
for i in range(0, len(ip_bin_list)):
  if ip_bin_list[i] != mask_bin_list[i]:
    net_bin_list.append('0')
  else:
    net_bin_list.append(ip_bin_list[i])

net_bin = ''.join(net_bin_list)

# Разбивка на октеты(в виде списка) элементов строки net и mask( находятся "в бинарным виде")

ip_octet = []
ip_octet.append(int(ip_bin[0:8],2)) 
ip_octet.append(int(ip_bin[8:16],2))
ip_octet.append(int(ip_bin[16:24],2))
ip_octet.append(int(ip_bin[24:32],2))

mask_octet = []
mask_octet.append(int(mask_bin[0:8],2)) 
mask_octet.append(int(mask_bin[8:16],2))
mask_octet.append(int(mask_bin[16:24],2))
mask_octet.append(int(mask_bin[24:32],2))

net_octet = []
net_octet.append(int(net_bin[0:8],2)) 
net_octet.append(int(net_bin[8:16],2))
net_octet.append(int(net_bin[16:24],2))
net_octet.append(int(net_bin[24:32],2))

# вывод net и mask в отформатированном виде
#print(template.format(int(net_octet[0]), int(net_octet[1]), int(net_octet[2]), int(net_octet[3]), mask, int(mask_octet[0]), int(mask_octet[1]), int(mask_octet[2]), int(mask_octet[3])))
print(template.format(*net_octet, mask, *mask_octet))