---
title: Storage Drivers and Device Objects
author: windows-driver-content
description: Storage Drivers and Device Objects
ms.assetid: dbadebe6-b2ae-4dc2-837b-5ca9634d45d0
keywords: ["storage drivers WDK , device objects", "device objects WDK storage"]
---

# Storage Drivers and Device Objects


## <span id="ddk_storage_drivers_and_device_objects_kg"></span><span id="DDK_STORAGE_DRIVERS_AND_DEVICE_OBJECTS_KG"></span>


The storage device stack consists of a tree of device objects created by the drivers that are involved in handling I/O to storage devices on the system. The root of this tree is a functional device object (FDO) for a storage adapter or for another driver stack integrated with the storage stack. The leaves of this tree are device objects for use by file systems and user-mode applications.

Like any PnP driver, a storage class or storage filter driver adds itself to the tree in its AddDevice routine by creating a device object with **IoCreateDevice** and attaching it to the device stack with **IoAttachDeviceToDeviceStack**, using the pointer to the device object passed to the driver's AddDevice routine by the PnP manager at initialization. **IoAttachDeviceToDeviceStack** attaches the new device object to the current top of the device stack.

A tape miniclass, medium changer miniclass, or SCSI miniport driver is not required to create a device object and attach it to the device stack. Instead, the system-supplied tape class, changer class, or SCSI port driver handles these tasks on behalf of the miniclass/miniport, calling miniclass/miniport driver routines to gather the data needed to create the device object.

Storage port drivers create physical device objects (PDOs) of type FILE\_DEVICE\_MASS\_STORAGE. The disk class, CD-ROM class, tape class and changer class drivers create FDOs of types FILE\_DEVICE\_DISK, FILE\_DEVICE\_CD\_ROM, FILE\_DEVICE\_TAPE, and FILE\_DEVICE\_CHANGER respectively.

For information about designing PnP drivers, see the [PnP Driver Design Guidelines](https://msdn.microsoft.com/library/windows/hardware/ff559623). For information about PnP-related **Io***Xxx* routines, see the [Plug and Play Routines](https://msdn.microsoft.com/library/windows/hardware/ff558809).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Storage%20Drivers%20and%20Device%20Objects%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


