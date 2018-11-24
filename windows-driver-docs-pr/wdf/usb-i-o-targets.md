---
title: USB I/O Targets
description: This section describes how KMDF and UMDF 2 drivers interact with universal serial bus (USB) devices.
ms.assetid: 195c0f4b-7f33-428a-8de7-32643ad854c6
keywords:
- I/O targets WDK KMDF , USB
- USB I/O targets WDK KMDF
- USB request blocks WDK KMDF
- URBs WDK KMDF
- USB I/O targets WDK KMDF , about USB I/O targets
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# USB I/O Targets


This section describes how Kernel-Mode Driver Framework (KMDF) and User-Mode Driver Framework (UMDF) drivers starting in version 2 interact with universal serial bus (USB) devices.




Each USB device, and each pipe that a USB device interface supports, has a separate I/O target. Control transfers that the USB device handles are sent to the device's I/O target. I/O transfers that a specific pipe handles are sent to that pipe's I/O target.

The framework communicates with a USB device's I/O target by sending USB request blocks ([**URBs**](https://msdn.microsoft.com/library/windows/hardware/ff538923)). The framework provides object methods that hide the URBs from your driver so that the driver does not have to build and send them itself. If you would prefer that your driver build URBs, a KMDF driver can use an additional set of object methods that build and send URBs.

For information about how to determine what type of driver you need for your USB device, see [Choosing a driver model for developing a USB client driver](https://msdn.microsoft.com/library/windows/hardware/ff540215).

This section includes:

-   [Working with USB Devices](working-with-usb-devices.md)

-   [Working with USB Interfaces](working-with-usb-interfaces.md)

-   [Working with USB Pipes](working-with-usb-pipes.md)

 

 





