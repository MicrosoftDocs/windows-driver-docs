---
title: Microsoft Bluetooth Test Platform - Model 2433 ESP32
description: Bluetooth Test Platform (BTP) supported hardware (ESP32).
ms.date: 06/09/2021
ms.localizationpriority: medium
---

# Model 2433 ESP32

## Overview

The Model 2433 ESP32 is a custom ESP32 board with a 12-pin adapter fit for the Traduci that exercises Wi-Fi connections for BTP. The ESP32 is a microcontorller with integrated Wi-Fi and dual-mode Bluetooth designed for use in IOT devices. More information can be found via the ESP32 page from [**Espressif**](https://www.espressif.com/en/products/socs/esp32).
The Model 2433 ESP32 allows the ESP32 to be utilized as a Traduci sled device. More information can be found via the Model 2433 ESP32 page from [**MCCI**](https://store.mcci.com/products/esp32-sled) or [**Digilent**](https://store.digilentinc.com/pmod-esp32-wireless-communication-module).

| Device Name | Parameter | Usage Example |
| --- | --- | --- |
| ESP32 Wi-Fi | esp32wifi | RunWiFiCoexScenarioTests.bat rn52 esp32wifi |

:::image type="content" source="images/ESP32.png" alt-text="Photo of the Model 2433 ESP32.":::

## Suported Tests

- [Wi-Fi coexistence tests](testing-BTP-tests-wifi.md) (as an Access Point device)

### ESP32 Device on BTP-compatible sled

:::image type="content" source="images/Traduci_and_ESP32.jpg" alt-text="Photo of the Model 2433 ESP32 device on a sled.":::

## Hardware

The ESP32 can be purchased via [MCCI](https://store.mcci.com/products/esp32-sled/)

The ESP32 can also be purchased via [Digilent](https://store.digilentinc.com/pmod-esp32-wireless-communication-module/).

USB Serial to UART breakout board equivalent to [Sparkfun FT232RL](https://www.sparkfun.com/products/12731) needed for first time Firmware Update.

## Getting Started

If the ESP32 has already been updated, skip to [Updating ESP32 Firmware via Traduci.cmd](testing-BTP-hw-esp32.md#updating-esp32-firmware-via-traducicmd)

> [!NOTE]
> The ESP32 device can **only** be plugged into the Traduci board 12-pin port labeled 'JD'.

## Updating ESP32 Firmware manually

This is required for first time setup of an ESP32 radio for use with the BTP Wi-Fi Coexistence tests. After first time setup, firmware updates to the device sled can be done via [Traduci.cmd](testing-BTP-hw-esp32.md#updating-esp32-firmware-via-traducicmd).  

1.  Acquire and setup the Arduino command line interface.
    1. Download the latest version of the [arduino-cli](https://arduino.github.io/arduino-cli/latest/installation/#download).
    1. If not done already, add the arduino-cli to your [PATH variable](/windows-server/administration/windows-commands/path).
    1. To aquire the ESP32 board packages, run the following from a cmd prompt:

        ```console
        arduino-cli config init
        arduino-cli core update-index
        arduino-cli core update-index --additional-urls https://dl.espressif.com/dl/package_esp32_index.json
        arduino-cli core install esp32:esp32 --additional-urls https://dl.espressif.com/dl/package_esp32_index.json
        ```

1. Connect the Hardware.
Using a USB Serial to UART board (like the one shown below) & jumper wires
    :::image type="content" source="images/ESP32_and_UART.png" alt-text="ESP32 with USB to UART board.":::

    1. Connect the GND of the Serial board to the GND of the ESP32
    1. Connect the RX of the Serial board to the TX of the ESP32
    1. Connect the TX of the Serial board to the RX of the ESP32
    1. Connect the USB Serial to UART board to the PC you installed the Arduino CLI to.
    1. Connect the ESP32 device to Port JD on the Traduci for power delivery.
    1. Power on the ESP32 via the Traduci using TraduciCMD.exe: `TraduciCmd.exe -power 4 3`
        :::image type="content" source="images/Traduci_and_ESP32.jpg" alt-text="ESP32 powered on by Traduci.":::
    1. Run `arduino-cli board list` to identify the COM port associated with the UART to USB Serial board.
    1. Move SW1 to the ON position to switch the ESP32 into boot mode.
        :::image type="content" source="images/ESP32Boot.png" alt-text="ESP32 enable boot mode.":::

1. Upload the firmware to the Bluefruit Feather by running the following from a cmd prompt, and replacing the X in COMX to the COM port number identified in the previous step:

    ```console
    arduino-cli upload -p COMX --fqbn esp32:esp32:esp32 --input-file C:\BTP\<version>\DeviceFirmware\WiFi-ESP32.ino.bin
    ```

    1. Wait for "Connecting ….____...." to show  on the terminal.
    1. Press BTN1 to reset the board.
        :::image type="content" source="images/ESP32Reset.png" alt-text="ESP32 reset button.":::
    1. Wait for "ESP32 firmware is up to date" to show on the terminal and indicate the process is done.
    1. Move the SW1 to the OFF position to exit boot mode and press BTN1 again to restart the board and the program.

## Updating ESP32 Firmware via Traduci.cmd

If the ESP32 already has BTP compatible firmware installed, future updates can be installed via the Traduci. Plug the ESP32 into port JD and run the following command from an elevated cmd prompt:

```console
TraduciCmd.exe -updateesp32firmware
```

This flashing process does not require the use of a UART to USB Serial board. This will not work if the ESP32 has not previously been provisioned with BTP compatible firmware via the [manual instructions](testing-BTP-hw-esp32.md#updating-esp32-firmware-manually)

## Features

- Wi-Fi, Bluetooth LE, and Bluetooth communication available
- 20.5 dBm output power at the antenna
- Custom firmware to enable updates delivered through the Traduci
- 12-pin Pmod connector with SPI and UART interfaces
- Supports creation of Wi-Fi soft access points
- Supports http web server capabilities
