---
title: Writing a DriverEntry Routine
author: windows-driver-content
description: Writing a DriverEntry Routine
MS-HAID:
- 'DrvComps\_080f7e6b-b429-4a72-9c89-34b652eb337d.xml'
- 'kernel.writing\_a\_driverentry\_routine'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c33bc82b-6181-4e31-b272-aaadb2d9b058
keywords: ["standard driver routines WDK kernel , DriverEntry routine", "driver routines WDK kernel , DriverEntry routine", "routines WDK kernel , DriverEntry routine", "DriverEntry WDK kernel", "DriverEntry WDK kernel , about DriverEntry routine", "driver initialization WDK kernel", "initializing drivers"]
---

# Writing a DriverEntry Routine


## <a href="" id="ddk-writing-a-driverentry-routine-kg"></a>


Each driver must have a [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine, which initializes driver-wide data structures and resources. The I/O manager calls the **DriverEntry** routine when it loads the driver.

In a driver that supports Plug and Play (PnP), as all drivers should, the **DriverEntry** routine is responsible for *driver* initialization, while the [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine (and, possibly, the dispatch routine that handles a PnP [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request) is responsible for *device* initialization. Driver initialization includes exporting the driver's other entry points, initializing certain objects the driver uses, and setting up various per-driver system resources. (Non-PnP drivers have significantly different requirements, as described in the Driver Development Kit \[DDK\] for Microsoft Windows NT 4.0 and earlier.)

**DriverEntry** routines are called in the context of a system thread at IRQL = PASSIVE\_LEVEL.

A **DriverEntry** routine can be pageable and should be in an INIT segment so it will be discarded. Use an **alloc\_text** pragma directive, as illustrated in the sample drivers that are provided with the Windows Driver Kit (WDK).

This section contains the following topics:

[DriverEntry's Required Responsibilities](driverentry-s-required-responsibilities.md)

[DriverEntry's Optional Responsibilities](driverentry-s-optional-responsibilities.md)

[DriverEntry Return Values](driverentry-return-values.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Writing%20a%20DriverEntry%20Routine%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


