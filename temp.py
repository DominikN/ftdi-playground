#!/usr/bin/env python3

import time

from pyftdi.ftdi import Ftdi
from pyftdi.eeprom import FtdiEeprom

device = 'ftdi://ftdi:ft-x:DK0AM0V0/1'

ftdi = Ftdi()
ftdi.open_from_url(url=device)

# Set mode manually
ftdi.set_bitmode(0, Ftdi.BitMode.CBUS)
# ^^^^^^^^^^^^^

ftdi.set_cbus_direction(0b1111,0b1011)

while True:
    print('1011')
    ftdi.set_cbus_gpio(0b1011)
    time.sleep(1)

    print('0000')
    ftdi.set_cbus_gpio(0b0000)
    time.sleep(1)