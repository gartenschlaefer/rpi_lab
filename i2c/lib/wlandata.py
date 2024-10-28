#ssid = 'Wait-for-it'
#password = 'seuttergasse2021'
ssid = 'Schuetzenmuehle'
password = 'Neuhof13'

#staticIP = '10.0.0.112'
#routerIP = '10.0.0.138'
staticIP = '192.168.1.112'
routerIP = '192.168.1.1'
gateway = '255.255.255.0'
port = 80

def set_device_ip(input):
    global staticIP
    staticIP = input
def get_device_ip():
    return staticIP
