#!/data/data/com.termux/files/usr/bin/bash

clear
figlet TeleX | lolcat
echo -e '\n\n'
echo -e '\033[1;31mInstalando...\033[m'
echo -e '\n'

git clone https://github.com/Visto-Preto/TeleX.git telex

cat telex/telex > /data/data/com.termux/files/usr/bin/telex
chmod 700 /data/data/com.termux/files/usr/bin/telex
cp -R telex /data/data/com.termux/files/usr/share/
echo -e '\n\n'
echo -e 'Para iniciar o Telex entre com o comando: \033[1;32mtelex\033[m'
