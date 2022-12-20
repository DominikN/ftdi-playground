FROM ubuntu:20.04

SHELL ["/bin/bash", "-c"]

# official releases are only for intel archs, so we need to build stm32flash from sources
RUN apt-get update && apt-get install -y \
		git \
        python3 \
        python3-pip \
        libusb-1.0

RUN pip3 install pyftdi

COPY bootloader_start.py /
COPY bootloader_stop.py /
COPY ftdi-eeprom-conf.py /