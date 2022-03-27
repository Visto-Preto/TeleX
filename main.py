#!/data/data/com.termux/files/usr/bin/python3

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
	print(red + '+' + cls + '}--------' + cyan + 'Visto-Preto' + cls + '--------{' + red + '+' + cls)
	print()
	print()
# ________________________________

__author__ = 'VistoPreto'
__update__ = '24/03/2022'
__version__ = '0.0001'


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
		print(blue + str(cont) + cls + ']	' + magenta + i)
		cont += 1
	print()
	print(blue + '0' + cls + ']' + magenta + '	Voltar') 
	print(blue + '00' + cls +']'+ magenta + '	Sair') 
	print()

	op_ver = input('\n' + yellow + 'Entre com o numero da opção:\n\n' + cls)

	if op_ver.isnumeric():
		if op_ver != 0:
			if int(op_ver) > len(lc):
				existe()
			else:
				op_id = op_ver
				lcc = str(lc[(int(op_id) - 1)])
				lll = str(ll[(int(op_id) - 1)])
		else:
			op_id = str(op_ver)
	else:
		existe()

	if op_ver == '0':
		start_menu()
	elif op_ver == '00':
		os.system('termux-vibrate -d 100')
		time.sleep(1)
		os.system('termux-toast -b black -c green -g middle -s Volume de mídia em 60%')
		os.system('termux-volume music 9')
		os.system(so_clear)
		sys.exit()
	elif op_ver == op_id:
		os.system('termux-vibrate -d 100')
		os.system('termux-toast -b black -c green -g middle -s Volume de mídia em 0%')
		os.system('termux-volume music 0')
		os.system(so_clear)
		banner()
		print()
		print(cls + 'Abrindo o canal ' + green + lcc)
		os.system('termux-open-url ' + lll)
		print()
		time.sleep(3)
		existe()



# ________________________________

def existe():
	if os.path.isfile('channels.db'):
		ver()
	else:
		banner()
		os.system('termux-vibrate -d 100')
		os.system(so_clear)
		print()
		print(red + 'Você não possue canais cadrastado\nFavor adicione canais na lista' + cls)		
		print()
		time.sleep(2)

# ________________________________

def adicionar():
	while True:
		os.system('termux-vibrate -d 100')
		os.system(so_clear)
		print()
		print(blue + '0' + cls + ']' + magenta + '	Voltar') 
		print(blue + '00' + cls +']'+ magenta + '	Sair')
		print()
		print() 
		channel = input(yellow + 'Qual o nome do chanal?\n\n' + cls)

		if channel == '0':
			break
		elif channel == '00':
			os.system('termux-vibrate -d 100')
			time.sleep(1)
			os.system('termux-toast -b black -c green -g middle -s Volume de mídia em 60%')
			os.system('termux-volume music 9')
			os.system(so_clear)
			sys.exit()
		os.system(so_clear)
		print()
		print(blue + '0' + cls + ']' + magenta + '	Voltar') 
		print(blue + '00' + cls +']'+ magenta + '	Sair')
		print()
		print() 
		link = input(yellow + 'Qual o link do chanal?\n\n' + cls)
		if link == '0':
			break
		elif link == '00':
			os.system('termux-vibrate -d 100')
			time.sleep(1)
			os.system('termux-toast -b black -c green -g middle -s Volume de mídia em 60%')
			os.system('termux-volume music 9')
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
			print(cls + 'O canal ' + green + channel + cls + ' foi adicionado a lista')
			time.sleep(2)

# ________________________________

def start_menu():
	while True:
		os.system('termux-vibrate -d 100')
		os.system(so_clear)
		banner()
		print('''
\033[1;34m1\033[m]	\033[1;35mVer lista de canais\033[m
\033[1;34m2\033[m]	\033[1;35mAdicionar canais\033[m

\033[1;34m00\033[m]	\033[1;35mSair\033[m
			''')
		op = input(yellow + 'Entre com o numero da opção:\n\n' + cls)

		if (op == '00'):
			os.system('termux-vibrate -d 100')
			time.sleep(1)
			os.system('termux-toast -b black -c green -g middle -s Volume de mídia em 60%')
			os.system('termux-volume music 9')
			os.system(so_clear)
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
