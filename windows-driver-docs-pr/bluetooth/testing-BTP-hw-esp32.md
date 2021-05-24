---
title: Microsoft Bluetooth Test Platform - Model 2433 ESP32
description: Bluetooth Test Platform (BTP) supported hardware (ESP32).
ms.date: 5/24/2021
ms.localizationpriority: medium

---

# Model 2433 ESP32

## Overview

The Model 2433 ESP32 is a custom ESP32 board with a 12 pin adapter fit for the Traduci that exercises WiFi connections for BTP. For more about the benefits of the ESP32, refer to the [WiFi Capable Devices](testing-BTP-hw-wifi.md).
  
This section will cover how to set up and use a Model 2433 ESP32 for testing with BTP.

![Photo of the Model 2433 ESP32](images/ESP32.png)

##  Required Hardware 

The ESP32 can be purchased via [MCCI] (https://store.mcci.com/products/esp32-sled/)

The ESP32 can also be purchased via [Digilent](https://store.digilentinc.com/pmod-esp32-wireless-communication-module/).

USB Serial to UART breakout board equivalent to [Sparkfun FT232RL](https://www.sparkfun.com/products/12731)


## Getting Started 

If the ESP32 has already been updated, skip to [Updating ESP32 Firmware via Traduci.cmd](testing-BTP-hw-esp32.md/#Updating-ESP32-Firmware-via-Traduci.cmd)

## Updating ESP32 Firmware manually

This is required for first time setup of an ESP32 radio for use with the BTP Wi-Fi Coexistence tests. After first time setup, firmware updates to the device sled can be done via [Traduci.cmd](testing-BTP-hw-esp32.md/#Updating-ESP32-Firmware-via-Traduci.cmd).  

1. Acquire and setup the Arduino-CLI
Download the latest version of the [Arduino-CLI](https://arduino.github.io/arduino-cli/latest/installation/#download)

If not done already, add the Arduino-cli to your [PATH variable](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/path).
To aquire the ESP32 board packages, run the following from a cmd prompt:
```console
arduino-cli config init
arduino-cli core update-index
arduino-cli core update-index --additional-urls https://dl.espressif.com/dl/package_esp32_index.json
arduino-cli core install esp32:esp32 --additional-urls https://dl.espressif.com/dl/package_esp32_index.json
```

2. Connect the Hardware and 
    Using a USB Serial to UART board (like the one shown below) ![ESP32 with USB to UART board](images/ESP32_and_UART.png)
    1. Connect the GND of the Serial board to the GND of the ESP32
    2. Connect the RX of the Serial board to the TX of the ESP32
    3. Connect the TX of the Serial board to the RX of the ESP32
    4. Connect the USB Serial to UART board to the PC you installed the Arduino CLI to.
    4. Connect the ESP32 device to Port JD on the Traduci for power delivery.
    5. Power on the ESP32 via the Traduci using TraduciCMD.exe: `TraduciCmd.exe -power 4 3`
    ![ESP32 powered on by Traduci](images/Traduci_and_ESP32.jpg)


Run `arduino-cli board list` to detect which COM port is associated with the UART to USB Serial board.

Once everything is wired correctly, and the COM port is identified, switch the ESP32 into boot mode by moving SW1 to the ON position.
![ESP32 enable boot mode](images/ESP32Boot.png)

3. Upload the Firmware
Run `arduino-cli upload -p <COM port from previous step here> --fqbn esp32:esp32:esp32 --input-file C:\BTP\<version>\DeviceFirmware\WiFi-ESP32.ino.bin`

Wait for “Connecting ….____....” to show up on the terminal.

Press BTN1 to reset the board.
![ESP32 reset button](images/ESP32Reset.png)

Once the upload is done, switch boot mode off by moving SW1 to the OFF position.

Press BTN1 again to reset the board and start the program.

## Updating ESP32 Firmware via Traduci.cmd

If the ESP32 already has BTP compatible firmware installed, future updates can be installed via the Traduci. Plug the ESP32 into port JD and run the following command from an elevated cmd prompt:
- `TraduciCmd.exe -updateesp32firmware`

This flashing process does not require the use of a UART to USB Serial board. This will not work if the ESP32 has not previously been provisioned with BTP compatible firmware via the [manual instructions](testing-BTP-hw-esp32.md/#Updating-ESP32-Firmware-manually)






