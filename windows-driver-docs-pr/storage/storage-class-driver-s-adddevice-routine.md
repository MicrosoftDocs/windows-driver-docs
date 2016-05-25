---
title: Storage Class Driver's AddDevice Routine
author: windows-driver-content
description: Storage Class Driver's AddDevice Routine
ms.assetid: ff07ae84-2748-44b4-88c6-e67f1d4c9268
keywords: ["AddDevice routine WDK storage"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Storage%20Class%20Driver's%20AddDevice%20Routine%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


