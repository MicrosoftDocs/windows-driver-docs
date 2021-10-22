---
title: Component Firmware Update (CFU) 
description: Provides information about Component Firmware Update (CFU)
ms.date: 10/01/2020
ms.topic: article
ms.localizationpriority: medium
---

# Component Firmware Update (CFU)

Component Firmware Update (CFU) provides Original Equipment Manufacturers (OEMs) and Independent Hardware Vendors (IHVs) a reliable and authenticated method for updating firmware on devices that have shipped to customers. This release contains reference firmware for receiving the firmware payload.

> [!NOTE]
> CFU is available in Windows 10, version 2004 (Windows 10 May 2020 Update) and later versions.

See the [Introducing Component Firmware Update](https://blogs.windows.com/buildingapps/?p=54456) blog post and [WinHEC 2018 - Component Firmware Update](https://developer.microsoft.com/windows/hardware/events) video for an introduction to CFU concepts.

## In this section

| Topic | Description |
|--|--|
| [CFU firmware implementation guide](cfu-firmware-implementation-guide.md) | Provides detailed guidance on implementing the CFU firmware protocol and creating new firmware images to install on the target device. |
| [CFU INF file configuration](cfu-inf-configuration.md) | Provides information on configuring your custom device INF file for your firmware update. |
| [CFU protocol specification](cfu-specification.md) | Provides detailed information on the CFU protocol offer, content, and firmware update command sequence. |
| [CFU standalone tool](cfu-standalone-tool.md) | Provides information on the CFU standalone tool that sends firmware update image files to a device. It can be used to test your firmware update on your device during development and before uploading it to Windows Update.|
| [CFU virtual HID device firmware update simulation](cfu-firmware-update-simulation.md) | Simulates updating firmware on a virtual HID device. |
