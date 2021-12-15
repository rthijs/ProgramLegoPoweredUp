# Program Lego Powered Up

I don't like controlling my Liebherr 9800 model with the Lego Power+ Android app. Controls on a touch screen just plain suck. Also I'd like another programming language than the graphical blocks Lego uses.

Eventually I hope to use the [Raspberry Pi Zero 2 W](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/) in a custom enclosure with fysical knobs to controll my Lego sets.

The development I'll do on a Raspberry Pi 4 with 4 gigs of ram. The low power Zero does not make a great development computer.

The Lego Powered Up brick connects with Bluetooth Low Engergy (BLE) and this is available for most Raspberry Pi's.

## Bluetooth Low Energy
According to `apt search` the `bluez` package for Bluetooth support is at version 5.50-1.2. To install the latest version, currently 5.62, I followed instructions from [here](https://www.argenox.com/library/bluetooth-low-energy/using-raspberry-pi-ble/). 

`hciconfig` shows the hci0 interface is up and running.

![hciconfig](.assets/hciconfig-output.png)

An lescan shows our Lego Technic Hub:

![lescan](.assets/lescan-output.png)

## Lego BLE Wireless Protocol

If you clone [this](https://github.com/LEGO/lego-ble-wireless-protocol-docs) repository (or download the zip), you can locally browse everything you need to know about how to interact with the Lego hubs. 

![Lego BLE docs](.assets/legobledocs.png)

Let's not dive into the deep just yet. There is a [Python library](https://github.com/undera/pylgbst) to interact with the hubs.

## Pylgbst

The author of this library, [Andrey Pokhilko](https://github.com/undera), suggests starting with looking into his [`demo.py`](https://github.com/undera/pylgbst/blob/master/examples/demo.py) file.

There is also a [MagPi article](https://magpi.raspberrypi.com/articles/hack-lego-boost-with-raspberry-pi) that takes you step by step towards getting to control your Lego hub.


# Links
 - [about powered up](https://www.lego.com/en-us/themes/powered-up/about)
 - [magpi artikel](https://magpi.raspberrypi.com/articles/hack-lego-boost-with-raspberry-pi)
 - [magpi download](https://magpi.raspberrypi.com/issues/80/pdf/download) --> uittreksel zit al in deze repo

 - [BOOSTrevenge](https://github.com/JorgePe/BOOSTreveng)
 - [Lego BLE wireless protocol docs](https://github.com/LEGO/lego-ble-wireless-protocol-docs)
 - [issue discovering devices](https://github.com/undera/pylgbst/issues/7)
 - [pylgbst](https://github.com/undera/pylgbst) --> dit lijkt de compleetste

 - [using ble devices with a Raspberry Pi](https://www.argenox.com/library/bluetooth-low-energy/using-raspberry-pi-ble/)

  - [Control Bluetooth LE Devices From a Raspberry Pi
](https://www.instructables.com/Control-Bluetooth-LE-Devices-From-A-Raspberry-Pi/)