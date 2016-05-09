---
title: Handling PnP Start in a Storage Class Driver
author: windows-driver-content
description: Handling PnP Start in a Storage Class Driver
ms.assetid: 8d4ccd09-c5d2-4c9b-b94d-e22c916f0043
keywords: ["storage class drivers WDK , PnP", "class drivers WDK storage , PnP", "PnP WDK storage", "Plug and Play WDK storage"]
---

# Handling PnP Start in a Storage Class Driver


## <span id="ddk_handling_pnp_start_in_a_storage_class_driver_kg"></span><span id="DDK_HANDLING_PNP_START_IN_A_STORAGE_CLASS_DRIVER_KG"></span>


A storage class driver performs device-specific initialization when the PnP manager calls the class driver's [**DispatchPnP**](https://msdn.microsoft.com/library/windows/hardware/ff543341) routine with a start request (IRP\_MJ\_PNP with [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749)). The storage class driver's *DispatchPnP* routine either calls an internal *StartDevice* routine or implements the same functionality inline. Because start requests sent to an FDO must be handled first by the lowest driver in the stack, the storage class driver's *DispatchPnP* routine forwards the request to the next-lower driver with [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) before calling *StartDevice*. If the request was sent to a PDO, the driver need not forward the request before handling it.

A storage class driver's internal *StartDevice* routine sets up the device extension of its FDO with driver-determined data to manage I/O requests for the device. For more information, see [Setting Up a Storage Class Driver's Device Extension](setting-up-a-storage-class-driver-s-device-extension.md).

A *StartDevice* routine should enable any device interfaces that the driver registered in its *AddDevice* routine. (See [Device Interface Classes](https://msdn.microsoft.com/library/windows/hardware/ff541339).) It might also create a symbolic link for its device object.

After the start of the lower device has completed, the driver can assume that the device is in the D0 power state (fully on and operational) for most purposes. If the device is not completely powered up, the port driver will queue requests until the device is ready. However, if the driver's *StartDevice* routine needs to perform any operations that require inrush current -- for example, to spin up a disk drive -- the driver must send a D0 power request to the next-lower driver before performing the operation.

A driver of a device of type FILE\_DEVICE\_DISK or FILE\_DEVICE\_MASS\_STORAGE can register for idle detection and use the standard power policy time outs for the device class by specifying conservation and performance time-out values of -1 in its **PoRegisterDeviceforIdleDetection** call.

For more information about a storage class driver's *DispatchPnP* routine, see [Handling PnP Requests to Storage Peripherals](handling-pnp-requests-to-storage-peripherals.md). For more information about handling PnP start requests, see [Starting a Device](https://msdn.microsoft.com/library/windows/hardware/ff563849).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Handling%20PnP%20Start%20in%20a%20Storage%20Class%20Driver%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


