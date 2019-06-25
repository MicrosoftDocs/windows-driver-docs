---
title: Separate DispatchCreate and DispatchClose Routines
description: Separate DispatchCreate and DispatchClose Routines
ms.assetid: b2e05555-c70d-4293-8622-51eea92091b1
keywords: ["dispatch routines WDK kernel , DispatchCreate routine", "dispatch routines WDK kernel , DispatchClose routine", "DispatchClose routine", "DispatchCreate routine", "IRP_MJ_CREATE I/O function code", "IRP_MJ_CLOSE I/O function code", "create dispatch routines WDK kernel", "close dispatch routines WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Separate DispatchCreate and DispatchClose Routines





A driver's *Dispatch* routines for [**IRP\_MJ\_CREATE**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-create) and [**IRP\_MJ\_CLOSE**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-close) requests might do nothing more than complete the input IRP with STATUS\_SUCCESS. For more information, see [Completing IRPs](completing-irps.md).

Another driver's *Dispatch* routines for **IRP\_MJ\_CREATE** and **IRP\_MJ\_CLOSE** requests might do more work, depending on the underlying device driver or on the underlying device. Consider the following scenarios:

- On receipt of a create request, a class driver might initialize an internal queue and send an [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-internal-device-control) request down to the corresponding port driver requesting device configuration information or exclusive access to a controller port.

- Receipt of **IRP\_MJ\_CLOSE** indicates that the last reference to the file object that is associated with the target device object has been removed. This implies that all handles to the file object has been closed and all outstanding I/O requests have been completed or canceled.

- On receipt of a create request, a driver of an infrequently used device might call [**MmLockPagableCodeSection**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-mmlockpagablecodesection) to make resident some of the driver routines that process other **IRP\_MJ\_*XXX*** requests. On receipt of a reciprocal close request, the driver might call [**MmUnlockPagableImageSection**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-mmunlockpagableimagesection) to conserve system memory by having its pageable-image section paged out when all file object handles for such a driver's device object(s) are closed.

Some drivers handle **IRP\_MJ\_CLOSE** requests only for symmetry because, after their device objects have been opened by a protected subsystem or higher-level driver, the lower-level drivers' device objects are not closed until the system itself is shut down. For example, keyboard and mouse drivers set up device objects representing physical devices that must be functional while the system is running, so these drivers might have minimal [*DispatchClose*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch) routines for symmetry, or they might have combined [*DispatchCreateClose*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch) routines.

If the device controlled by a lower-level driver must be available for the system to continue running, the driver's *DispatchClose* routine generally will not be called. For example, some of the system disk drivers have no *DispatchClose* routine, but these drivers usually have [*DispatchFlushBuffers*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch) and [*DispatchShutdown*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch) routines to complete any outstanding file I/O operations before the system is shut down.

While you can implement separate [*DRIVER_DISPATCH*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch) and *DispatchClose* routines, drivers sometimes have [a single DispatchCreateClose routine](a-single-dispatchcreateclose-routine.md) for handling both create and close requests.

 

 




