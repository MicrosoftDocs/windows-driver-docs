---
title: Storage Class Driver's DriverEntry Routine
description: Storage Class Driver's DriverEntry Routine
keywords:
- DriverEntry WDK storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storage Class Driver's DriverEntry Routine


## <span id="ddk_storage_class_drivers_driverentry_routine_kg"></span><span id="DDK_STORAGE_CLASS_DRIVERS_DRIVERENTRY_ROUTINE_KG"></span>


Like any other Windows NT kernel-mode higher-level driver, the [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine of a storage class driver must do the following:

1.  Allocate a driver object extension of appropriate size by calling [**IoAllocateDriverObjectExtension**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocatedriverobjectextension).

2.  Copy the input registry path into the driver extension for later use (if necessary) and initialize the driver extension.

3.  Define its dispatch entry points in the input driver object.

For more information about a PnP driver's **DriverEntry** routine, see [Writing a DriverEntry Routine](../kernel/writing-a-driverentry-routine.md).

 

