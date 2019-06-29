---
title: Restrictions on Pageable Code in Storage Drivers
description: Restrictions on Pageable Code in Storage Drivers
ms.assetid: 1958f22f-5563-41e9-9c3f-dec8a4ac80c0
keywords:
- storage drivers WDK , pageable code restrictions
- pageable code restrictions WDK storage
- deadlocks WDK storage
- paging path WDK storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Restrictions on Pageable Code in Storage Drivers


## <span id="ddk_restrictions_on_pageable_code_in_storage_drivers_kg"></span><span id="DDK_RESTRICTIONS_ON_PAGEABLE_CODE_IN_STORAGE_DRIVERS_KG"></span>


To prevent deadlock, no part of a storage driver that is used to service read or write requests should have pageable code, nor should it ever attempt to access pageable memory. This is because the driver's [**DispatchRead**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch) and [**DispatchWrite**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch) routines can be called at IRQL &gt; PASSIVE\_LEVEL, and the in-paging I/O that services a page fault takes place at IRQL = APC\_LEVEL.

Similar rules apply to a storage driver's device control dispatch routine, [**DispatchDeviceControl**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch), with certain qualifications. A storage driver's device control dispatch routine must not contain pageable code or access pageable memory. The dispatch routine must be able to receive IOCTL requests that are intended for other drivers at arbitrary IRQLs and pass them down the driver stack. Drivers *must* pass all unhandled IOCTL requests down the stack without altering the IRQL or the context of the request.

However, Microsoft requires that all *storage* IOCTL requests be submitted at PASSIVE\_LEVEL, so although the dispatch routine is not itself pageable, it can call pageable subroutines to handle storage IOCTL requests. These subroutines can also access pageable memory.

Routines such as [**DriverEntry**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_initialize), [**Reinitialize**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nc-ntddk-driver_reinitialize), and [**Unload**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_unload), that do no I/O and run at IRQL = PASSIVE\_LEVEL can also have pageable code.

Special considerations apply to drivers that manage storage devices in the paging path. A driver is in the "paging path" if it participates in I/O operations on the paging file. When a storage driver is in the paging path, its [**DispatchPower**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch) routine for IRP\_MJ\_POWER requests must not be pageable.

By default, the code for kernel-mode drivers is not pageable, nor is the global memory used by kernel-mode drivers pageable. For information about how to make code pageable, see [Making Driver Code or Data Pageable](https://docs.microsoft.com/windows-hardware/drivers/kernel/making-driver-code-or-data-pageable).

 

 




