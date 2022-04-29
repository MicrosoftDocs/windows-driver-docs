---
title: Microsoft Bluetooth Test Platform - BM-62-EVB board
description: Bluetooth Test Platform (BTP) supported hardware (BM62).
ms.date: 06/09/2021
---

# BM62

## Overview

The BM62 is a dual-mode Bluetooth v5.0 radio designed for use in headsets, speakers, or multi-speaker peripherals. More information can be found on the BM62 page from [**Microchip Technology Incorporated**](https://www.microchip.com/wwwproducts/en/BM62). This sled breaks out the audio out/in data from the radio and routes it to an audio codec and audio processing FPGA on the Traduci in order to aid with validation.

| Device Name | Parameter | Usage Example |
| --- | --- | --- |
| BM62 | bm62 | RunPairingTests.bat bm62 |

:::image type="content" source="images/BM62.png" alt-text="Photo of the BM62 device.":::

## Supported tests

- [Pairing tests](testing-BTP-tests-pairing.md)
- [Audio tests](testing-BTP-tests-audio.md)
- [Audio & HID tests](testing-BTP-tests-audio-hid.md) (as an audio device)
- [Wi-Fi coexistence tests](testing-BTP-tests-wifi.md) (as an audio device)
> This radio supports audio streaming but has many known audio quality problems. Do not use it for audio quality validation.

## Required Hardware

The PMOD + Audio header BM62 device can be purchased via [MCCI](https://store.mcci.com/collections/frontpage/products/model-2435-bm62-audio-capable-radio-sled).

> The BM62 device can <b>only</b> be plugged into the Traduci board 12-pin port labeled 'JA'.
:::image type="content" source="images/BM62_Traduci.png" alt-text="Photo of the BM62 attached to the Traduci.":::

## Features

- UART data connection with custom packet structure
- Supports SPP, A2DP, HFP, and AVRCP profiles
- Bluetooth v5.0
- Supports Bluetooth dual-mode (BDR/EDR/BLE)
- Supports AAC and SBC codecs
- Heavily featured, surface mount module

## Known test failures

 With version 1.7.2 both standalone audio tests will fail as will some audio-HID tests due to backend architecture changes. If this breaks you, please file a bug or email btpsupport@microsoft.com
