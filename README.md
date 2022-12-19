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

```
user@pc:~/ftdi-playground$ docker run --rm -it --privileged ftdi-test bash
root@ab993979c9b5:/# python3
Python 3.8.10 (default, Nov 14 2022, 12:59:47) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from pyftdi.ftdi import Ftdi
>>> Ftdi.show_devices()
Available interfaces:
  ftdi://ftdi:232:A505TCVJ/1   (FT232R USB UART)
>>> f1 = Ftdi.create_from_url('ftdi://ftdi:232:A505TCVJ/1')
>>> f1.has_cbus
True

```