# ftdi-playground
Controlling CBUS pins

## Building

```
docker build -t ftdi-test .
```

## Running

Connect FTDI to the computer and make sure it is listed:

```
$ ls -la /dev/ttyUSB*
crw-rw---- 1 root dialout 188, 0 gru 19 19:13 /dev/ttyUSB0
```

And run the container:

```bash
user@pc:~/ftdi-playground$ docker run --rm -it --privileged ftdi-test bash
root@ab993979c9b5:/# python3
>>> from pyftdi.ftdi import Ftdi
>>> Ftdi.show_devices()
Available interfaces:
  ftdi://ftdi:ft-x:DK0AM0V0/1   (FT230X Basic UART)
>>> f1 = Ftdi.create_from_url('ftdi://ftdi:ft-x:DK0AM0V0/1')
>>> f1.has_cbus
True
>>> f1.set_cbus_direction(0xF,0x0) # set the direction of cbus0...3 (mask 0xF -> 0b1111) to inputs (0 - input, 1 -output)
>>> f1.get_cbus_gpio()
8
```

## Checking EEPROM configuration

```
>>> from pyftdi.eeprom import FtdiEeprom
>>> from pyftdi.ftdi import Ftdi
>>> ftdi = Ftdi.create_from_url('ftdi://ftdi:ft-x:DK0AM0V0/1')
>>> eeprom = FtdiEeprom()
>>> eeprom.connect(ftdi)
>>> eeprom.dump_config()
vendor_id: 0x0403
product_id: 0x6015
type: 0x1000
self_powered: False
remote_wakeup: False
power_max: 90
has_serial: True
suspend_pull_down: False
out_isochronous: False
in_isochronous: False
manufacturer: FTDI
product: FT230X Basic UART
serial: DK0AM0V0
channel_a_driver: VCP
invert_TXD: False
invert_RXD: False
invert_RTS: False
invert_CTS: False
invert_DTR: False
invert_DSR: False
invert_DCD: False
invert_RI: False
dbus_drive: 4
dbus_schmitt: False
dbus_slow_slew: False
cbus_drive: 4
cbus_schmitt: False
cbus_slow_slew: False
cbus_func_0: TXDEN
cbus_func_1: TXLED
cbus_func_2: RXLED
cbus_func_3: SLEEP
```


## enter/exit bootloader mode

```
docker run --rm -it --privileged ftdi-test /bootloader_start.py
```

```
docker run --rm -it --privileged ftdi-test /bootloader_stop.py
```