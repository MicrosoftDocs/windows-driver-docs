---
title: Storage Drivers and Device Objects
description: Storage Drivers and Device Objects
ms.assetid: dbadebe6-b2ae-4dc2-837b-5ca9634d45d0
keywords:
- storage drivers WDK , device objects
- device objects WDK storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storage Drivers and Device Objects


## <span id="ddk_storage_drivers_and_device_objects_kg"></span><span id="DDK_STORAGE_DRIVERS_AND_DEVICE_OBJECTS_KG"></span>


The storage device stack consists of a tree of device objects created by the drivers that are involved in handling I/O to storage devices on the system. The root of this tree is a functional device object (FDO) for a storage adapter or for another driver stack integrated with the storage stack. The leaves of this tree are device objects for use by file systems and user-mode applications.

Like any PnP driver, a storage class or storage filter driver adds itself to the tree in its AddDevice routine by creating a device object with **IoCreateDevice** and attaching it to the device stack with **IoAttachDeviceToDeviceStack**, using the pointer to the device object passed to the driver's AddDevice routine by the PnP manager at initialization. **IoAttachDeviceToDeviceStack** attaches the new device object to the current top of the device stack.

A tape miniclass, medium changer miniclass, or SCSI miniport driver is not required to create a device object and attach it to the device stack. Instead, the system-supplied tape class, changer class, or SCSI port driver handles these tasks on behalf of the miniclass/miniport, calling miniclass/miniport driver routines to gather the data needed to create the device object.

Storage port drivers create physical device objects (PDOs) of type FILE\_DEVICE\_MASS\_STORAGE. The disk class, CD-ROM class, tape class and changer class drivers create FDOs of types FILE\_DEVICE\_DISK, FILE\_DEVICE\_CD\_ROM, FILE\_DEVICE\_TAPE, and FILE\_DEVICE\_CHANGER respectively.

For information about designing PnP drivers, see the [PnP Driver Design Guidelines](https://msdn.microsoft.com/library/windows/hardware/ff559623). For information about PnP-related **Io***Xxx* routines, see the [Plug and Play Routines](https://msdn.microsoft.com/library/windows/hardware/ff558809).

 

 




