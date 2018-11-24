---
title: Storage Class Driver's AddDevice Routine
description: Storage Class Driver's AddDevice Routine
ms.assetid: ff07ae84-2748-44b4-88c6-e67f1d4c9268
keywords:
- AddDevice routine WDK storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storage Class Driver's AddDevice Routine


## <span id="ddk_storage_class_drivers_adddevice_routine_kg"></span><span id="DDK_STORAGE_CLASS_DRIVERS_ADDDEVICE_ROUTINE_KG"></span>


The PnP manager calls a storage class driver's [**AddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine when it detects a device controlled by that driver. A storage class driver's *AddDevice* routine:

-   Claims the device as described in [Storage Class Driver's ClaimDevice Routine](storage-class-driver-s-claimdevice-routine.md), or, if the driver is unable to claim the device, returns STATUS\_SUCCESS.

-   If the driver successfully claims the device, creates a device object (FDO).

-   Registers device interfaces that applications and other system devices can use. The class driver enables such interfaces when it receives a PnP start request.

-   Prepares the device object to handle a start request as described in [Writing an AddDevice Routine](https://msdn.microsoft.com/library/windows/hardware/ff566398).

-   Attaches the device object to the device stack by calling [**IoAttachDeviceToDeviceStack**](https://msdn.microsoft.com/library/windows/hardware/ff548300) with the input PDO.

-   If the device starts in a known power state, calls [**PoSetPowerState**](https://msdn.microsoft.com/library/windows/hardware/ff559765).

-   Clears the DO\_DEVICE\_INITIALIZING flag on the new device object.

A storage class driver stores the pointer returned by **IoAttachDeviceToDeviceStack** in the device extension of its own device object (FDO) that represents the newly claimed device, and *must use this pointer in all subsequent requests that the class driver sends to the next-lower driver*. The driver also stores the pointer to the input PDO in the device extension, but after **IoAttachDeviceToDeviceStack** returns the driver must use the pointer to the input PDO only in calls to PnP **Io***Xxx* routines that take such a pointer as a parameter.

For more information, see [Writing an AddDevice Routine](https://msdn.microsoft.com/library/windows/hardware/ff566398).

 

 




