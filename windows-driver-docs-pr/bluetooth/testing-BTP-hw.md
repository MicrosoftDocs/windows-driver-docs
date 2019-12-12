---
title: Microsoft Bluetooth Test Platform
description: Bluetooth Test Platform (BTP) supported hardware.
ms.assetid: a6beeecb-5967-4e08-bfe2-b8aae26861ad
ms.date: 4/17/2019
ms.localizationpriority: medium

---

# BTP Suported Hardware

The Bluetooth Test Platform (BTP) requires external Bluetooth radios to simulate peripheral is the software component of Microsoft's latest automated Bluetooth testing. The Traduci is the hardware platform that the BTP runs on and supports peripheral radios to be plugged into it. The package consists of software tests, a firmware package, a provisioning tool  the Traduci board and a set of peripheral radios used for testing basic functionality.

At this time the only supported radio is the RN42. Purchasing information for the Traduci, RN42 and future radios can be found below.


# Devices #

## Traduci board ##
[**MCCI**](https://mcci.com/usb/dev-tools/model-2411/)

<img src="images/Traduci_Overhead.jpg" alt="Photo of the Traduci board" width="400"/>

- 4 12-pin ports to support 4 radios simultaneously
- 3 FPGAs connected to ports 1, 2, and 3 respectively
- Supports audio testing via the integrated audio codec
- Supports HID and pairing tests

### PMOD Layout ###

<img src="images/Traduci_Overhead.jpg" alt="Photo of the Traduci board" width="400"/>

- Unlabled pins can easily be statically assigned to HIGH or LOW depending on the needs of the radio plugged into the port
- The Traduci does not currently support hardware handshaking using CTS and RTS

