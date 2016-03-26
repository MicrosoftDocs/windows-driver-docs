---
title: Using I/O Targets in UMDF
description: Using I/O Targets in UMDF
ms.assetid: 5633242c-ffab-4af5-9650-7449395deb6b
keywords: ["user-mode drivers WDK UMDF , I/O targets", "UMDF WDK , I/O targets", "User-Mode Driver Framework WDK , I/O targets", "framework-based drivers WDK UMDF , I/O targets", "I/O targets WDK UMDF", "targets WDK UMDF"]
---

# Using I/O Targets in UMDF


\[This topic applies to UMDF 1.*x*.\]

When a driver receives an I/O request, the driver might be able to process the request by itself, or it might require the assistance of other drivers. If the driver requires assistance, it can forward the request to another driver, or it can create one or more new requests and send them to another driver.

UMDF-based drivers use *I/O targets* to send I/O requests to another driver. Each I/O target is represented by an I/O target object. Each I/O target object is primarily a queue. When a driver sends a request to an I/O target, the framework stores the request in the queue until it can deliver the request to the I/O target.

The framework supports both general I/O targets and specialized I/O targets:

-   [General I/O targets](general-i-o-targets-in-umdf.md) can be used by all UMDF drivers, but they do not support any special, device-specific data formats.

-   Specialized I/O targets enable UMDF drivers to send I/O requests that require special, target-specific data formatting. Currently, the framework provides support for [USB I/O targets](usb-i-o-targets-in-umdf.md).

If the framework provides specialized I/O targets that support your device's data format, your driver should use the specialized I/O targets. Otherwise, the driver should use general I/O targets.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Using%20I/O%20Targets%20in%20UMDF%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




