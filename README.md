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