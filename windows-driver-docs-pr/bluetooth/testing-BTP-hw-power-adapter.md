---
title: Microsoft Bluetooth Test Platform - Power Adapter
description: Bluetooth Test Platform (BTP) supported hardware (power adapter).
ms.date: 12/14/2021
ms.localizationpriority: medium
---

# Traduci Power Adapter

## Overview

Certain test cases will require more power than the USB VBus can provide to the Traduci and its attached BT devices. In these instances the test will identify in documentation that an external power adapter is required.  

### Tests that require an external power adapater
- [Power State HID tests](testing-BTP-tests-power-state-hid.md)

### Tests that an external power adapter is recommended for
- [Audio and HID Scenario Tests](testing-BTP-tests-audio-hid.md)
- [Wi-Fi and Bluetooth Audio Coexistence Tests](testing-BTP-tests-wifi.md)

## Requirements

The power adapter chosen must meet the following specification:

- 9V DC
- 1A (minimum)
- Positive Center
- 2.1mm id barrel
- 5.5mm od barrel

## Availability

The 9V DC 1000mA power adapter from Adafruit meets these requirements and can be purchased via [Adafruit](https://www.adafruit.com/product/63).

Any other power adapters that meet the above specification can be used as well.




