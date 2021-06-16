---
title: Microsoft Bluetooth Test Platform - Bluefruit Friend
description: Bluetooth Test Platform (BTP) supported hardware (Bluefruit Friend).
ms.date: 06/09/2021
ms.localizationpriority: medium
---

# Bluefruit LE UART Friend (nRF51822)

## Overview

The nRF51 is a Low Energy (LE) radio from Nordic Semiconductor capable of behaving as a HID peripheral (like a keyboard or mouse) among other things. More information can be found at [Adafruit](https://www.adafruit.com/product/2479) and through the [Nordic Semiconductor](https://www.nordicsemi.com/Products/Low-power-short-range-wireless/nRF51822) nRF51822 reference.

| Device Name | Parameter | Usage Example |
| --- | --- | --- |
| Bluefruit Friend | bluefruit | RunPairingTests.bat bluefruit |

:::image type="content" source="images/Bluefruit.png" alt-text="Photo of the Bluefruit Friend device.":::

## Supported tests

- [Pairing tests](testing-BTP-tests-pairing.md)
- [Human Interface Device (HID) tests](testing-BTP-tests-hid.md)
- [Battery tests](testing-BTP-tests-battery.md)
- [Audio & HID tests](testing-BTP-tests-audio-hid.md) (as a HID device)

## Hardware

The Bluefruit LE UART Friend can be purchased via [MCCI](https://store.mcci.com/products/bluefruit-radio-sled-for-btp).
The Bluefruit LE UART Friend can be purchased via [Adafruit](https://www.adafruit.com/product/2479) and adapted to work with the Traduci.

## Getting started

1. If purchased from MCCI, the board will arrive with a 12-pin pmod adapter already attached and ready to be programmed. If the device was purchased via Adafruit, you will need to make an adapter for the radio to attach to the Traduci. Please contact btpsupport@microsoft.com for help.
1. Install the [Bluefruit Connect app](https://learn.adafruit.com/bluefruit-le-connect) by Adafruit on an Android device or iPhone.
1. Move the switch on the Bluefruit Friend device to UART mode for firmware update.
1. Plug the Bluefruit into the Bluetooth Test Platform Traduci board port labeled 'JC' and power it on from a command prompt using TraduciCMD.exe: `TraduciCmd.exe -power 3 3`. The red LED on port JC should light up, as well as the blue LED on the Bluefruit Friend device.
1. Open the Bluefruit Connect app and select your device.
1. Wait for a prompt to update your device, then update the device. Do not power off either device until the update has completed.
1. Power off the device using TraduciCMD.exe: `TraduciCmd.exe -power 3 0`.
1. Move the switch on the Bluefruit Friend device back to CMD mode.

> [!NOTE]
> The Bluefruit device can **only** be plugged into a Bluetooth Test Platform Traduci board port labeled 'JC'.

## Features

- UART data connection
- Supports HID and other GATT based services
- Fully certified Low Energy Bluetooth 4.1 radio
- Configurable ATT database
- Small form factor, low power, surface mount module

## Troubleshooting

- No prompt to update OR blue light indicating pairing does not turn on during test passes after initial update

  - If the Bluefruit Connect app does not immediately prompt to update, factory reset the radio.
  - Place the radio back into UART mode via the switch.
  - Connect pin 5 on the 12-pin adapter to GND
  - Connect pin 6 on the 12-pin adapter to 3.3V PWR. You can use the Traduci for this process only connecting pins 5 and 6 and the power commands from the setup above. Do not plug the radio into the Traduci directly.
  - Once radio is powered on, connect a jumper wire from pin 11 (GND) on the 12-pin adapter to pin 8 (DFU) on the Bluefruit board. A male to female jumper wire is easiest to use. Hold the connection for approximately 4 seconds. The red LED should light up, then the blue LED. The lights should flash back and forth. Once the blue LED stops flashing, break the connection. If you maintain the connection, the system will continue to reset the chip. Pull the jumper once the red light is solid.
  - Follow from step 5 above.

If still not working, email btpsupport@microsoft.com
