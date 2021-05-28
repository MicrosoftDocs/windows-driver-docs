---
title: Microsoft Bluetooth Test Platform - RN42
description: Bluetooth Test Platform (BTP) supported hardware (RN42).
ms.date: 5/24/2021
ms.localizationpriority: medium

---

# RN42 (PMOD BT2)

## Overview

The RN42 is a Basic Rate (BR) radio from Roving Networks capable of behaving as a HID peripheral such as a keyboard or mouse. More info can be found at [Digilent](https://store.digilentinc.com/pmod-bt2-bluetooth-interface/) and through the [**MicroChip**](https://www.microchip.com/wwwproducts/en/RN42) RN42 reference.

| Device | Capabilities | Parameter |
| --- | --- | --- |
| RN42 | Basic Rate (BR) radio | rn42 (ex. RunPairingTests.bat rn42) |

![Photo of the RN42 Device](images/RN42.png)

## Suported Tests
- [Pairing tests](testing-BTP-tests-pairing.md)
- [Human Interface Device (HID) tests](testing-BTP-tests-hid.md)
- [Audio & HID tests](testing-BTP-tests-audio-hid.md)

## Hardware 

The Pmod BT2 device can be purchased via [Digilent](https://store.digilentinc.com/pmod-bt2-bluetooth-interface/)

### Bluetooth Test Platform Traduci Board and Diligent sled

![Photo of the RN42 Device on a Digilent sled](images/Traduci_and_DigilentRN42.jpg)

> [!NOTE]
> The RN42 device can **only** be plugged into Bluetooth Test Platform Traduci board port labeled 'JB'.

## Features

- UART data connection
- Supports HID profile and Bluetooth data links
- Fully certified Class 2 BR Bluetooth 2.1+
- Small form factor, low power, surface mount module
