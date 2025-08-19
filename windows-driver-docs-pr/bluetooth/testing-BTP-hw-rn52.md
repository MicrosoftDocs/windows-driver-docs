---
title: Microsoft Bluetooth Test Platform - RN52 - Audio-Capable Peripheral Radios
description: Bluetooth Test Platform (BTP) supported hardware (RN52).
ms.date: 01/07/2025
ms.topic: overview
---

# RN52 device

## Overview

The RN52 is a Bluetooth basic rate (BR) radio from Roving Networks capable of behaving as an audio peripheral, such as a speaker or headset. To aid with validation, this sled routes the audio out data from the radio to an audio codec and audio processing field-programmable gate array (FPGA) on the Traduci. For more information, see the [MicroChip RN52](https://www.microchip.com/en-us/product/RN52) web page.

| Device Name | Parameter | Usage Example |
| --- | --- | --- |
| RN52 | rn52 | RunPairingTests.bat rn52 |

:::image type="content" source="images/RN52.png" alt-text="Close-up photo of the RN52 Bluetooth audio device.":::

## Supported tests

- [Pairing tests](testing-BTP-tests-pairing.md)
- [Audio tests](testing-BTP-tests-audio.md)
- [Audio & HID tests](testing-BTP-tests-audio-hid.md) (as an audio device)
- [Wi-Fi coexistence tests](testing-BTP-tests-wifi.md) (as an audio device)

## Hardware

The peripheral module (PMOD) interface and audio header RN52 device can be purchased via [MCCI](https://store.mcci.com/collections/frontpage/products/rn52-sled)

### RN52 Device on BTP-compatible sled

:::image type="content" source="images/Traduci_and_RN52.jpg" alt-text="RN52 device mounted on a BTP-compatible sled.":::

> [!NOTE]
> The RN52 device can **only** be plugged into the Traduci board 12-pin port labeled 'JA'.

## Features

- UART data connection with AT commands to configure software
- SPP, A2DP, HFP, and AVRCP profiles
- Audio module version 3.0
- Fully certified Class 2 BR Bluetooth 2.1+EDR
- Small form factor, low power, surface mount module
