---
title: Optional Dispatch Routines
author: windows-driver-content
description: Optional Dispatch Routines
ms.assetid: 38a3fcc9-237d-432d-85db-1594697c96a5
keywords: ["dispatch routines WDK kernel , optional", "optional dispatch routines WDK kernel", "mass storage devices WDK dispatch routines"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Optional Dispatch Routines


## <a href="" id="ddk-optional-dispatch-routines-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Optional%20Dispatch%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


