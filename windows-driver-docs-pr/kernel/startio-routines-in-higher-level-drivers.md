---
title: StartIo Routines in Higher-Level Drivers
description: StartIo Routines in Higher-Level Drivers
keywords: ["StartIo routines, higher-level drivers"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# StartIo Routines in Higher-Level Drivers





Any higher-level driver can have a [*StartIo*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio) routine. However, such a driver is unlikely to be interoperable with existing lower-level drivers and is likely to exhibit poor performance characteristics.

A *StartIo* routine in a higher-level driver has the following effects:

-   Incoming IRPs can be queued by calling [**IoStartPacket**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iostartpacket) from the driver's *Dispatch*Xxx routine(s) and [**IoStartNextPacket**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iostartnextpacket) from its [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine(s), thereby causing IRPs to be processed one at a time through the *StartIo* routine.

-   The driver's I/O throughput could become noticeably slower during periods of heavy I/O demand, because its *StartIo* routine can become a bottleneck.

-   The driver's *StartIo* routine calls [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) with each IRP at IRQL = DISPATCH\_LEVEL, thereby causing all lower-level drivers' dispatch routines also to run at IRQL = DISPATCH\_LEVEL. This restricts the set of support routines that lower drivers can call in their dispatch routines. Because most driver writers assume their drivers' dispatch routines run at IRQL &lt; DISPATCH\_LEVEL, the higher-level driver is unlikely to be interoperable with many existing lower-level drivers.

-   The *StartIo* routine reduces overall system throughput because it and the dispatch routines of all lower-level drivers in its chain are run at IRQL = DISPATCH\_LEVEL.

    For more information about the IRQLs at which standard driver routines are run, see [Managing Hardware Priorities](managing-hardware-priorities.md).

None of the system-supplied higher-level drivers has a *StartIo* routine, because it can slow IRP processing for the driver itself, for all drivers above and below it, and for the system overall.

Most higher-level drivers simply send IRPs to lower-level drivers from their dispatch routines and do any necessary clean-up processing in their *IoCompletion* routines.

However, higher-level drivers can set up internal queues for IRPs that request particular kinds of operations, or set up internal queues to hold IRPs bound for a set of heterogeneous underlying devices like the SCSI port driver. For more information, see [Queuing and Dequeuing IRPs](queuing-and-dequeuing-irps.md).

 

