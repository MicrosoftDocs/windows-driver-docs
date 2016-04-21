---
title: USB I/O Targets in UMDF
author: windows-driver-content
description: USB I/O Targets in UMDF
ms.assetid: e08ca910-1b28-4809-9a5b-db3730cda31a
keywords: ["user-mode drivers WDK UMDF , USB I/O targets", "UMDF WDK , USB I/O targets", "User-Mode Driver Framework WDK , USB I/O targets", "framework-based drivers WDK UMDF , USB I/O targets", "USB I/O targets WDK UMDF", "I/O targets WDK UMDF , USB"]
---

# USB I/O Targets in UMDF


Each universal serial bus (USB) device, and each pipe that a USB device interface supports, has a separate I/O target. I/O that the USB device processes is sent to the device's I/O target. I/O that a specific pipe processes is sent to that pipe's I/O target.

## In this section


-   [Choosing a Driver Model for a USB Device](choosing-a-driver-model-for-a-usb-device.md)
-   [USB-Specific UMDF 1.x Interfaces](usb-specific-umdf-1-x-interfaces.md)
-   [Working with USB Devices in UMDF 1.x Drivers](working-with-usb-devices-in-umdf-1-x-drivers.md)
-   [Working with USB Interfaces in UMDF 1.x Drivers](working-with-usb-interfaces-in-umdf-1-x-drivers.md)
-   [Working with USB Pipes in UMDF 1.x Drivers](working-with-usb-pipes-in-umdf-1-x-drivers.md)
-   [File Creation by a USB I/O Target](file-creation-by-a-usb-i-o-target.md)
-   [Calling WinUSB from UMDF](escaping-to-winusb.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20USB%20I/O%20Targets%20in%20UMDF%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




