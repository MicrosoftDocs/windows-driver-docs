---
title: StartIo Routines in Higher-Level Drivers
author: windows-driver-content
description: StartIo Routines in Higher-Level Drivers
MS-HAID:
- 'IRPs\_9d507e46-e086-4c80-a9c8-1c8dc84d9eff.xml'
- 'kernel.startio\_routines\_in\_higher\_level\_drivers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8b0e3bef-4a73-4cf8-b71a-6aedf451d648
keywords: ["StartIo routines, higher-level drivers"]
---

# StartIo Routines in Higher-Level Drivers


## <a href="" id="ddk-startio-routines-in-higher-level-drivers-kg"></a>


Any higher-level driver can have a [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine. However, such a driver is unlikely to be interoperable with existing lower-level drivers and is likely to exhibit poor performance characteristics.

A *StartIo* routine in a higher-level driver has the following effects:

-   Incoming IRPs can be queued by calling [**IoStartPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550370) from the driver's *Dispatch*Xxx routine(s) and [**IoStartNextPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550358) from its [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine(s), thereby causing IRPs to be processed one at a time through the *StartIo* routine.

-   The driver's I/O throughput could become noticeably slower during periods of heavy I/O demand, because its *StartIo* routine can become a bottleneck.

-   The driver's *StartIo* routine calls [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) with each IRP at IRQL = DISPATCH\_LEVEL, thereby causing all lower-level drivers' dispatch routines also to run at IRQL = DISPATCH\_LEVEL. This restricts the set of support routines that lower drivers can call in their dispatch routines. Because most driver writers assume their drivers' dispatch routines run at IRQL &lt; DISPATCH\_LEVEL, the higher-level driver is unlikely to be interoperable with many existing lower-level drivers.

-   The *StartIo* routine reduces overall system throughput because it and the dispatch routines of all lower-level drivers in its chain are run at IRQL = DISPATCH\_LEVEL.

    For more information about the IRQLs at which standard driver routines are run, see [Managing Hardware Priorities](managing-hardware-priorities.md).

None of the system-supplied higher-level drivers has a *StartIo* routine, because it can slow IRP processing for the driver itself, for all drivers above and below it, and for the system overall.

Most higher-level drivers simply send IRPs to lower-level drivers from their dispatch routines and do any necessary clean-up processing in their *IoCompletion* routines.

However, higher-level drivers can set up internal queues for IRPs that request particular kinds of operations, or set up internal queues to hold IRPs bound for a set of heterogeneous underlying devices like the SCSI port driver. For more information, see [Queuing and Dequeuing IRPs](queuing-and-dequeuing-irps.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20StartIo%20Routines%20in%20Higher-Level%20Drivers%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


