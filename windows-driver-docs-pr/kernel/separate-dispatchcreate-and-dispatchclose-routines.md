---
title: Separate DispatchCreate and DispatchClose Routines
author: windows-driver-content
description: Separate DispatchCreate and DispatchClose Routines
MS-HAID:
- 'DrvComps\_f01ee9fe-cee6-4ce2-b956-229ac4e9907a.xml'
- 'kernel.separate\_dispatchcreate\_and\_dispatchclose\_routines'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b2e05555-c70d-4293-8622-51eea92091b1
keywords: ["dispatch routines WDK kernel , DispatchCreate routine", "dispatch routines WDK kernel , DispatchClose routine", "DispatchClose routine", "DispatchCreate routine", "IRP_MJ_CREATE I/O function code", "IRP_MJ_CLOSE I/O function code", "create dispatch routines WDK kernel", "close dispatch routines WDK kernel"]
---

# Separate DispatchCreate and DispatchClose Routines


## <a href="" id="ddk-separate-dispatchcreate-and-dispatchclose-routines-kg"></a>


A driver's *Dispatch* routines for [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff550729) and [**IRP\_MJ\_CLOSE**](https://msdn.microsoft.com/library/windows/hardware/ff550720) requests might do nothing more than complete the input IRP with STATUS\_SUCCESS. For more information, see [Completing IRPs](completing-irps.md).

Another driver's *Dispatch* routines for **IRP\_MJ\_CREATE** and **IRP\_MJ\_CLOSE** requests might do more work, depending on the underlying device driver or on the underlying device. Consider the following scenarios:

-   On receipt of a create request, a class driver might initialize an internal queue and send an [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766) request down to the corresponding port driver requesting device configuration information or exclusive access to a controller port.

-   Receipt of **IRP\_MJ\_CLOSE** indicates that the last reference to the file object that is associated with the target device object has been removed. This implies that all handles to the file object has been closed and all outstanding I/O requests have been completed or canceled.

-   On receipt of a create request, a driver of an infrequently used device might call [**MmLockPagableCodeSection**](https://msdn.microsoft.com/library/windows/hardware/ff554601) to make resident some of the driver routines that process other **IRP\_MJ\_*XXX*** requests. On receipt of a reciprocal close request, the driver might call [**MmUnlockPagableImageSection**](https://msdn.microsoft.com/library/windows/hardware/ff556377) to conserve system memory by having its pageable-image section paged out when all file object handles for such a driver's device object(s) are closed.

Some drivers handle **IRP\_MJ\_CLOSE** requests only for symmetry because, after their device objects have been opened by a protected subsystem or higher-level driver, the lower-level drivers' device objects are not closed until the system itself is shut down. For example, keyboard and mouse drivers set up device objects representing physical devices that must be functional while the system is running, so these drivers might have minimal [*DispatchClose*](https://msdn.microsoft.com/library/windows/hardware/ff543255) routines for symmetry, or they might have combined [*DispatchCreateClose*](https://msdn.microsoft.com/library/windows/hardware/ff543270) routines.

If the device controlled by a lower-level driver must be available for the system to continue running, the driver's *DispatchClose* routine generally will not be called. For example, some of the system disk drivers have no *DispatchClose* routine, but these drivers usually have [*DispatchFlushBuffers*](https://msdn.microsoft.com/library/windows/hardware/ff543314) and [*DispatchShutdown*](https://msdn.microsoft.com/library/windows/hardware/ff543405) routines to complete any outstanding file I/O operations before the system is shut down.

While you can implement separate [*DispatchCreate*](https://msdn.microsoft.com/library/windows/hardware/ff543266) and *DispatchClose* routines, drivers sometimes have [a single DispatchCreateClose routine](a-single-dispatchcreateclose-routine.md) for handling both create and close requests.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Separate%20DispatchCreate%20and%20DispatchClose%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


