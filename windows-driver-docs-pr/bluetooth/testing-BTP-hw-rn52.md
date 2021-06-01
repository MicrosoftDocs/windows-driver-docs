---
title: Microsoft Bluetooth Test Platform - RN52 - Audio-capable peripheral radios
description: Bluetooth Test Platform (BTP) supported hardware (RN52).
ms.date: 5/27/2021
ms.localizationpriority: medium

---

# RN52 device

## Overview

The RN52 is a Basic Rate (BR) radio from Roving Networks capable of behaving as an Audio peripheral such as a speaker or headset). More information can be found via the RN52 page from [**MicroChip**](https://www.microchip.com/wwwproducts/en/RN52). This sled breaks out the audio out data from the radio and routes it to an audio codec and audio processing FPGA on the Traduci in order to aid with validation.

| Device Name | Parameter | Usage Example |
| --- | --- | --- |
| RN52 | rn52 | RunPairingTests.bat rn52 |

![Photo of the RN52 Device](images/RN52.png)

## Suported Tests
- [Pairing tests](testing-BTP-tests-pairing.md)
- [Audio tests](testing-BTP-tests-audio.md)
- [Audio & HID tests](testing-BTP-tests-audio-hid.md) (as an audio device)
- [Wi-Fi coexistence tests](testing-BTP-tests-wifi.md) (as an audio device)

## Hardware 

The PMOD + Audio header RN52 device can be purchased via [MCCI](https://store.mcci.com/collections/frontpage/products/rn52-sled)

### RN52 Device on BTP-compatible sled

![Photo of the RN52 Device on a sled](images/Traduci_and_RN52.jpg)

> [!NOTE]
> The RN52 device can **only** be plugged into the Traduci board 12-pin port labeled 'JA'.

## Features

- UART data connection with AT commands to configure software
- Supports SPP, A2DP, HFP, and AVRCP profiles
- Version 3.0 audio module
- Fully certified Class 2 BR Bluetooth 2.1+EDR
- Small form factor, low power, surface mount module
