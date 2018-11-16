---
title: USB I/O Targets in UMDF
description: USB I/O Targets in UMDF
ms.assetid: e08ca910-1b28-4809-9a5b-db3730cda31a
keywords:
- user-mode drivers WDK UMDF , USB I/O targets
- UMDF WDK , USB I/O targets
- User-Mode Driver Framework WDK , USB I/O targets
- framework-based drivers WDK UMDF , USB I/O targets
- USB I/O targets WDK UMDF
- I/O targets WDK UMDF , USB
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# USB I/O Targets in UMDF

[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

Each universal serial bus (USB) device, and each pipe that a USB device interface supports, has a separate I/O target. I/O that the USB device processes is sent to the device's I/O target. I/O that a specific pipe processes is sent to that pipe's I/O target.

## In this section


-   [Choosing a Driver Model for a USB Device](choosing-a-driver-model-for-a-usb-device.md)
-   [USB-Specific UMDF 1.x Interfaces](usb-specific-umdf-1-x-interfaces.md)
-   [Working with USB Devices in UMDF 1.x Drivers](working-with-usb-devices-in-umdf-1-x-drivers.md)
-   [Working with USB Interfaces in UMDF 1.x Drivers](working-with-usb-interfaces-in-umdf-1-x-drivers.md)
-   [Working with USB Pipes in UMDF 1.x Drivers](working-with-usb-pipes-in-umdf-1-x-drivers.md)
-   [File Creation by a USB I/O Target](file-creation-by-a-usb-i-o-target.md)
-   [Calling WinUSB from UMDF](escaping-to-winusb.md)

 

 





