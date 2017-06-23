---
title: Points to Consider About Device Objects
author: windows-driver-content
description: Points to Consider About Device Objects
ms.assetid: 4c54340b-3b4c-4c67-b28d-fac769e4feb7
keywords: ["device objects WDK kernel , design considerations"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Points to Consider About Device Objects


## <a href="" id="ddk-points-to-consider-about-device-objects-kg"></a>


Keep the following points in mind when designing a kernel-mode driver:

-   Except for certain file system drivers, all I/O operations are always sent to the top device object of a device stack.

-   Device stacks are identified using the name of the named device object in the stack, or by using an alias for that name, such as a symbolic link or a device interface. For WDM function drivers, the named device object is created by the bus driver for the device. Non-WDM drivers must create their own named device objects.

-   A lowest-level driver, such as a PnP hardware bus driver, creates a physical device object (PDO) for each device it controls. An intermediate driver, such as a PnP function driver, creates a functional device object (FDO).

    A WDM driver creates device objects in its [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine, which is called by the PnP manager after device enumeration.

-   For most lowest-level and intermediate drivers, the device extension of each device object is each driver's primary (and frequently only) global data storage area. Many drivers maintain device state and all other device-specific data and resources a driver requires in the driver-defined device extension of each driver-created device object.

    (Additionally, the driver-specific [I/O stack location](i-o-stack-locations.md) associated with an IRP can be considered an operation-specific local storage area for some kinds of data.)

For more information about the device objects a specific driver must create, see the device-type-specific documentation in the Windows Driver Kit (WDK).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Points%20to%20Consider%20About%20Device%20Objects%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


