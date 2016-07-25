---
title: Operating a Parallel Port
author: windows-driver-content
description: Operating a Parallel Port
MS-HAID:
- 'vspd\_73157715-9621-45f3-a7fd-c935f74ec012.xml'
- 'parports.operating\_a\_parallel\_port'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c9015a01-a7cb-41f4-9710-a868ef19f6d7
keywords: ["vendor-supplied parallel drivers WDK , parallel port operation", "system-supplied function drivers WDK parallel ports", "function drivers WDK parallel ports"]
---

# Operating a Parallel Port


## <a href="" id="ddk-operating-a-parallel-port-kg"></a>


This section describes how a client, in particular, a vendor-supplied function driver for a parallel device, operates a parallel port.

The system-supplied function driver for parallel ports creates a functional device object (FDO) for each parallel port enumerated in the system. The following topics describe how a client operates a parallel port by using the interface provided by the port's FDO:

[Creating and Starting a Parallel Port](creating-and-starting-a-parallel-port.md)

[Opening and Closing a Parallel Port](opening-and-closing-a-parallel-port.md)

[Obtaining Information About a Parallel Port](obtaining-information-about-a-parallel-port.md)

[Synchronizing the Use of a Parallel Port](synchronizing-the-use-of-a-parallel-port.md)

[Selecting and Deselecting an IEEE 1284 Device Attached to a Parallel Port](selecting-and-deselecting-an-ieee-1284-device-attached-to-a-parallel-p.md)

[Setting and Clearing the Communication Mode on a Parallel Port](setting-and-clearing-the-communication-mode-on-a-parallel-port.md)

[Connecting to an IEEE 1284.3 Data Link Device](connecting-to-an-ieee-1284-3-data-link-device.md)

[Connecting an Interrupt Service Routine to a Parallel Port](connecting-an-interrupt-service-routine-to-a-parallel-port.md)

For more information about system support for parallel ports, see:

[Introduction to ParallelPorts and Devices](introduction-to-parallel-ports-and-devices.md)

[System-Supplied Parallel Drivers](system-supplied-parallel-drivers.md)

[Client Interfaces to System-Supplied Parallel Drivers](https://msdn.microsoft.com/library/windows/hardware/ff543926)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bparports\parports%5D:%20Operating%20a%20Parallel%20Port%20%20RELEASE:%20%287/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


