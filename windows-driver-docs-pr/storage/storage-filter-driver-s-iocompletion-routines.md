---
title: Storage Filter Driver's IoCompletion Routines
description: Storage Filter Driver's IoCompletion Routines
ms.assetid: 1a27598b-7113-4f95-8777-bbb10003c268
keywords:
- storage filter drivers WDK , IoCompletion
- filter drivers WDK storage , IoCompletion
- SFD WDK storage , IoCompletion
- IoCompletion
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storage Filter Driver's IoCompletion Routines


## <span id="ddk_storage_filter_drivers_iocompletion_routines_kg"></span><span id="DDK_STORAGE_FILTER_DRIVERS_IOCOMPLETION_ROUTINES_KG"></span>


A storage filter driver's [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine is called when lower-level drivers (port, class, and additional filter drivers, if any) have called [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343). The *IoCompletion* routine of an storage filter driver (SFD) should return **STATUS\_MORE\_PROCESSING\_REQUIRED** to prevent completion processing of a driver-allocated IRP, or to retain an original IRP if the SFD will reuse the IRP before completing it.

Like any other higher-level driver, the [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine of an SFD is responsible for calling [**IoFreeIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549113) to release any IRP the driver's *Dispatch* routines created with [**IoAllocateIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548257) or [**IoBuildAsynchronousFsdRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548310).

Depending on its device, an SFD might supply an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine for IRPs it sends to the next-lower driver from its *Dispatch* routines. In particular, a device that retrieves and processes data in a nonstandard format might require the SFD to have a *TranslateDataIn* routine called from its *IoCompletion* routine for transfer requests from such a device to system memory.

Note that such a *TranslateDataIn* routine would be called at IRQL == DISPATCH\_LEVEL and in an arbitrary thread context. Therefore, the buffer into which the driver returns data either must be located in nonpaged pool or must be locked down and accessible using mapped, nonpaged system-space virtual addresses. For more information about safely accessing user-supplied buffers at raised IRQL, see [Methods for Accessing Data Buffers](https://msdn.microsoft.com/library/windows/hardware/ff554436).

In general, a storage filter driver should supply an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine with the same functionality as a class driver's *IoCompletion* routine for IRPs that the filter driver sets up with SRBs and CDBs. Consequently, a storage filter driver might have any or all of the *ReleaseQueue*, *InterpretRequestSense*, or *RetryRequest* routines that can be called from a storage class driver's *IoCompletion* routines.

For more information about *InterpretRequestSense*, *RetryRequest*, and *ReleaseQueue* routines, see [Storage Class Drivers](storage-class-drivers.md). For more information about general requirements for [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routines, see [Using IoCompletion Routines](https://msdn.microsoft.com/library/windows/hardware/ff565398).

 

 




