#!/data/data/com.termux/files/usr/bin/bash

echo -e '\n\n'
echo -e '\033[1;31mInstalando dependências...\033[m'
echo -e '\n'
apt update && apt upgrade -y
apt install -y python figlet termux-api git

pip install requests lolcat

clear
termux-vibrate -d 100
figlet TeleX | lolcat
echo -e '\n\n'
echo -e '\033[1;31mInstalando o TeleX...\033[m'
echo -e '\n'

git clone https://github.com/Visto-Preto/TeleX.git telex

cat telex/telex > /data/data/com.termux/files/usr/bin/telex
chmod 700 /data/data/com.termux/files/usr/bin/telex
cp -R telex /data/data/com.termux/files/usr/share/
rm -rf telex

termux-vibrate -d 100
echo -e '\n\n'
echo -e 'Para iniciar o Telex entre com o comando: \033[1;32mtelex\033[m'
echo -e '\n\n\n'
