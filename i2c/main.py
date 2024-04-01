# --------------------------------------------------
# Sewage Treatment Plant - Wlan Webserver
# --------------------------------------------------

import time
from machine import Pin, I2C, SoftI2C

# global
runtime = 0


def scan_i2c(i2c):
  """
  scan for devices on i2c
  """

  # scan i2c
  i2c_addresses = i2c.scan()

  if i2c_addresses:
    #led.on()
    print('serial read...')

    # data
    i2c_data = None

    for addr in i2c_addresses:
      print("addr: ", addr)
      try:
        i2c_data = i2c.readfrom(addr, 8, stop = True)
        print(i2c_data)
      except:
        print("address could not read")


def main(led, i2c):
  """
  main
  """

  # global variables
  global runtime

  # address
  i2c_addr = 16

  # runtime print
  if runtime > 1000:
    runtime = 0
    print("life sign <3")
    led.toggle()

  # add
  runtime += 1
  print(runtime)

  # read
  try:
    read_data = i2c.readfrom(i2c_addr, 2, True)
    print("data: ", read_data)
  except:
    pass

  # buffer
  #rx_buffer = bytearray(2)
  #i2c.readfrom_into(i2c_addr, rx_buffer, True)
  #print(rx_buffer)

  # scan devices
  #scan_i2c(i2c)



if __name__ == "__main__":

  print("-- Setup I2C")

  # parameter definition
  led = Pin("LED", Pin.OUT)
  i2c = I2C(0, scl = Pin(17), sda = Pin(16), freq = 200000)
  #i2c = SoftI2C(scl = Pin(17), sda = Pin(16), freq = 200000)

  # off led
  led.off()

  # main loop
  while(1): main(led, i2c)