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

Component Firmware Update (CFU) provides Original Equipment Manufacturers (OEMs) and Independent Hardware Vendors (IHVs) a reliable, robust against power interruption, and authenticated method for updating firmware on devices that have shipped to customers. This release contains a reference device driver for delivering the firmware payload to a target device and reference firmware for receiving the firmware payload.

See the [Introducing Component Firmware Update](https://blogs.windows.com/buildingapps/?p=54456) blog post and [WinHEC 2018 - Component Firmware Update](https://developer.microsoft.com/windows/hardware/events) video for an introduction to CFU concepts.

## In this section

[CFU engineering guide](cfu-engineering-guide.md)

[CFU host driver sample](cfu-host-driver.md)

[Customize the CFU driver](customize-the-cfu-driver.md)

[CFU standalone tool sample](cfu-standalone-tool-sample.md)

[CFU protocol specification](cfu-specification.md)

## CFU repository on GitHub

- [Firmware](https://github.com/Microsoft/CFU/tree/master/Firmware) - sample firmware source code for implementing the CFU protocol

- [Host](https://github.com/Microsoft/CFU/tree/master/Host) - sample CFU driver source code

  - [Component Firmware Update Driver](https://github.com/microsoft/CFU/tree/master/Host/ComponentFirmwareUpdateDriver)
  
  - [Componentized Package Example](https://github.com/microsoft/CFU/tree/master/Host/ComponentizedPackageExample)
  
  - [Monolithic Package Example](https://github.com/microsoft/CFU/tree/master/Host/MonolithicPackageExample)

  - [CFU Firmware Simulation](https://github.com/microsoft/CFU/tree/master/Host/CFUFirmwareSimulation)

- [Tools](https://github.com/Microsoft/CFU/tree/master/Tools) - sample CFU standalone tool
