---
title: Optional Dispatch Routines
description: Optional Dispatch Routines
ms.assetid: 38a3fcc9-237d-432d-85db-1594697c96a5
keywords: ["dispatch routines WDK kernel , optional", "optional dispatch routines WDK kernel", "mass storage devices WDK dispatch routines"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Optional Dispatch Routines





Drivers might include the following dispatch routines:

-   [*DispatchCleanup*](https://msdn.microsoft.com/library/windows/hardware/ff543233)

    [**IRP\_MJ\_CLEANUP**](https://msdn.microsoft.com/library/windows/hardware/ff550718) indicates that the last handle for a file object that is associated with the target device object is being closed. Outstanding I/O requests for the file object might still exist. Drivers can implement a *DispatchCleanup* routine to perform cleanup that is not specific to any particular file handle. Drivers can also use their [*DispatchClose*](https://msdn.microsoft.com/library/windows/hardware/ff543255) routine for the same purpose.

-   [*DispatchQueryInformation*](https://msdn.microsoft.com/library/windows/hardware/ff543364), [*DispatchSetInformation*](https://msdn.microsoft.com/library/windows/hardware/ff543399)

    Some highest-level drivers might have to process [**IRP\_MJ\_QUERY\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff550788) and [**IRP\_MJ\_SET\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff550799) IRPs. Such requests indicate that a user-mode application, kernel-mode component, or driver has requested information about the length of the file object (representing the driver's device object) for which the user-mode requester has a handle, or that the user-mode requester is attempting to set an end-of-file on that file object.

    Parallel class and serial device drivers handle these requests by setting the [**FILE\_STANDARD\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545855) or [**FILE\_POSITION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545848) length or position to zero. Other highest-level device drivers should support these requests, particularly if a user-mode application or kernel-mode driver might call C runtime functions to manipulate the file object. File system drivers must support these requests more fully than these highest-level device drivers.

-   [*DispatchFlushBuffers*](https://msdn.microsoft.com/library/windows/hardware/ff543314)

    A driver that caches data in a device or buffers data internally in driver-allocated memory might receive [**IRP\_MJ\_FLUSH\_BUFFERS**](https://msdn.microsoft.com/library/windows/hardware/ff550760). Receipt of this request indicates that the driver should write its buffered data or flush the cached data out to the device, or should discard buffered or cached data that was read from the device.

    For example, the system keyboard and mouse class drivers, which have internal ring buffers for input data from their devices, support the flush request. Drivers of mass-storage devices and drivers layered above them also support this request.

-   [*DispatchShutdown*](https://msdn.microsoft.com/library/windows/hardware/ff543405)

    Any driver that is likely to be called before the system shuts down must handle [**IRP\_MJ\_SHUTDOWN**](https://msdn.microsoft.com/library/windows/hardware/ff550807). The *DispatchShutdown* routine should do whatever driver-determined cleanup is necessary before the power manager sends a system set-power IRP to shut down the system. A driver can call [**IoRegisterShutdownNotification**](https://msdn.microsoft.com/library/windows/hardware/ff549541) or [**IoRegisterLastChanceShutdownNotification**](https://msdn.microsoft.com/library/windows/hardware/ff549518) to register for shutdown notification.

Drivers for mass-storage devices and intermediate drivers layered over them can rely on a highest-level file system driver to send them shutdown IRPs when the system is about to shut down. That is, the FSD is responsible for making sure that any cached file data is written out to peripheral devices, calling underlying drivers to flush data from their device caches or buffers (if any), and so forth before the system is shut down.

The driver of a mass-storage device that caches data internally must provide *DispatchShutdown* and *DispatchFlushBuffers* routines. If a mass-storage driver buffers data in memory but its device has no internal cache, it also must provide *DispatchShutdown* and *DispatchFlushBuffers* routines.

Any intermediate driver layered above a driver that handles [**IRP\_MJ\_FLUSH\_BUFFERS**](https://msdn.microsoft.com/library/windows/hardware/ff550760) and [**IRP\_MJ\_SHUTDOWN**](https://msdn.microsoft.com/library/windows/hardware/ff550807) requests also provide *DispatchShutdown* and *DispatchFlushBuffers* routines.

 

 




