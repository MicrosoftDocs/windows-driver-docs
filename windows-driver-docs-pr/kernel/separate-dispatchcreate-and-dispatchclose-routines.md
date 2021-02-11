---
title: Separate DispatchCreate and DispatchClose Routines
description: Separate DispatchCreate and DispatchClose Routines
keywords: ["dispatch routines WDK kernel , DispatchCreate routine", "dispatch routines WDK kernel , DispatchClose routine", "DispatchClose routine", "DispatchCreate routine", "IRP_MJ_CREATE I/O function code", "IRP_MJ_CLOSE I/O function code", "create dispatch routines WDK kernel", "close dispatch routines WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Separate DispatchCreate and DispatchClose Routines





A driver's *Dispatch* routines for [**IRP\_MJ\_CREATE**](./irp-mj-create.md) and [**IRP\_MJ\_CLOSE**](./irp-mj-close.md) requests might do nothing more than complete the input IRP with STATUS\_SUCCESS. For more information, see [Completing IRPs](completing-irps.md).

Another driver's *Dispatch* routines for **IRP\_MJ\_CREATE** and **IRP\_MJ\_CLOSE** requests might do more work, depending on the underlying device driver or on the underlying device. Consider the following scenarios:

- On receipt of a create request, a class driver might initialize an internal queue and send an [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](./irp-mj-internal-device-control.md) request down to the corresponding port driver requesting device configuration information or exclusive access to a controller port.

- Receipt of **IRP\_MJ\_CLOSE** indicates that the last reference to the file object that is associated with the target device object has been removed. This implies that all handles to the file object has been closed and all outstanding I/O requests have been completed or canceled.

- On receipt of a create request, a driver of an infrequently used device might call [**MmLockPagableCodeSection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmlockpagablecodesection) to make resident some of the driver routines that process other **IRP\_MJ\_*XXX*** requests. On receipt of a reciprocal close request, the driver might call [**MmUnlockPagableImageSection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmunlockpagableimagesection) to conserve system memory by having its pageable-image section paged out when all file object handles for such a driver's device object(s) are closed.

Some drivers handle **IRP\_MJ\_CLOSE** requests only for symmetry because, after their device objects have been opened by a protected subsystem or higher-level driver, the lower-level drivers' device objects are not closed until the system itself is shut down. For example, keyboard and mouse drivers set up device objects representing physical devices that must be functional while the system is running, so these drivers might have minimal [*DispatchClose*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routines for symmetry, or they might have combined [*DispatchCreateClose*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routines.

If the device controlled by a lower-level driver must be available for the system to continue running, the driver's *DispatchClose* routine generally will not be called. For example, some of the system disk drivers have no *DispatchClose* routine, but these drivers usually have [*DispatchFlushBuffers*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) and [*DispatchShutdown*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routines to complete any outstanding file I/O operations before the system is shut down.

While you can implement separate [*DRIVER_DISPATCH*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) and *DispatchClose* routines, drivers sometimes have [a single DispatchCreateClose routine](a-single-dispatchcreateclose-routine.md) for handling both create and close requests.

 

