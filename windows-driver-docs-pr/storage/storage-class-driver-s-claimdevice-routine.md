---
title: Storage Class Driver's ClaimDevice Routine
description: Storage Class Driver's ClaimDevice Routine
ms.assetid: 175b9be6-34a5-4d20-970c-aa9a6880c242
keywords: ["ClaimDevice", "claiming storage devices", "query-property requests WDK storage", "configuration information WDk storage"]
---

# Storage Class Driver's ClaimDevice Routine


## <span id="ddk_storage_class_drivers_claimdevice_routine_kg"></span><span id="DDK_STORAGE_CLASS_DRIVERS_CLAIMDEVICE_ROUTINE_KG"></span>


The *ClaimDevice* routine, which claims a storage device, is typically called from a [Storage Class Driver's AddDevice Routine](storage-class-driver-s-adddevice-routine.md).

To claim a storage device, a class driver gets a reference to a device object by calling [**IoGetAttachedDeviceReference**](https://msdn.microsoft.com/library/windows/hardware/ff549145) with the PDO passed to the class driver in the *AddDevice* call, then either calls an internal *ClaimDevice* routine from its *AddDevice* routine or implements the same functionality inline. A *ClaimDevice* routine sets up an SRB with the **Function** value SRB\_FUNCTION\_CLAIM\_DEVICE and sends it to the device object returned by the class driver's call to **IoGetAttachedDeviceReference**.

The *ClaimDevice* routine allocates an IRP with [**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318), setting up the port driver's I/O stack location with the I/O control code IOCTL\_SCSI\_EXECUTE\_NONE and a pointer to the SRB at **Parameters.Scsi.Srb**. *ClaimDevice* also must set up an event object with **KeInitializeEvent** so it can wait for the completion of the IRP. Then, it sends the IRP on to the next-lower driver with [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336).

When the IRP completes, *ClaimDevice* should release the reference to the device object returned by **IoGetAttachedDeviceReference**.

A *ClaimDevice* routine can serve double duty as a routine to be called from a class driver's *RemoveDevice* routine, or from *AddDevice* if the driver succeeds in claiming the device but cannot create a device object. In such cases, *ClaimDevice* sends an SRB with the **Function** value SRB\_FUNCTION\_RELEASE\_DEVICE.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Storage%20Class%20Driver's%20ClaimDevice%20Routine%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




