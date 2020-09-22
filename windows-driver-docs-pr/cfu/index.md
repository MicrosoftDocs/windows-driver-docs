---
title: Component Firmware Update (CFU) 
description: Provides information about Component Firmware Update (CFU)
ms.date: 09/01/2020
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Component Firmware Update (CFU)

Component Firmware Update (CFU) provides Original Equipment Manufacturers (OEMs) and Independent Hardware Vendors (IHVs) a reliable and authenticated method for updating firmware on devices that have shipped to customers. This release contains reference firmware for receiving the firmware payload.

See the [Introducing Component Firmware Update](https://blogs.windows.com/buildingapps/?p=54456) blog post and [WinHEC 2018 - Component Firmware Update](https://developer.microsoft.com/windows/hardware/events) video for an introduction to CFU concepts.

## In this section

| Topic | Description |
|--|--|
| [CFU engineering guide](cfu-engineering-guide.md) | Provides detailed guidance on implementing the CFU protocol and the process of creating new firmware images to be installed on the target device. |
| [CFU virtual HID device firmware update](cfu-virtual-hid-device-firmware-update.md) | Provides a walkthrough of updating the sample virtual HID device firmware. |
| [CFU inbox HIDSYS driver INF configuration](cfu-inbox-driver-inf-configuration.md) | Provides information on configuring the inbox HIDSYS driver INF file for your firmware update. |
| [CFU standalone tool sample](cfu-standalone-tool-sample.md) | Provides information on the CFU standalone tool sample that sends firmware update image files to a device. |
| [CFU protocol specification](cfu-specification.md) | Provides detailed information on the CFU protocol offer, content, and firmware update command sequence. |

## CFU repository on GitHub

- [Component Firmware Update (CFU) repository](https://github.com/microsoft/CFU)
