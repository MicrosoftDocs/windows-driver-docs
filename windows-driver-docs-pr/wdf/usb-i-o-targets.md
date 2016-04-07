---
title: USB I/O Targets
description: This section describes how Kernel-Mode Driver Framework (KMDF) and User-Mode Driver Framework (UMDF) drivers starting in version 2 interact with universal serial bus (USB) devices.
ms.assetid: 195c0f4b-7f33-428a-8de7-32643ad854c6
keywords: ["I/O targets WDK KMDF , USB", "USB I/O targets WDK KMDF", "USB request blocks WDK KMDF", "URBs WDK KMDF", "USB I/O targets WDK KMDF , about USB I/O targets"]
---

# USB I/O Targets


This section describes how Kernel-Mode Driver Framework (KMDF) and User-Mode Driver Framework (UMDF) drivers starting in version 2 interact with universal serial bus (USB) devices.

## <a href="" id="ddk-using-usb-i-o-targets-df"></a>


Each USB device, and each pipe that a USB device interface supports, has a separate I/O target. Control transfers that the USB device handles are sent to the device's I/O target. I/O transfers that a specific pipe handles are sent to that pipe's I/O target.

The framework communicates with a USB device's I/O target by sending USB request blocks ([**URBs**](https://msdn.microsoft.com/library/windows/hardware/ff538923)). The framework provides object methods that hide the URBs from your driver so that the driver does not have to build and send them itself. If you would prefer that your driver build URBs, a KMDF driver can use an additional set of object methods that build and send URBs.

For information about how to determine what type of driver you need for your USB device, see [Choosing a driver model for developing a USB client driver](https://msdn.microsoft.com/library/windows/hardware/ff540215).

This section includes:

-   [Working with USB Devices](working-with-usb-devices.md)

-   [Working with USB Interfaces](working-with-usb-interfaces.md)

-   [Working with USB Pipes](working-with-usb-pipes.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20USB%20I/O%20Targets%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




