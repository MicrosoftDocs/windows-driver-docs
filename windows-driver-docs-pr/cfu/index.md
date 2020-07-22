---
title: Component Firmware Update (CPU) 
description: Provides information about Component Firmware Update (CPU)
ms.date: 07/21/2020
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Component Firmware Update (CPU)

Component Firmware Update (CFU) is a mechanism developed by the Microsoft Devices team which provides Original Equipment Manufacturers (OEMs) and Independent Hardware Vendors (IHVs) a reliable robust (against power interruptions), and authenticated method for updating firmware on devices that have shipped to customers. This release contains a reference device driver for delivering the firmware payload to a target device and reference firmware for receiving the firmware payload.

For additional information, see [Introducing Component Firmware Update](https://blogs.windows.com/buildingapps/?p=54456) and [WinHEC 2018 video on Component Firmware Update](https://developer.microsoft.com/windows/hardware/events).

## Component Firmware Update (CFU) documentation

[Customize the Component Firmware Update (CFU) driver](customize-the-cfu-driver.md)

[Component Firmware Update (CFU) engineering guide](cfu-engineering-guide.md)

[Component Firmware Update (CPU) host](cfu-host.md)

[Component Firmware Update (CPU) host driver](cfu-host-driver.md)

[Component Firmware Update (CPU) standalone tool sample](cfu-standalone-tool-sample.md)

[Component Firmware Update (CPU) protocol specification](cfu-specification.md)

## Component Firmware Update (CFU) repository on GitHub

- The [Firmware](https://github.com/Microsoft/CFU/tree/master/Firmware) folder contains sample firmware source code for implementing the CFU protocol.

- The [Host](https://github.com/Microsoft/CFU/tree/master/Host) folder contains sample CFU protocol driver source code.

  - [Component Firmware Update Driver](https://github.com/microsoft/CFU/tree/master/Host/ComponentFirmwareUpdateDriver)
  
  - [Componentized Package Example](https://github.com/microsoft/CFU/tree/master/Host/ComponentizedPackageExample)
  
  - [Monolithic Package Example](https://github.com/microsoft/CFU/tree/master/Host/MonolithicPackageExample)

  - [CFU Firmware Simulation](https://github.com/microsoft/CFU/tree/master/Host/CFUFirmwareSimulation)

- The [Tools](https://github.com/Microsoft/CFU/tree/master/Tools) folder contains the standalone tool sample used with CFU.

  - [Component Firmware Update StandAlone Tool Sample](https://github.com/microsoft/CFU/tree/master/Tools/ComponentFirmwareUpdateStandAloneToolSample)
