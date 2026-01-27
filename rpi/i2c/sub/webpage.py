from lib.globaldata import *
from lib.wlandata import *
from .wlanconnection import WiFi, datum_zeit_text

# Homepage
# --------------------------------------------------
def main_homepage():
    data = get_serial_data()
    localdatetime = datum_zeit_text(WiFi.get_zeit_lokal(None))
    refreshtime = 10
    ip = get_device_ip()
    
    html = """
    <!DOCTYPE html>
    <html lang="de">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="refresh" content="{}">
            <title>Sewage Treatment Plant</title>
        </head>
        <body>
            <h1>Kläranlage</h1>
            <h4>Datum: ...<br>Uhrzeit: ...</h4>
            <p>
                <strong>Daten = {}</strong><br>
                <br>
                LOG-File: <a href="http://{}/log">http://{}/log</a><br>
                <br>
                {}
            </p>
        </body>
    </html>
    """.format(refreshtime, data, ip, ip, localdatetime)
    
    return html

def data_page():
    
    data = get_serial_data() 
    #datarow = ' '.join(data[0][:]) + ' ' + ' '.join(data[1][:])
    
    html = """
    <!DOCTYPE html>
    <html lang=de>
        <head>
            <meta charset="UTF-8" />
            <meta http-equiv="refresh" content="10">
            <title>data</title>
        </head>
        <body>
            <p>
                {}
            </p>
        </body>
    </html>
    """.format(data)
    
    return html
