---
title: Which Type of DPC Should You Use
description: Which Type of DPC Should You Use
keywords: ["deferred procedure calls WDK kernel", "DPCs WDK kernel", "DpcForIsr", "CustomDpc"]
ms.date: 06/16/2017
---

# Which Type of DPC Should You Use?





Depending on a driver's design, it can have any of the following:

-   A single [*DpcForIsr*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_dpc_routine) to complete all interrupt-driven I/O operations

-   A set of one or more [*CustomDpc*](/windows-hardware/drivers/ddi/wdm/nc-wdm-kdeferred_routine) routines.

-   Both a *DpcForIsr* and a set of operation-specific *CustomDpc* routines

Whether a driver has a single *DpcForIsr* routine, a set of *CustomDpc* routines, or both, depends on the nature of its underlying device and the set of I/O requests it must support.

Most lowest-level device drivers have a single *DpcForIsr* routine to complete I/O processing for each IRP that requires one or more operations on their respective devices. Using a single *DpcForIsr* to complete per-request, interrupt-driven I/O operations on a device that does one operation at a time is relatively easy. Such a driver's ISR need only call [**IoRequestDpc**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iorequestdpc) for each interrupt-driven I/O operation.

Few lowest-level drivers have *CustomDpc* routines unless their devices require more than one DPC to complete a varied set of interrupt-driven I/O operations.

Using a single *DpcForIsr* to complete overlapped, interrupt-driven I/O operations on a device that can do concurrent operations is possible with careful design, but can be relatively difficult. In addition to or instead of queuing a *DpcForIsr*, an ISR can queue a set of operation-specific, driver-supplied *CustomDpc* routines by calling [**KeInsertQueueDpc**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinsertqueuedpc).

For example, consider some of the design challenges involved in writing a serial driver. As the driver of a full-duplex device, a serial driver cannot rely on a one-to-one correspondence between the order in which IRPs are queued to a *StartIo* routine and the sequence of interrupts from its device in a multitasking, multiprocessor system. Furthermore, serial drivers must handle timing out requests and asynchronous user-generated requests to cancel previously requested operations, to purge buffered data, and so forth.

Consequently, a serial driver might maintain internal queues for the read, write, purge, and wait operations that user-mode COM port applications can request. It also could maintain reference counts or use some other tracking mechanism, such as a set of flags, for the IRPs in its internal queues. Its ISR would call **KeInsertQueueDpc** with any of a number of driver-allocated and initialized DPC objects, each associated with a driver-supplied *CustomDpc* routine.

 

