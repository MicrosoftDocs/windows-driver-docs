---
title: Storage Filter Driver's IoCompletion Routines
description: Storage Filter Driver's IoCompletion Routines
keywords:
- storage filter drivers WDK , IoCompletion
- filter drivers WDK storage , IoCompletion
- SFD WDK storage , IoCompletion
- IoCompletion
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storage Filter Driver's IoCompletion Routines

A storage filter driver's [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine is called when lower-level drivers (port, class, and additional filter drivers, if any) have called [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest). The *IoCompletion* routine of an storage filter driver (SFD) should return **STATUS_MORE_PROCESSING_REQUIRED** to prevent completion processing of a driver-allocated IRP, or to retain an original IRP if the SFD will reuse the IRP before completing it.

Like any other higher-level driver, the [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine of an SFD is responsible for calling [**IoFreeIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iofreeirp) to release any IRP the driver's *Dispatch* routines created with [**IoAllocateIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocateirp) or [**IoBuildAsynchronousFsdRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuildasynchronousfsdrequest).

Depending on its device, an SFD might supply an [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine for IRPs it sends to the next-lower driver from its *Dispatch* routines. In particular, a device that retrieves and processes data in a nonstandard format might require the SFD to have a *TranslateDataIn* routine called from its *IoCompletion* routine for transfer requests from such a device to system memory.

Note that such a *TranslateDataIn* routine would be called at IRQL == DISPATCH_LEVEL and in an arbitrary thread context. Therefore, the buffer into which the driver returns data either must be located in nonpaged pool or must be locked down and accessible using mapped, nonpaged system-space virtual addresses. For more information about safely accessing user-supplied buffers at raised IRQL, see [Methods for Accessing Data Buffers](../kernel/methods-for-accessing-data-buffers.md).

In general, a storage filter driver should supply an [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine with the same functionality as a class driver's *IoCompletion* routine for IRPs that the filter driver sets up with SRBs and CDBs. Consequently, a storage filter driver might have any or all of the *ReleaseQueue*, *InterpretRequestSense*, or *RetryRequest* routines that can be called from a storage class driver's *IoCompletion* routines.

For more information about *InterpretRequestSense*, *RetryRequest*, and *ReleaseQueue* routines, see [Storage Class Drivers](introduction-to-storage-class-drivers.md). For more information about general requirements for [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routines, see [Using IoCompletion Routines](../kernel/using-iocompletion-routines.md).
