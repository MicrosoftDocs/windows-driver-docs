---
title: Microsoft Bluetooth Test Platform - Bluefruit Feather
description: Bluetooth Test Platform (BTP) supported hardware (Bluefruit Feather).
ms.date: 09/29/2023
---

# Bluefruit Feather (nRF52840)

## Overview

The nRF52840 is a Low Energy (LE) radio from Nordic Semiconductor capable of behaving as a HID peripheral, like a keyboard or mouse, among other things. More information can be found at [Adafruit](https://www.adafruit.com/product/4062) and through the [Nordic Semiconductor](https://www.nordicsemi.com/Products/nRF52840) nRF52840 reference.

| Device Name | Parameter | Usage Example |
| --- | --- | --- |
| Bluefruit Feather | bluefruit52 | RunPairingTests.bat bluefruit52 |

:::image type="content" source="images/BluefruitFeather.png" alt-text="Photo of the Bluefruit Feather nRF52840 device.":::

## Supported tests

- [Pairing tests](testing-BTP-tests-pairing.md)
- [Human Interface Device (HID) tests](testing-BTP-tests-hid.md)
- [Battery tests](testing-BTP-tests-battery.md)
- [Audio & HID tests](testing-BTP-tests-audio-hid.md) (as a HID device)
- [Power State HID tests](testing-BTP-tests-power-state-hid.md)
- [Wi-Fi coexistence tests](testing-BTP-tests-wifi.md) (as a HID device)

## Hardware

The Bluefruit LE UART Friend can be purchased via [Adafruit](https://www.adafruit.com/product/4062). It requires a micro-USB cable.

> [!NOTE]
> The Bluefruit Feather device is supported via USB serial only at this time.

## Getting Started

### Updating the bootloader

When you first get new hardware, the bootloader needs to be updated. You should only need to do this once for each Bluefruit Feather device.

1. Plug the Bluefruit Feather device into a PC via a micro-USB cable.
1. Follow the [Adafruit](https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather/update-bootloader) instructions to update the bootloader.
    - Use version 0.6.3_s140_6.1.1 of the bootloader.
    - The correct package to download should have the name "feather_nrf52840_express_bootloader-0.6.3_s140_6.1.1.zip". It can be found on the [0.6.3 release page](https://github.com/adafruit/Adafruit_nRF52_Bootloader/releases/tag/0.6.3).

### Updating the firmware

You need to update the firmware for each release of BTP.

1. Acquire and setup the Arduino command line interface.
    1. Download the latest version of the [arduino-cli](https://arduino.github.io/arduino-cli/latest/installation/#download).
    2. If not done already, add the arduino-cli to your [PATH variable](/windows-server/administration/windows-commands/path).
    3. To acquire the Adafruit board packages, run the following from a command prompt:

    ```console
    arduino-cli config init
    arduino-cli core update-index
    arduino-cli core update-index --additional-urls https://adafruit.github.io/arduino-board-index/package_adafruit_index.json
    arduino-cli core install adafruit:nrf52 --additional-urls https://adafruit.github.io/arduino-board-index/package_adafruit_index.json
    ```

1. Identify the COM port assigned to the Bluefruit Feather by running the following from a command prompt:

    ```console
    arduino-cli board list
    ```

1. Upload the firmware to the Bluefruit Feather by running the following from a command prompt, and replacing the X in COMX to the COM port number identified in the previous step:

    ```console
    arduino-cli upload -p COMX --fqbn adafruit:nrf52:feather52840 --input-file C:\BTP\<version>\DeviceFirmware\BtpBluefruit_nRF52840.ino.zip
    ```

## Features

- UART data connection
- Supports HID and other GATT based services
- Fully certified Low Energy Bluetooth 5.0 radio
- Configurable ATT database
- Small form factor, low power, surface mount module

> [!Note]
> The Bluefruit Feather is not currently supported for use with the Traduci.

## Trouble shooting

- If the tests are failing consistently and the firmware of the Bluefruit Feather has not been updated recently, check that the firmware is a supported version by following step 1. If the version is older, download the bootloader and install the latest firmware.
