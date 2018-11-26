---
title: Storage Class Driver's ClaimDevice Routine
description: Storage Class Driver's ClaimDevice Routine
ms.assetid: 175b9be6-34a5-4d20-970c-aa9a6880c242
keywords:
- ClaimDevice
- claiming storage devices
- query-property requests WDK storage
- configuration information WDk storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storage Class Driver's ClaimDevice Routine


## <span id="ddk_storage_class_drivers_claimdevice_routine_kg"></span><span id="DDK_STORAGE_CLASS_DRIVERS_CLAIMDEVICE_ROUTINE_KG"></span>


The *ClaimDevice* routine, which claims a storage device, is typically called from a [Storage Class Driver's AddDevice Routine](storage-class-driver-s-adddevice-routine.md).

To claim a storage device, a class driver gets a reference to a device object by calling [**IoGetAttachedDeviceReference**](https://msdn.microsoft.com/library/windows/hardware/ff549145) with the PDO passed to the class driver in the *AddDevice* call, then either calls an internal *ClaimDevice* routine from its *AddDevice* routine or implements the same functionality inline. A *ClaimDevice* routine sets up an SRB with the **Function** value SRB\_FUNCTION\_CLAIM\_DEVICE and sends it to the device object returned by the class driver's call to **IoGetAttachedDeviceReference**.

The *ClaimDevice* routine allocates an IRP with [**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318), setting up the port driver's I/O stack location with the I/O control code IOCTL\_SCSI\_EXECUTE\_NONE and a pointer to the SRB at **Parameters.Scsi.Srb**. *ClaimDevice* also must set up an event object with **KeInitializeEvent** so it can wait for the completion of the IRP. Then, it sends the IRP on to the next-lower driver with [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336).

When the IRP completes, *ClaimDevice* should release the reference to the device object returned by **IoGetAttachedDeviceReference**.

A *ClaimDevice* routine can serve double duty as a routine to be called from a class driver's *RemoveDevice* routine, or from *AddDevice* if the driver succeeds in claiming the device but cannot create a device object. In such cases, *ClaimDevice* sends an SRB with the **Function** value SRB\_FUNCTION\_RELEASE\_DEVICE.

 

 




