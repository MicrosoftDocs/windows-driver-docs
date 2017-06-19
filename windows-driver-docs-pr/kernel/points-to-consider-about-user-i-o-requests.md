---
title: Points to Consider about User I/O Requests
author: windows-driver-content
description: Points to Consider about User I/O Requests
ms.assetid: e8143055-4ad7-4e39-a2f2-64d9e79d33a0
keywords: ["device-specific I/O control codes WDK kernel", "private I/O control codes WDK kernel", "layered driver IRP processing WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Points to Consider about User I/O Requests


## <a href="" id="ddk-points-to-consider-about-user-i-o-requests-kg"></a>


Keep the following points in mind when designing a kernel-mode driver:

-   Drivers can be layered, and more than one driver can process a single I/O request (IRP).

-   A driver cannot make any assumptions about which other drivers will be in the device stack. Therefore, each driver should be prepared to receive requests from any other driver and should handle all potential error cases.

-   Drivers communicate the success or failure of a requested I/O operation in the I/O status block of the IRP. The I/O manager communicates the success or failure of a requested I/O operation to a user-mode requester.

-   Drivers need not and should not be designed to provide application-specific support. A protected subsystem or its subsystem-specific, user-mode drivers supply this kind of support. There is one exception to this rule: an MS-DOS application that relies on an application-dedicated device can require a kernel-mode driver to control the device and a closely coupled Win32 user-mode virtual device driver (VDD). For more information about VDDs, see the Virtual Device Drivers documentation in the Windows Driver Development Kit (DDK). (The DDK preceded the Windows Driver Kit \[WDK\].)

-   A new driver must handle the same set of **IRP\_MJ\_*XXX*** as any system-supplied driver it replaces. The I/O manager returns STATUS\_INVALID\_DEVICE\_REQUEST for a given I/O request to a target device if its driver does not define an entry point for that **IRP\_MJ\_*XXX***. A device driver also must handle the same I/O control codes for [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) requests as any system-supplied driver it replaces. In other words, a new device driver must not "break applications" by implementing less functionality than an existing driver for the same type of device.

-   A new intermediate driver inserted into a chain of existing drivers should recognize the same set of **IRP\_MJ\_*XXX*** as the driver it displaces. The new driver can simply pass on IRPs for those requests that it does not process to the next-lower-level driver. However, a new intermediate driver must not "break the chain" for drivers above and below it by neglecting to define an entry point for an **IRP\_MJ\_*XXX*** request that the newly displaced, next-lower-level driver does handle.

-   A lowest-level driver can access only its own I/O stack location in any IRP that it is sent. A higher-level driver can access only its own and the next-lower-level driver's I/O stack locations in any IRP that it is sent.

-   Every driver communicates information to higher-level drivers (and ultimately, to user-mode applications via the I/O manager) only in the I/O status blocks of IRPs because the I/O manager zeros the corresponding I/O stack location as each driver in a chain completes an IRP. Any new driver that attempts to implement back-door communication with a particular higher (or lower) driver compromises its portability and its interoperability with other drivers from one Windows platform or version to the next.

-   A pair of drivers can define a set of device-specific (also called *private*) I/O control codes for [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766) requests that the higher of the pair can send down to the lower of the pair. However, such a pair of drivers must follow all of the preceding guidelines if they are to remain portable and interoperable with other drivers from one Windows platform or version to another. If you design a pair of drivers with a private interface, consider the set of I/O control codes to be defined carefully. Make them as generally useful as possible and design your paired drivers to follow the preceding guidelines, so that you (or someone else) can reuse, replace, or displace either or both of your new drivers easily as they migrate from one Windows platform or version to another.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Points%20to%20Consider%20about%20User%20I/O%20Requests%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


