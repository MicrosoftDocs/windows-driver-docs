---
title: Component Firmware Update (CPU) 
description: Provides information about Component Firmware Update (CPU)
ms.date: 07/17/2020
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Component Firmware Update (CPU)

Component Firmware Update (CFU) is a mechanism developed by the Microsoft Devices team which provides Original Equipment Manufacturers (OEMs) and Independent Hardware Vendors (IHVs) a reliable robust (against power interruptions), and authenticated method for updating firmware on devices that have shipped to customers. This release contains a reference device driver for delivering the firmware payload to a target device and reference firmware for receiving the firmware payload.

For additional information, see [**Introducing Component Firmware Update**](https://blogs.windows.com/buildingapps/?p=54456) and [**WinHEC 2018 video on Component Firmware Update**](https://developer.microsoft.com/windows/hardware/events).

## Component Firmware Update (CFU) documentation

[CFU driver](cfu-driver.md)

[CFU engineering guide](cfu-engineering-guide.md)

[CFU host](cfu-host.md)

[CFU host driver](cfu-host-driver.md)

[CFU tools](cfu-tools.md)

[CFU standalone tool sample](cfu-standalone-tool-sample.md)

[CFU specification](cfu-specification.md)

## Component Firmware Update (CFU) repository on GitHub

The [Host](https://github.com/Microsoft/CFU/tree/master/Host) folder contains a link to the sample CFU protocol driver source code on GitHub.

- [CFU host](cfu-host.md)

- [CFU host driver](cfu-host-driver.md)

The [Firmware](https://github.com/Microsoft/CFU/tree/master/Firmware) folder contains sample firmware source code for implementing the CFU protocol.

The [Tools](https://github.com/Microsoft/CFU/tree/master/Tools) folder contains tools used with CFU.

- [CFU tools](cfu-tools.md)

- [CFU standalone tool sample](cfu-standalone-tool-sample.md)
