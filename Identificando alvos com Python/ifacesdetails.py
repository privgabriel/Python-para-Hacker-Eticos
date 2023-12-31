import sys
try:
    import netifaces
except:
    sys.exit("[!] Instale a biblioteca netifaces com o comando: pip install netifaces")

gateways = {}
network_ifaces={}

# Encontra todas as interfaces relevantes para esse sistema
def get_interfaces():
    interfaces = netifaces.interfaces()
    return interfaces

# Função identifica os gateways e os retorna como um dicionário
def get_gateways():
    gateway_dict = {}
    gws = netifaces.gateways()
    for gw in gws:
        try:
            gateway_iface = gws[gw][netifaces.AF_INET]
            gateway_ip, iface = gateway_iface[0], gateway_iface[1]
            gw_list =[gateway_ip, iface]
            gateway_dict[gw]=gw_list
        except:
            pass
    return gateway_dict

# Função identifica os endereços para cada interface, que inclui o endereço MAC, endereço de interface (tipicamente IPv4), endereço de broadcast e máscara de rede.
def get_addresses(interface):
    addrs = netifaces.ifaddresses(interface)
    link_addr = addrs[netifaces.AF_LINK]
    iface_addrs = addrs[netifaces.AF_INET]
    iface_dict = iface_addrs[0]
    link_dict = link_addr[0]
    hwaddr = link_dict.get('addr')
    iface_addr = iface_dict.get('addr')
    iface_broadcast = iface_dict.get('broadcast')
    iface_netmask = iface_dict.get('netmask')
    return hwaddr, iface_addr, iface_broadcast, iface_netmask

# Função que identifica o gateway IP a partir do dicionário fornecido pela função get_gateways para a interface
def get_networks(gateways_dict):
    networks_dict = {}
    for key, value in gateways.iteritems():
        gateway_ip, iface = value[0], value[1]
        hwaddress, addr, broadcast, netmask = get_addresses(iface)
        network = {'gateway': gateway_ip, 'hwaddr' : hwaddress, 'addr' : addr, 'broadcast' : broadcast, 'netmask' : netmask}
        networks_dict[iface] = network
    return networks_dict


gateways = get_gateways()
network_ifaces = get_networks(gateways)
print(network_ifaces)
