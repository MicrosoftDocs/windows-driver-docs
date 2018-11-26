---
title: Handling PnP Initialization in a Storage Class Driver
description: Handling PnP Initialization in a Storage Class Driver
ms.assetid: 472e52c8-a214-418b-a82f-fd4a9bcc894e
keywords:
- storage class drivers WDK , PnP
- class drivers WDK storage , PnP
- PnP WDK storage
- Plug and Play WDK storage
- initializing storage class drivers
- storage class drivers WDK , initializing
- class drivers WDK storage , initializing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling PnP Initialization in a Storage Class Driver


## <span id="ddk_handling_pnp_initialization_in_a_storage_class_driver_kg"></span><span id="DDK_HANDLING_PNP_INITIALIZATION_IN_A_STORAGE_CLASS_DRIVER_KG"></span>


Initialization of a storage class driver is much the same as initialization of any PnP driver.

Storage class driver initialization begins when the PnP manager calls the driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine to load and initialize the driver. Then the PnP manager calls the storage class driver's [**AddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine, passing a pointer to a physical device object (PDO) that represents the target device.

In its *AddDevice* routine, the class driver calls [**IoGetAttachedDeviceReference**](https://msdn.microsoft.com/library/windows/hardware/ff549145) and issues an SRB\_FUNCTION\_CLAIM\_DEVICE command (see [**SCSI\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff565393)) to the device object returned, to prevent legacy class drivers from claiming the device. The class driver must send no other commands to the device during this phase of initialization.

If the class driver successfully claims the device, it creates a functional device object (FDO) and attaches it to the device stack by calling [**IoAttachDeviceToDeviceStack**](https://msdn.microsoft.com/library/windows/hardware/ff548300) with the input PDO. When *AddDevice* returns, the driver must be ready to handle a PnP start request (IRP\_MJ\_PNP with an [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749)). After the PnP manager has finished constructing the driver stack (which might include one or more filter drivers layered above and below the class driver) it issues a start request to the topmost driver in the driver stack for the target device.

If the class driver cannot successfully claim the device, it must not attempt to attach an FDO to the device stack, and should simply return a success status from its *AddDevice* routine. Such a driver will not receive a PnP start request for the device, although the PnP manager might call its *AddDevice* routine again for the same or a different device.

For more information about initializing storage class drivers, see the following:

[Storage Class Driver's DriverEntry Routine](storage-class-driver-s-driverentry-routine.md)

[Storage Class Driver's AddDevice Routine](storage-class-driver-s-adddevice-routine.md)

Also see [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125).

 

 




