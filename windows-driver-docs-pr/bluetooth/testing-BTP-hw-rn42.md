---
title: Microsoft Bluetooth Test Platform - RN42
description: Bluetooth Test Platform (BTP) supported hardware (RN42).
ms.date: 06/09/2021
ms.localizationpriority: medium
---

# RN42 (PMOD BT2)

## Overview

The RN42 is a Basic Rate (BR) radio from Roving Networks capable of behaving as a HID peripheral such as a keyboard or mouse. More info can be found at [Digilent](https://store.digilentinc.com/pmod-bt2-bluetooth-interface/) and through the [Microchip](https://www.microchip.com/wwwproducts/en/RN42) RN42 reference.

| Device Name | Parameter | Usage Example |
| --- | --- | --- |
| RN42 | rn42 | RunPairingTests.bat rn42 |

:::image type="content" source="images/RN42.png" alt-text="Photo of the RN42 device.":::

## Supported tests

- [Pairing tests](testing-BTP-tests-pairing.md)
- [Human Interface Device (HID) tests](testing-BTP-tests-hid.md)
- [Audio & HID tests](testing-BTP-tests-audio-hid.md) (as a HID device)

## Hardware

The Model 2431 RN42 Radio Sled for BTP can be purchased via [MCCI](https://store.mcci.com/collections/frontpage/products/rn42-sled). The Pmod BT2 device can be purchased via [Digilent](https://store.digilentinc.com/pmod-bt2-bluetooth-interface/)

### Bluetooth Test Platform Traduci Board and Diligent sled

:::image type="content" source="images/Traduci_and_DigilentRN42.jpg" alt-text="Photo of the RN42 device on a Digilent sled.":::

> [!NOTE]
> The RN42 device can **only** be plugged into a Bluetooth Test Platform Traduci board port labeled 'JB'.

## Features

- UART data connection
- Supports HID profile and Bluetooth data links
- Fully certified Class 2 BR Bluetooth 2.1+
- Small form factor, low power, surface mount module
