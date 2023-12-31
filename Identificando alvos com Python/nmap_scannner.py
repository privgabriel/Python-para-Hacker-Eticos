import sys
try:
    import nmap
except:
    sys.exit("[!] Instale a biblioteca nmap com o comando: pip install python-nmap")

# Validator Argumento
if len(sys.argv) != 3:
    sys.exit("Forneça dois argumentos, sendo o primeiro o alvo, o segundo as portas")

ports = str(sys.argv[2]) # Variável da porta no argumento 2
addrs = str(sys.argv[1]) # Variável da porta no argumento 1
portlist = ports.split(',')
print(portlist) # Printa as portas

scanner = nmap.PortScanner()
scanner.scan(addrs, ports)
print(scanner.all_hosts()) # Printa o hostname desclarado

# Verifica se a porta está aberta ou fechada.
for host in scanner.all_hosts():
    print(scanner[host])
    for port in portlist:
        state = scanner[host]['tcp'][int(port)]['state']
        print(" [*] " + host + " tcp/" + port + " " + state)
