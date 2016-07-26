---
title: Operating a Parallel Device Attached to a Parallel Port
author: windows-driver-content
description: Operating a Parallel Device Attached to a Parallel Port
MS-HAID:
- 'vspd\_af50eebe-27e3-4206-b852-c0dac3ab6368.xml'
- 'parports.operating\_a\_parallel\_device\_attached\_to\_a\_parallel\_port'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5ad36162-efbe-4be8-954c-964ef12c539a
keywords: ["parallel ports WDK , parallel device operation", "parallel devices WDK", "vendor-supplied parallel drivers WDK , parallel device operation", "parallel devices WDK , client operation"]
---

# Operating a Parallel Device Attached to a Parallel Port


## <a href="" id="ddk-operating-a-parallel-device-attached-to-a-parallel-port-kg"></a>


This section describes how a client, in particular, a vendor-supplied function driver for a parallel device, operates a parallel device attached to a parallel port.

The system-supplied bus driver for parallel ports creates a physical device object (PDO) for each parallel device enumerated on a parallel port. The following topics describe how a client operates a parallel device by using the interface provided by the device's PDO:

[Opening and Using a Parallel Device](opening-and-using-a-parallel-device.md)

[Connecting to a Parallel Device](connecting-to-a-parallel-device.md)

[Obtaining Information about a Parallel Device](obtaining-information-about-a-parallel-device.md)

[Locking and Unlocking a Parallel Port for Use by a Parallel Device](locking-and-unlocking-a-parallel-port-for-use-by-a-parallel-device.md)

[Setting and Clearing a Communication Mode for a Parallel Device](setting-and-clearing-a-communication-mode-for-a-parallel-device.md)

[Setting Attributes on a Parallel Device](setting-attributes-on-a-parallel-device.md)

[Reading and Writing a Parallel Device](reading-and-writing-a-parallel-device.md)

For more information about support for parallel devices attached to a parallel port, see:

[Introduction to ParallelPorts and Devices](introduction-to-parallel-ports-and-devices.md)

[System-Supplied Parallel Drivers](system-supplied-parallel-drivers.md)

[Client Interfaces to System-Supplied Parallel Drivers](https://msdn.microsoft.com/library/windows/hardware/ff543926)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bparports\parports%5D:%20Operating%20a%20Parallel%20Device%20Attached%20to%20a%20Parallel%20Port%20%20RELEASE:%20%287/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


