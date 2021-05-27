---
title: Microsoft Bluetooth Test Platform - Bluefruit Feather
description: Bluetooth Test Platform (BTP) supported hardware (Bluefruit Feather).
ms.date: 5/24/2021
ms.localizationpriority: medium

---

# Bluefruit Feather (nRF51822)

The nRF51822 is a Low Energy (LE) radio from Nordic Semiconductor capable of behaving as a HID peripheral (like a keyboard or mouse) among other things. It is currently supported by the BTP pairing and HID tests. More information can be found at [Adafruit](https://www.adafruit.com/product/2829) and through the [Nordic Semiconductor](https://www.nordicsemi.com/Products/Low-power-short-range-wireless/nRF51822) nRF51822 reference.


| Device | Capabilities | Parameter |
| --- | --- | --- |
| rf52 | Low Energy (LE) radio | rf52 (ex. RunPairingTests.bat bluerf52fruit) |


## Suported Tests
    [Pairing tests](testing-BTP-tests-pairing.md)
    [Human Interface Device tests](testing-BTP-tests-hid.md) 
    [Audio & HID tests](testing-BTP-tests-audio-hid.md)

## Hardware

The Bluefruit LE UART Friend can be purchased via [Adafruit](https://www.adafruit.com/product/2479)
Requires a micro-USB cable.

> [!NOTE]
> The Bluefruit Feather device is supported via USB serial only at this time. 


## Getting Started 

For first time setup the bootloader needs to be updated. This step is not required for furture firmware upadtes.

1.  Follow the [Adafruit](https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather/update-bootloader) instructions to update the bootloader. The correct package to download should have a name similar to "feather_nrf52840_express_bootloader-<version>.zip" where the version number should be equal or great to 0.3.2_s140_6.1.1. 
If you are having issues, try using version 0.3.2_s140_6.1.1 which is known and verified to work with the BTP tests.

2.  Acquire and setup the Arduino-CLI

Download the latest version of the [Arduino-CLI](https://arduino.github.io/arduino-cli/latest/installation/#download)
If not done already, add the Arduino-cli to your [PATH variable](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/path).
To aquire the Adafruit board packages, run the following from a cmd prompt:
```console
arduino-cli config init
arduino-cli core update-index
arduino-cli core update-index --additional-urls https://adafruit.github.io/arduino-board-index/package_adafruit_index.json
arduino-cli core install esp32:esp32 --additional-urls https://adafruit.github.io/arduino-board-index/package_adafruit_index.json
```

3. Identify the COM port assigned to the Bluefruit Feather

From an cmd prompt run: `arduino-cli board list`
and note the COM port being used.

4. Upload the firmware to the Bluefruit Feather

From a cmd prompt run `arduino-cli upload -p COMX --fqbn adafruit:nrf52:feather52840 --input-file C:\BTP\<version>\DeviceFirmware\BtpBluefruit_nRF52840.ino.zip` where the x in COMX indicates the COM port identified in step 3.


## Features

- UART data connection
- Supports HID and other GATT based services 
- Fully certified Low Energy Bluetooth 5.0 radio
- Configurable ATT database
- Small form factor, low power, surface mount module
