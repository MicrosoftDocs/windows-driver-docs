---
title: Points to Consider About Device Objects
description: Points to Consider About Device Objects
ms.assetid: 4c54340b-3b4c-4c67-b28d-fac769e4feb7
keywords: ["device objects WDK kernel , design considerations"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Points to Consider About Device Objects





Keep the following points in mind when designing a kernel-mode driver:

-   Except for certain file system drivers, all I/O operations are always sent to the top device object of a device stack.

-   Device stacks are identified using the name of the named device object in the stack, or by using an alias for that name, such as a symbolic link or a device interface. For WDM function drivers, the named device object is created by the bus driver for the device. Non-WDM drivers must create their own named device objects.

-   A lowest-level driver, such as a PnP hardware bus driver, creates a physical device object (PDO) for each device it controls. An intermediate driver, such as a PnP function driver, creates a functional device object (FDO).

    A WDM driver creates device objects in its [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine, which is called by the PnP manager after device enumeration.

-   For most lowest-level and intermediate drivers, the device extension of each device object is each driver's primary (and frequently only) global data storage area. Many drivers maintain device state and all other device-specific data and resources a driver requires in the driver-defined device extension of each driver-created device object.

    (Additionally, the driver-specific [I/O stack location](i-o-stack-locations.md) associated with an IRP can be considered an operation-specific local storage area for some kinds of data.)

For more information about the device objects a specific driver must create, see the device-type-specific documentation in the Windows Driver Kit (WDK).

 

 




