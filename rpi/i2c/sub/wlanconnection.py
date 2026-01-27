'''
  - Verbindung mit WLAN
  - Zeitzonen und aktuelle Zeit
  - Formatierung Zeit- und Datum
'''
import network
import time
import rp2
import ntptime
import urequests as requests
from lib.wlandata import *

# Einbinden in das eigene WLAN
class WiFi:
    
    zeitzone = 3600 # Zeitverschiebung in Sekunden
    
    def __init__(self):
        rp2.country("AT")
        self.wlan = network.WLAN(network.STA_IF)
    
    def set_zeitzone(self,zone):
        self.zeitzone = zone
    
    def get_zeitzone(self):
        return self.zeitzone
    
    def get_wlan(self):
        return self.wlan
    
    def wlan_scan(self):
        print('available connections ', self.wlan.scan())
        return self.wlan.scan()

    def connect_wlan(self, led, timeout = 10000):
        if self.wlan.isconnected():
            self.disconnect_wlan()
        print('connect to wifi...')
        self.wlan.active(True)
        self.wlan.config(pm = 0xa11140) # Disable power-save mode
        self.wlan.ifconfig((staticIP, gateway, routerIP, routerIP)) #IP, Netmask, Gateway, DNS
        self.wlan.connect(ssid, password)
        
        start = time.ticks_ms()
        while self.wlan.isconnected() == False and start + timeout > time.ticks_ms():
            print('waiting for connection...')
            led.toggle()
            time.sleep(1)
        led.off()
        
        if self.wlan.isconnected() == False: #self.wlan.status() != 3
            print('connection failed')
            #raise RuntimeError('network connection failed')
        else:
            self.is_connected()
            set_device_ip(self.get_ip()[0])
    
    def disconnect_wlan(self):
        print('disconnect from wifi...')
        self.wlan.disconnect()
        self.wlan.active(False)
        self.is_disconnected()
    
    def is_connected(self):
        print('connected to wifi')
    
    def is_disconnected(self):
        print('disconnected from wifi')
    
    def get_status(self):
        print('wifi status ', self.wlan.status())
        return self.wlan.status()
    
    def get_connection(self):
        print('wifi connection ', self.wlan.isconnected())
        return self.wlan.isconnected()
    
    def get_ip(self):
        conf = self.wlan.ifconfig() # (ip, subnet, gateway, dns)
        #print('ip = ' + conf[0])
        print('IP config ', conf)
        return conf
    
    def get_ssid(self):
        print('essid ', self.wlan.config('essid'))
        return self.wlan.config('essid')
    
    def get_request(self, url):
        print('url ', requests.get(url))
        return requests.get(url)
    
     ###### Zeitverschiebung #######
    def update_timechange(self, zeit):
        zeitString = time.localtime(zeit)
        if (zeitString[1] > 3) and (zeitString[1] < 11):
            self.set_zeitzone(7200)
        else:
            self.set_zeitzone(3600)
    
    def start_server(self, asyncio, serve_client, timelog):
        homeserver = None
        if self.get_connection():
            ip = get_device_ip()
            
            try:
                print('setting up socket...')
                asyncio.open_connection(ip, port)
                print('listening on ', ip)
                
                print('setting up webserver...')
                homeserver = asyncio.create_task(asyncio.start_server(serve_client, ip, port, backlog = timelog))
                print('ready to read')
            except:
                print('webserver error')
                homeserver = None
        else:
            print('no wifi connection')
        return homeserver
    
    ###### Zeit und Datum #######
    # Aktuelle Zeit
    # Sekunden seit 2000-01-01 00:00:00 UTC
    @classmethod
    def get_zeit(cls):
        try:
            ntptime.settime()
        except:
            return None
        return time.mktime(time.localtime())
    
    # Korrigiert 'zeit' um Zeitzone, wenn 'zeit' nicht mitgegeben
    # wird, wird die aktuelle Zeit zurückgegeben 
    @classmethod
    def get_zeit_lokal(cls, zeit = None):
        if zeit:
            return zeit + cls.zeitzone
        else:
            zeit = cls.get_zeit()
            if zeit:
                return zeit + cls.zeitzone
            else:
                return None
    

# Formatierungsfunktionen für Textausgabe
# von Datum und Zeit

# tt.mm.yyyy
def datum_text(zeit):
    zeitString = time.localtime(zeit)
    return "{:02d}.{:02d}.{:04d}".format(zeitString[2],zeitString[1],zeitString[0])

# hh:mm:ss
def zeit_text(zeit):
    zeitString = time.localtime(zeit)
    return "{:02d}:{:02d}:{:02d}".format(zeitString[3],zeitString[4],zeitString[5])

# tt.mm.yyyy hh:mm:ss
def datum_zeit_text(zeit):
    if zeit:
        return datum_text(zeit) + " " + zeit_text(zeit)
    else:
        return "--.--.---- --:--:--"
