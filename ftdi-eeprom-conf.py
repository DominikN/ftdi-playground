#!/usr/bin/env python3

from pyftdi.ftdi import Ftdi
from pyftdi.eeprom import FtdiEeprom

device = 'ftdi://ftdi:ft-x:DK0AM0V0/1'

ftdi = Ftdi()
ftdi.open_from_url(url=device)

eeprom = FtdiEeprom()
eeprom.connect(ftdi)

# eeprom.set_manufacturer_name('FTDI')
# eeprom.set_product_name('FT230X Basic UART')
# eeprom.set_serial_number('DK0AM0V0')

# eeprom.set_property('self_powered', True)
# eeprom.set_property('remote_wakeup', True)
# eeprom.set_property('power_max', 90)
# eeprom.set_property('has_serial', True)
# eeprom.set_property('suspend_pull_down', False)
# eeprom.set_property('out_isochronous', False)
# eeprom.set_property('in_isochronous', False)
# eeprom.set_property('channel_a_driver', 'VCP')
# eeprom.set_property('invert_TXD', False)
# eeprom.set_property('invert_RXD', False)
# eeprom.set_property('invert_RTS', False)
# eeprom.set_property('invert_CTS', False)
# eeprom.set_property('invert_DTR', False)
# eeprom.set_property('invert_DSR', False)
# eeprom.set_property('invert_DCD', False)
# eeprom.set_property('invert_RI', False)
# eeprom.set_property('dbus_drive', 4)
# eeprom.set_property('dbus_schmitt', False)
# eeprom.set_property('dbus_slow_slew', False)
# eeprom.set_property('cbus_drive', 4)
# eeprom.set_property('cbus_schmitt', False)
# eeprom.set_property('cbus_slow_slew', False)
# eeprom.set_property('cbus_func_0', 'GPIO')
# eeprom.set_property('cbus_func_1', 'GPIO')
# eeprom.set_property('cbus_func_2', 'RXLED')
# eeprom.set_property('cbus_func_3', 'SLEEP')

eeprom.set_property('cbus_func_0','GPIO')
eeprom.set_property('cbus_func_1','GPIO')

eeprom.commit(False)
eeprom.reset_device()
