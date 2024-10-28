from machine import Pin, I2C
import time

i2c = I2C(0, scl = Pin(17), sda = Pin(16), freq = 100000, timeout = 1000)
i2cData = None

while True:
        
    print(i2c.scan())
    
    for addr in i2c.scan():
        data = (i2c.readfrom(addr, 9))
        #data = str(data, 'UTF-8')
        #data = data.decode('utf8', 'strict')
        print(data)
    
    #time.sleep(5) 
