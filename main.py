#!/dada/dada/com.termux/files/usr/bin/python3

import sys, os, time


# ________________________________

red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
magenta = '\033[1;35m'
cyan = '\033[1;36m'
cls = '\033[m'
# ________________________________

so_clear = 'clear'

# ________________________________
def banner():
	os.system('figlet TeleX | lolcat')
	print()
	print(red + '+' + cls + '}--------' + cyan + 'Visto-Preto' + cls + '--------{' + red '+' + cls)
	print()
	print()
# ________________________________

__author__ = 'VistoPreto'
__update__ = '24/03/2022'
__version__ = '0.0001'

# ________________________________

def existe():
	if os.path.isfile('channels.db'):
		ver()
	else:
		banner()
		os.system('termux-vibrate -d 100')
		os.system(so_clear)
		print()
		print('Você não possue canais cadrastado\nFavor adicione canais na lista')		
		print()
		time.sleep(2)

# ________________________________


def ver():
	db = open('channels.db', 'r')
	ver_db = db.read()
	db.close()
	l = ver_db.split('\n')
	l = l[:-1]

	ll = []
	lc = []

	os.system(so_clear)
	banner()
	while len(l) > 0:
		ll += l[1:2]
		lc += l[0:1]
		t = len(l)
		l = l[2:t]

	os.system('termux-vibrate -d 100')
	cont = 1
	for i in lc:
		print(str(cont) + ']	' + i)
		cont += 1
	print()
	print('0]	Voltar') 
	print('00]	Sair') 

	op_ver = input('\nEntre com o numero da opção:\n\n')
	op_id = op_ver
	lcc = str(lc[(int(op_id) - 1)])
	lll = str(ll[(int(op_id) - 1)])
	if op_ver == '0':
		pass
	elif op_ver == '00':
		os.system('termux-vibrate -d 100')
		time.sleep(1)
		os.system('termux-toast -b black -c green -g middle -s Volume de mídia em 60%')
		os.system('termux-volume music 9')
		os.system(so_clear)
		sys.exit()
	elif op_ver == op_id:
		os.system('termux-vibrate -d 100')
		os.system('termux-toast -b black -c green -g middle -s Volume de mídia silenciada')
		os.system('termux-volume music 0')
		os.system(so_clear)
		banner()
		print()
		print('Abrindo o canal', lcc)
		os.system('termux-open-url ' + lll)
		print()
		time.sleep(2)
		ver()

# ________________________________

def adicionar():
	while True:
		os.system('termux-vibrate -d 100')
		os.system(so_clear)
		banner()
		channel = input('''
Qual o nome do chanal?

0]	Voltar
00]	Sair

''')

		if channel == '0':
			break
		elif channel == '00':
			os.system('termux-vibrate -d 100')
			time.sleep(1)
			os.system('termux-toast -b black -c green -g middle -s Volume de mídia em 60%')
			os.system('termux-music 9')
			os.system(so_clear)
			sys.exit()
		os.system(so_clear)
		link = input('''
Qual o link do chanal?

0]	Voltar
00]	Sair

''')
		if link == '0':
			break
		elif link == '00':
			os.system('termux-vibrate -d 100')
			time.sleep(1)
			os.system('termux-toast -b black -c green -g middle -s Volume de mídia em 60%')
			os.system('termux-music 9')
			os.system(so_clear)
			sys.exit()
		else:
			with open('channels.db', 'a') as db:
				db.write(channel)
				db.write('\n') 
				db.write(link)
				db.write("\n") 
			os.system(so_clear)
			banner()
			os.system('termux-vibrate -d 100')
			print('O canal', channel, 'foi adicionado a lista')
			time.sleep(2)

# ________________________________

def start_menu():
	while True:
		os.system('termux-vibrate -d 100')
		os.system(so_clear)
		banner()
		print('''
\033[1;34m1\033[m]	Ver lista de canais
\033[1;34m2\033[m]]	Adicionar canais

\033[m]00\033[m]	Sair
			''')
		op = input('Entre com o numero da opção:\n\n')

		if (op == '00'):
			os.system('termux-vibrate -d 100')
			time.sleep(1)
			os.system('termux-toast -b black -c green -g middle -s Volume de mídia em 60%')
			os.system('termux-volume music 9')
			break
		elif (op == '1'):
			existe()
		elif (op == '2'):
			adicionar()

# ________________________________


if len(sys.argv) == 1:
	arg = ''
elif len(sys.argv) == 2:
	arg = sys.argv[1]
else:
	arg = 'err'

descricao = '''

TeleX.py [ --about ] [ --help : -h : -? ]

--about		Sobre o script
--help		Como usar o script 
--start		Inciar funçoes do script
'''

def arg_analise(x):

	if x == '--about':
		print()
		print('Desenvolvido por ', __author__)
		print('Version ', __version__)
		print('Ultimo update ', __update__)

	elif x == '--help' or x == '-h' or x == '-?':
		print('legal')

	elif x == '--start':
		start_menu()

	elif x == '' or x == 'err':
		print(descricao)
	else:
		print(descricao)

arg_analise(arg)
