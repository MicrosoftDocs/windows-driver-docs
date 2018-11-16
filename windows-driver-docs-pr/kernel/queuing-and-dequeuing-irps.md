---
title: Queuing and Dequeuing IRPs
description: Queuing and Dequeuing IRPs
ms.assetid: 736107bf-4790-4562-8785-c37fbbed03d3
keywords: ["IRPs WDK kernel , queuing", "queuing IRPs", "dequeuing IRPs", "multiple I/O request handling WDK kernel", "internal IRP queues WDK kernel", "synchronization WDK IRPs", "starting I/O operations", "I/O WDK kernel , operation starting", "StartIo routines", "cancel-safe IRP queues WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Queuing and Dequeuing IRPs





Because the I/O manager supports asynchronous I/O within a multitasking and multithreaded system, I/O requests to a device can come in faster than its driver can process them to completion, particularly in multiprocessor machines. Consequently, IRPs bound to any particular device must be queued in the driver when its device is already busy processing another IRP.

Therefore, a lowest-level driver requires one of the following:

-   A [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine, which the I/O manager calls to start I/O operations for IRPs the driver has queued to a system-supplied IRP queue (see [**IoStartPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550370)).

-   An internal IRP queuing and dequeuing mechanism, which the driver uses to manage IRPs that come in faster than it can satisfy them. Drivers can use device queues, interlocked queues, or cancel-safe queues. For more information, see [Driver-Managed IRP Queues](driver-managed-irp-queues.md).

Only a lowest-level device driver that can satisfy and complete every possible IRP in its dispatch routines needs no *StartIo* routine and no driver-managed queues for IRPs.

Higher-level drivers almost never have *StartIo* routines. Most intermediate drivers have neither *StartIo* routines nor internal queues; an intermediate driver can usually pass IRPs with valid parameters on from its dispatch routines and do whatever postprocessing is required for any IRP in its [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine.

The following describes, in general, some of the design considerations for determining whether to implement a *StartIo* routine with or without internal, driver-managed queues for IRPs.

### StartIo Routines in Drivers

For computer peripheral devices capable of handling only one device I/O operation at a time, device drivers can implement *StartIo* routines. For these drivers, the I/O manager provides [**IoStartPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550370) and [**IoStartNextPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550358) routines to queue and dequeue IRPs to and from a system-supplied IRP queue.

For more information about *StartIo* routines, see [Writing a StartIo Routine](writing-a-startio-routine.md).

### Internal Queues for IRPs in Drivers

If a device can support more than one concurrent I/O operation, its lowest-level device driver must set up internal request queues and manage its own queuing of IRPs. For example, the system serial driver maintains separate queues for read, write, purge, and wait operations on its devices because it supports full-duplex serial devices.

A higher-level driver that sends requests to some number of underlying device drivers also might maintain internal queues of IRPs. For example, file system drivers almost always have internal queues for IRPs.

For more information, see [Driver-Managed IRP Queues](driver-managed-irp-queues.md).

### Internal Queue Synchronization

Drivers with device-dedicated threads and highest-level drivers that use executive worker threads (including most file system drivers) usually set up their own queue for IRPs. The queue is shared by the driver thread or driver-supplied worker-thread callback and by other driver routines that process IRPs.

A driver that implements its own queue structure must ensure that access to the queue is synchronized, and that canceled IRPs are removed from the queue. To make this task simpler for driver writers, cancel-safe IRP queues provide a standard framework you can use when implementing an IRP queue. See [Cancel-Safe IRP Queues](cancel-safe-irp-queues.md) for more information. This is the preferred method for implementing an IRP queue.

Drivers can also implement all IRP queue synchronization and cancel logic explicitly. For example, a driver could use an interlocked queue. The driver's dispatch routines insert IRPs into the interlocked queue and a driver-created thread or the driver's worker-thread callback removes them by calling the **ExInterlocked*Xxx*List** support routines.

For example, the system floppy controller driver uses an interlocked queue. Its device-dedicated thread handles the same processing of IRPs that is done by other device drivers' *StartIo* routines and some of the same processing of IRPs that is done by other device drivers' [*DpcForIsr*](https://msdn.microsoft.com/library/windows/hardware/ff544079) routines.

### Internal Queues with StartIo Routines in Drivers

A driver that manages its own internal queues can also have a *StartIo* routine, but need not. Most lowest-level device drivers either have a *StartIo* routine or manage their own queuing of IRPs, but not both.

An exception to this is the SCSI port driver, which has a *StartIo* routine and manages internal queues of IRPs. The I/O manager queues IRPs to the port driver's *StartIo* routine in the device queue associated with the driver-created device object that represents a SCSI HBA. The SCSI port driver also sets up and manages device queues for IRPs to each target device (corresponding to a SCSI logical unit) on any HBA-driven SCSI bus in the machine.

The SCSI port driver uses its supplemental device queues to hold IRPs sent down from the SCSI class drivers in LU-specific queues whenever any device on a SCSI bus is particularly busy. In effect, this driver's supplemental, LU-specific device queues allow the SCSI port driver to serialize operations for heterogeneous SCSI devices through an HBA while keeping each device on that HBA's SCSI buses as busy as possible.

 

 




