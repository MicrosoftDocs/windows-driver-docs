---
title: Storage Class Driver's Dispatch Routines
description: Storage Class Driver's Dispatch Routines
keywords:
- dispatch routines WDK storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storage Class Driver's Dispatch Routines


## <span id="ddk_storage_class_drivers_dispatch_routines_kg"></span><span id="DDK_STORAGE_CLASS_DRIVERS_DISPATCH_ROUTINES_KG"></span>


Class driver [*DRIVER_DISPATCH*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) and [**DispatchClose**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routines usually have no device-specific requirements. Most storage class drivers are intermediate drivers; their dispatch routines just return STATUS\_SUCCESS to indicate that a given device object exists so that higher-level drivers and, indirectly, user-mode applications can open the device for I/O and close the device afterward.

Class driver [**DispatchDeviceControl**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) and [**DispatchInternalDeviceControl**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routines must be resident; that is, they cannot be pageable nor part of a driver's pageable-image section. Depending on the IOCTL of a given request, such a dispatch routine might call a paged routine or wait for a call from a synchronization or notification object (thereby blocking the executing thread), but the dispatch routine must be able to pass an unknown IOCTL through at DISPATCH\_LEVEL.

A storage class driver must have a [**DispatchPnP**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine for requests to start, stop, and remove the device and respond to other PnP requests such as notification that the device is on the paging path. For details about handling a PnP start request, see [Handling PnP Start in a Storage Class Driver](handling-pnp-start-in-a-storage-class-driver.md). For details about handling other PnP requests, see [Handling PnP Requests to Storage Peripherals](handling-pnp-requests-to-storage-peripherals.md).

A storage class driver must also have a [**DispatchPower**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine for requests to set the power state of its device. For details, see [Handling Power Requests to Storage Peripherals](handling-power-requests-to-storage-peripherals.md).

A storage class driver must have a [**DispatchShutdown**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine and possibly a [**DispatchFlushBuffers**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine if its device caches data internally, if its device might be attached to a bus driven by an HBA that caches data internally, or if a file system is layered above the class driver. To maintain data integrity, such a cache should be flushed to the device before the system is shut down.

See also [Writing Dispatch Routines](../kernel/writing-dispatch-routines.md) for more information about general requirements for dispatch routines.

 

