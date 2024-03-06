---
title: Overview of Developing Windows Drivers for Emulated USB Devices (UDE)
description: Overview of developing Windows drivers for emulated USB devices (UDE)
ms.date: 01/12/2024
---

# Overview of developing Windows drivers for emulated USB devices (UDE)

This article describes USB emulated device (UDE) support in the Windows operating system, for developing an emulated Universal Serial Bus (USB) host controller driver and a connected virtual USB device. Both components are combined into a single KMDF driver that communicates with the Microsoft-provided USB device emulation class extension (UdeCx).

## Development tools and Microsoft-provided binaries

The Windows Driver Kit (WDK) contains resources that are required for driver development, such as headers, libraries, tools, and samples.

[Download kits and tools for Windows](https://developer.microsoft.com/windows/hardware/)

To write a function controller driver, you need:

- UdeCx: (udecx.sys) a WDF extension used by the function driver. This extension is included in Windows.
- Link to the stub library (Udecxstub.lib). The stub library is in the WDK.
- Include Udecx.h provided in the WDK.

## Architecture of UDE

[Architecture: USB Device Emulation (UDE)](usb-emulated-device--ude--architecture.md)

[USB host-side drivers](usb-3-0-driver-stack-architecture.md) in Windows

## Writing drivers for emulated host controller and devices

Familiarize yourself with UDE objects and handles. For details on WDF objects, see [Introduction to Framework Objects](../wdf/introduction-to-framework-objects.md).

Understand the behavior of UDE, how it interacts with the client driver, and the features that the client driver is expected to implement.

[Write a UDE client driver](writing-a-ude-client-driver.md)

## Programming reference sections

[Emulated USB host controller driver programming reference](/windows-hardware/drivers/ddi/_usbref/#emulated-host-controller-driver-reference)

[WDF Reference](/windows-hardware/drivers/ddi/_wdf/)

## Related topics

- [Universal Serial Bus (USB)](./index.md)
