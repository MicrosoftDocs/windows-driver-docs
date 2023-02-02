---
title: Overview of developing Windows drivers for USB function controllers
description: Overview of developing Windows drivers for USB function controllers
ms.date: 01/19/2023
---

# Overview of developing Windows drivers for USB function controllers

This article describes support in the Windows operating system, for developing a Universal Serial Bus (USB) function controller driver that communicates with the Microsoft-provided USB function controller extension (UFX).

## Development tools and Microsoft-provided binaries

The Windows Driver Kit (WDK) contains resources that are required for driver development, such as headers, libraries, tools, and samples.

[Download kits and tools for Windows](https://go.microsoft.com/fwlink/p/?linkid=617155)

Windows provides inbox USB function controller drivers such as UfxSynopsys.sys for the controller hardware of Synopsys IP. They generally require platform level changes and validation that are typically performed by hardware partners or OEMs when bringing up a platform. This bring-up process may include integration with ACPI to notify system drivers of USB attach/detach events, and performing additional validation using Microsoft-provided HLK tests. To write your own controller driver, you need:

- UFX (Ufx01000.sys) loaded as the FDO. This driver is included in Windows.
- Link to the stub library (Ufx01000.lib). The stub library is in the WDK. The library translates calls made by the function controller driver and pass them up to UFX.
- Include Ufxclient.h provided in the WDK.

To send requests from user mode, you need:

- GenericUSBFn.sys loaded as the USB function class driver. This driver is included in Windows.
- Include Genericusbfnioctl.h provided in the WDK.

To send requests from your USB class driver, you need:

- UFX (Ufx01000.sys) loaded as the FDO. This driver is included in Windows.
- Include Usbfnioctl.h provided in the WDK.

To write a filter driver that handles charging through proprietary chargers, you need:

- Either UfxChipidea.sys or Ufxsynopsys.sys loaded as the client driver to UFX.
- Include Ufxproprietarycharger.h provided in the WDK.

## Architecture of UFX

Familiarize yourself with the Microsoft-provided USB driver stack:

[USB device-side drivers in Windows](usb-device-side-drivers-in-windows.md)

## Familiarize yourself with UFX objects and handles

UFX extends the WDF object functionality to define its own USB-specific UCX objects. For more details on WDF objects, see [Introduction to Framework Objects](../wdf/introduction-to-framework-objects.md).

For queuing requests, UFX uses USB-specific objects. For more information, [UFX objects and handles used by a USB function client driver](ufx-objects-and-handles-used-by-a-usb-function-controller.md).

## Writing a function controller client driver

Understand the behavior of UFX, how it interacts with the client driver, and the features that the client driver is expected to implement.

[Tasks for a function controller client driver](function-client-driver.md)

## Programming reference sections

[USB function class driver to UFX programming reference](/windows-hardware/drivers/ddi/_usbref/#function-class-driver-reference)

[USB function controller client driver programming reference](/windows-hardware/drivers/ddi/_usbref/#usb-function-controller-client-driver-reference)

[USB filter driver for supporting proprietary chargers](/windows-hardware/drivers/ddi/_usbref/#filter-driver-for-supporting-usb-chargers)

## Related topics

- [Universal Serial Bus (USB)](../index.yml)
