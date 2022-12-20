#!/usr/bin/python3

from pyftdi.ftdi import Ftdi
import time

f1 = Ftdi.create_from_url('ftdi://ftdi:ft-x:DK0AM0V0/1')

# CBUS0 - BOOT0
# CBUS1 - RST

f1.set_cbus_direction(0b11,0b11) # set CBUS0 and CBUS1 to output
time.sleep(0.1)
f1.set_cbus_gpio(0b10) #set CBUS0 to 0 and RST to 1
time.sleep(0.1)
f1.set_cbus_gpio(0b00) #set CBUS0 to 0 and RST to 0
time.sleep(0.1)
f1.set_cbus_direction(0b11,0b00) # set CBUS0 and CBUS1 to input