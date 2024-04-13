---
title: Restrictions on Pageable Code in Storage Drivers
description: Restrictions on Pageable Code in Storage Drivers
keywords:
- storage drivers WDK , pageable code restrictions
- pageable code restrictions WDK storage
- deadlocks WDK storage
- paging path WDK storage
ms.date: 04/20/2017
---

# Restrictions on Pageable Code in Storage Drivers


## <span id="ddk_restrictions_on_pageable_code_in_storage_drivers_kg"></span><span id="DDK_RESTRICTIONS_ON_PAGEABLE_CODE_IN_STORAGE_DRIVERS_KG"></span>


To prevent deadlock, no part of a storage driver that is used to service read or write requests should have pageable code, nor should it ever attempt to access pageable memory. This is because the driver's [**DispatchRead**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) and [**DispatchWrite**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routines can be called at IRQL &gt; PASSIVE\_LEVEL, and the in-paging I/O that services a page fault takes place at IRQL = APC\_LEVEL.

Similar rules apply to a storage driver's device control dispatch routine, [**DispatchDeviceControl**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch), with certain qualifications. A storage driver's device control dispatch routine must not contain pageable code or access pageable memory. The dispatch routine must be able to receive IOCTL requests that are intended for other drivers at arbitrary IRQLs and pass them down the driver stack. Drivers *must* pass all unhandled IOCTL requests down the stack without altering the IRQL or the context of the request.

However, Microsoft requires that all *storage* IOCTL requests be submitted at PASSIVE\_LEVEL, so although the dispatch routine is not itself pageable, it can call pageable subroutines to handle storage IOCTL requests. These subroutines can also access pageable memory.

Routines such as [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize), [**Reinitialize**](/windows-hardware/drivers/ddi/ntddk/nc-ntddk-driver_reinitialize), and [**Unload**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload), that do no I/O and run at IRQL = PASSIVE\_LEVEL can also have pageable code.

Special considerations apply to drivers that manage storage devices in the paging path. A driver is in the "paging path" if it participates in I/O operations on the paging file. When a storage driver is in the paging path, its [**DispatchPower**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine for IRP\_MJ\_POWER requests must not be pageable.

By default, the code for kernel-mode drivers is not pageable, nor is the global memory used by kernel-mode drivers pageable. For information about how to make code pageable, see [Making Driver Code or Data Pageable](../kernel/detecting-code-that-can-be-pageable.md).

