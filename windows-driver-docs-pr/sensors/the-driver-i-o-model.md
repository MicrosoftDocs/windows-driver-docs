---
title: The driver I/O model
author: windows-driver-content
description: The sample driver and the accelerometer communicate over the simple peripheral bus, the system GPIO pins, and the resource hub.
ms.assetid: 69368837-0599-497F-883C-608DFE014C7E
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# The driver I/O model


The sample driver and the accelerometer communicate over the simple peripheral bus, the system GPIO pins, and the resource hub.

The following illustration depicts the organization of the components running in: user mode, kernel mode, and the actual hardware.

![io diagram](images/io.png)

## Simple peripheral bus (SPB)


Windows 8.1 supports an SPB component in the form of a class extension that simplifies the development and implementation for SPB controller drivers. In general, the component offers the following:

-   Handles all communication with the Resource Hub including registration and setting retrieval.
-   Implements tiered queue structure to manage simultaneous targets and bus-locking requests
-   Translates buffers from user-mode to kernel-mode

## General-purpose input/output (GPIO)


Windows 8.1 supports a GPIO class extension that resides at the same level as the kernel-mode SPB component. The GPIO class extension allows for flexibility in the underlying hardware connections and GPIO locations while offering a standard interface for client drivers.

On SoC platforms GPIO pins are spread across the chip as well as exposed on other components like a SPI-connected modem.

## Resource hub


Windows 8.1 supports a resource hub which manages the connections among all devices and bus controllers. The hub guarantees that the necessary start and stop ordering is maintained.

The hub is a component specifically aimed at SoC platforms and their flat device tree. Buses on these systems differ from PCs in the following ways:

-   Connections are typically non-discoverable; they are statically defined in ACPI
-   Hardware components often have multiple dependencies spanning multiple buses, rather than strict parent-child relationships

## Related topics
[SpbAccelerometer driver sample](spbaccelerometer-driver-sample.md)  
[Using the sensor class extension](using-the-sensor-class-extension.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20The%20driver%20I/O%20model%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


