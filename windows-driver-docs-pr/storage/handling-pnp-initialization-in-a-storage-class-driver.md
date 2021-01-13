---
title: Handling PnP Initialization in a Storage Class Driver
description: Handling PnP Initialization in a Storage Class Driver
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

Storage class driver initialization begins when the PnP manager calls the driver's [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine to load and initialize the driver. Then the PnP manager calls the storage class driver's [**AddDevice**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routine, passing a pointer to a physical device object (PDO) that represents the target device.

In its *AddDevice* routine, the class driver calls [**IoGetAttachedDeviceReference**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iogetattacheddevicereference) and issues an SRB\_FUNCTION\_CLAIM\_DEVICE command (see [**SCSI\_REQUEST\_BLOCK**](/windows-hardware/drivers/ddi/srb/ns-srb-_scsi_request_block)) to the device object returned, to prevent legacy class drivers from claiming the device. The class driver must send no other commands to the device during this phase of initialization.

If the class driver successfully claims the device, it creates a functional device object (FDO) and attaches it to the device stack by calling [**IoAttachDeviceToDeviceStack**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioattachdevicetodevicestack) with the input PDO. When *AddDevice* returns, the driver must be ready to handle a PnP start request (IRP\_MJ\_PNP with an [**IRP\_MN\_START\_DEVICE**](../kernel/irp-mn-start-device.md)). After the PnP manager has finished constructing the driver stack (which might include one or more filter drivers layered above and below the class driver) it issues a start request to the topmost driver in the driver stack for the target device.

If the class driver cannot successfully claim the device, it must not attempt to attach an FDO to the device stack, and should simply return a success status from its *AddDevice* routine. Such a driver will not receive a PnP start request for the device, although the PnP manager might call its *AddDevice* routine again for the same or a different device.

For more information about initializing storage class drivers, see the following:

[Storage Class Driver's DriverEntry Routine](storage-class-driver-s-driverentry-routine.md)

[Storage Class Driver's AddDevice Routine](storage-class-driver-s-adddevice-routine.md)

Also see [Plug and Play](../kernel/introduction-to-plug-and-play.md).

