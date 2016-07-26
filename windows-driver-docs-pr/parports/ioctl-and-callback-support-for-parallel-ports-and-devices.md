---
title: IOCTL and Callback Support for Parallel Ports and Devices
author: windows-driver-content
description: IOCTL and Callback Support for Parallel Ports and Devices
MS-HAID:
- 'sspd\_cafc81fd-1ccb-4f62-bae4-acc7763cb06e.xml'
- 'parports.ioctl\_and\_callback\_support\_for\_parallel\_ports\_and\_devices'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 72a31f50-2f59-4a4d-aac7-571f83a94259
keywords: ["system-supplied parallel drivers WDK , IOCTLs", "IOCTLs WDK parallel drivers", "callbacks WDK parallel drivers", "system-supplied parallel drivers WDK , callbacks", "parallel devices WDK , callbacks", "parallel devices WDK , IOCTLs"]
---

# IOCTL and Callback Support for Parallel Ports and Devices


## <a href="" id="ddk-ioctl-and-callback-support-for-parallel-ports-and-devices-kg"></a>


This section provides links to topics that describe how the system-supplied parallel drivers support operating parallel ports and devices attached to parallel ports.

Vendor function drivers for parallel devices that are attached to parallel ports are optional. The system-supplied parallel drivers provide extensive support for directly controlling a parallel device as a raw device, and for operating a device's parent parallel port.

For information about the IOCTLs and callbacks that the system-supplied function driver provides to operate a parallel port, see the following topics:

[Obtaining Information About a Parallel Port](obtaining-information-about-a-parallel-port.md)

[Synchronizing the Use of a Parallel Port](synchronizing-the-use-of-a-parallel-port.md)

[Selecting and Deselecting an IEEE 1284 Device Attached to a Parallel Port](selecting-and-deselecting-an-ieee-1284-device-attached-to-a-parallel-p.md)

[Setting and Clearing the Communication Mode on a Parallel Port](setting-and-clearing-the-communication-mode-on-a-parallel-port.md)

[Connecting to an IEEE 1284.3 Data Link Device](connecting-to-an-ieee-1284-3-data-link-device.md)

For information about the IOCTLs and callbacks that the system-supplied bus driver provides to operate a parallel device that is attached to a parallel port, see the following:

[Opening and Using a Parallel Device](opening-and-using-a-parallel-device.md)

[Connecting to a Parallel Device](connecting-to-a-parallel-device.md)

[Obtaining Information about a Parallel Device](obtaining-information-about-a-parallel-device.md)

[Locking and Unlocking a Parallel Port for Use by a Parallel Device](locking-and-unlocking-a-parallel-port-for-use-by-a-parallel-device.md)

[Setting and Clearing a Communication Mode for a Parallel Device](setting-and-clearing-a-communication-mode-for-a-parallel-device.md)

[Setting Attributes on a Parallel Device](setting-attributes-on-a-parallel-device.md)

[Reading and Writing a Parallel Device](reading-and-writing-a-parallel-device.md)

For more information about how to operate parallel ports and devices attached to parallel ports, see:

[Operating a Parallel Port](operating-a-parallel-port.md)

[Operating a Parallel Device Attached to a Parallel Port](operating-a-parallel-device-attached-to-a-parallel-port.md)

[Client Interfaces to System-Supplied Parallel Drivers](https://msdn.microsoft.com/library/windows/hardware/ff543926)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bparports\parports%5D:%20IOCTL%20and%20Callback%20Support%20for%20Parallel%20Ports%20and%20Devices%20%20RELEASE:%20%287/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


