---
title: Writing an AddDevice Routine
author: windows-driver-content
description: Writing an AddDevice Routine
MS-HAID:
- 'DrvComps\_40f27e9d-2a0a-4de0-b7a4-cdd9679815e6.xml'
- 'kernel.writing\_an\_adddevice\_routine'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 93a272f4-888c-4cc8-b013-c6313c10a8d8
keywords: ["standard driver routines WDK kernel , AddDevice routines", "driver routines WDK kernel , AddDevice routines", "routines WDK kernel , AddDevice routines", "AddDevice routines WDK kernel", "system-space memory allocations WDK kernel", "system resource storage WDK kernel", "storing system resources", "device objects WDK kernel , creating", "device initialization WDK kernel", "initializing devices", "AddDevice routines WDK kernel , about AddDevice routines"]
---

# Writing an AddDevice Routine


## <a href="" id="ddk-writing-an-adddevice-routine-kg"></a>


Any driver that supports PnP must have an [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine. The *AddDevice* routine creates one or more device objects representing the physical, logical, or virtual devices for which the driver carries out I/O requests. It also attaches the device object to the device stack, so the device stack will contain a device object for each driver associated with the device.

The PnP manager calls a driver's *AddDevice* routine for each device controlled by the driver. *AddDevice* routines are called during system initialization (when devices are first enumerated), and any time a new device is enumerated while the system is running.

This section contains the following topics:

[AddDevice Routines in Function or Filter Drivers](adddevice-routines-in-function-or-filter-drivers.md)

[AddDevice Routines in Bus Drivers](adddevice-routines-in-bus-drivers.md)

[Guidelines for Writing AddDevice Routines](guidelines-for-writing-adddevice-routines.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Writing%20an%20AddDevice%20Routine%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


