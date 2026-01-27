#from datetime import datetime
from .filestorage import log, safe
from lib.globaldata import *

async def serial_read(i2c, timestamp):
    i2cData = None
    #tm = None
    #pm = None
    datensatz = [None]
    try:
        for addr in i2c.scan():
            print(addr)
            try:
                i2cData = i2c.readfrom(addr, 8, stop = True)
                print(i2cData)
                datensatz.append(i2cData)
            except:
                print("address could not read")
            
        #print(i2c.scan())
        #addr = i2c.scan()[0]
        #print(addr)
        #i2c.readfrom_into(addr, i2cData, stop = True)
        #print(i2cData)
    except:
        i2cData = None
    
    if datensatz != None:
        set_serial_data(datensatz)
        
        #i2cData= str(i2cData, 'UTF-8')
        for datenrow in datensatz:
            try:    
                i2cData = datenrow.decode('utf8', 'strict')
                print(i2cData)
            except:
                pass
        #print("Daten:\n" + i2cData)
        """
        if rxData.find("tm") == 0 and rxData.find("pm") >= 0:
            rxData = rxData.split("\r")
            
            tm = rxData[0].split(" ")
            pm = rxData[1].split(" ",18)
            pm = pm[0:-1]
            print([tm,pm])
            
            last_line = log.read_last_line()
            if (last_line == '') or (last_line == None):
                last_line = "tm 0000-00-00 00:00:00 pm 0"
            old_data = last_line.split(' ')
            old_date = old_data[1]
            old_time = old_data[2]
            new_date = tm[1]
            new_time = tm[2]
            
            if timestamp != "--.--.---- --:--:--":
                #file save at new day
                if new_date[8:10] != old_date[8:10]:
                    safe.clear()
                    safe.add(log.get_content())
                    log.clear()
                    log.add("Timestamp: " + timestamp)
                    log.add(' '.join(tm) + ' ' + ' '.join(pm))
                
                #new hour new log line 
                elif new_time[0:2] != old_time[0:2]:
                    log.add("Timestamp: " + timestamp)
                    log.add(' '.join(tm) + ' ' + ' '.join(pm))
                else:
                    pass
            else:
                pass
            
            set_serial_data([tm,pm])
        
        else:
            print('wrong data format')
        """
        
    else:
        print('no data read')
    
    return i2cData
    #return [tm,pm]
