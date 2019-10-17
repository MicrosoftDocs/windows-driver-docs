---
title: Component Firmware Update (CPU) 
description: Provides information about Component Firmware Update (CPU)
ms.date: 09/10/2019
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Component Firmware Update (CPU)

Component Firmware Update (CFU) is a mechanism developed by the Microsoft Devices team which allows Original Equipment Manufacturers (OEMs) and Independent Hardware Vendors (IHVs) a reliable, robust against power interruptions and authenticated mechanism for updating firmware for devices that have shipped to customers. This release contains a reference device driver for delivering the firmware payload to a target device, and reference firmware for receiving the firmware payload and associated documentation.

For an overview, read this post: [Introducing Component Firmware Update](https://blogs.windows.com/buildingapps/?p=54456) and watch the [WinHEC 2018 video on Component Firmware Update](https://developer.microsoft.com/en-us/windows/hardware/events).

## Contents

The [Documentation](https://github.com/Microsoft/CFU/tree/master/Documentation) folder contains the CFU protocol specification and the CFU driver design documentation.

The [Host](https://github.com/Microsoft/CFU/tree/master/Host) folder contains a link to the sample CFU protocol driver source code on GitHub.

The [Firmware](https://github.com/Microsoft/CFU/tree/master/Firmware) folder contains sample firmware source code for implementing the CFU protocol.

The [Tools](https://github.com/Microsoft/CFU/tree/master/Tools) folder contains tools used with CFU.

## See also

[Storage Firmware Update (SFU)](storage-firmware-update-driver.md)
