
import sys, os, time
# ________________________________
so = sys.platform
so_clear = ''

if (so == 'linux'):
	so_clear = 'clear'
elif(so == 'win32'):
	so_clear = 'cls'
# ________________________________

__author__ = 'VistoPreto'
__update__ = '24/03/2022'
__version__ = '0.0001'

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
def existe():
	if os.path.isfile('channels.db'):
		ver()
	else:
		os.system(so_clear)
		print()
		print('Você não possue canais cadrastado\nFavor adicione canais na lista')		
		print()
		time.sleep(3)
		start_menu()




def ver():
	db = open('channels.db', 'r')
	ver_db = db.read()
	db.close()
	l = ver_db.split('\n')
	l = l[:-1]

	ll = []
	lc = []

	os.system(so_clear)
	print()

	while len(l) > 0:
		ll += l[1:2]
		lc += l[0:1]
		t = len(l)
		l = l[2:t]

	cont = 1
	for i in lc:
		print(str(cont) + ']	' + i)
		cont += 1

	print()
	print('0]	Voltar') 
	print('00]	Sair') 
	op_ver = input('\nEntre com o numero da opção:\n\n')
	op_id = op_ver
	if op_ver == '0':
		start_menu()
	elif op_ver == '00':
		os.system(so_clear)
		sys.exit()
	elif op_ver == op_id:
		os.system(so_clear)
		print()
		print(ll[(int(op_id) - 1)])
		print()
		time.sleep(2)
		ver()



def adicionar():
	while True:
		os.system(so_clear)
		print()
		channel = input('''
Qual o nome do chanal?

0]	Voltar
00]	Sair

''')

		if channel == '0':
			break
		elif channel == '00':
			os.system(so_clear)
			sys.exit()
		os.system(so_clear)
		link = input('''
Qual o nome do chanal?

0]	Voltar
00]	Sair

''')

		if link == '0':
			break
		elif link == '00':
			os.system(so_clear)
			sys.exit()
		else:
			with open('channels.db', 'a') as db:
				db.write(channel)
				db.write('\n') 
				db.write(link)
				db.write("\n") 
			os.system(so_clear)
			print('O canal', channel, 'foi adicionado a lista')
			time.sleep(2)

# ________________________________

def start_menu():
	while True:
		os.system(so_clear)
		print('''
1]	Ver lista de canais
2]	Adicionar canais
3]	Excluir canais

00]	Sair
			''')
		op = input('Entre com o numero da opção:\n\n')

		if (op == '00'):
			break
		elif (op == '1'):
			existe()
			break
		elif (op == '2'):
			adicionar()
		elif (op == '3'):
			print(3)


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
