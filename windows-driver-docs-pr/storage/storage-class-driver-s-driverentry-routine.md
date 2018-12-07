---
title: Storage Class Driver's DriverEntry Routine
description: Storage Class Driver's DriverEntry Routine
ms.assetid: 45e929ff-b4e2-4855-8498-15ec4c30f497
keywords:
- DriverEntry WDK storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storage Class Driver's DriverEntry Routine


## <span id="ddk_storage_class_drivers_driverentry_routine_kg"></span><span id="DDK_STORAGE_CLASS_DRIVERS_DRIVERENTRY_ROUTINE_KG"></span>


Like any other Windows NT kernel-mode higher-level driver, the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine of a storage class driver must do the following:

1.  Allocate a driver object extension of appropriate size by calling [**IoAllocateDriverObjectExtension**](https://msdn.microsoft.com/library/windows/hardware/ff548233).

2.  Copy the input registry path into the driver extension for later use (if necessary) and initialize the driver extension.

3.  Define its dispatch entry points in the input driver object.

For more information about a PnP driver's **DriverEntry** routine, see [Writing a DriverEntry Routine](https://msdn.microsoft.com/library/windows/hardware/ff566402).

 

 




