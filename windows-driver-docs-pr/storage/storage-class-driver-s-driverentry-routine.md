---
title: Storage Class Driver's DriverEntry Routine
author: windows-driver-content
description: Storage Class Driver's DriverEntry Routine
ms.assetid: 45e929ff-b4e2-4855-8498-15ec4c30f497
keywords: ["DriverEntry WDK storage"]
---

# Storage Class Driver's DriverEntry Routine


## <span id="ddk_storage_class_drivers_driverentry_routine_kg"></span><span id="DDK_STORAGE_CLASS_DRIVERS_DRIVERENTRY_ROUTINE_KG"></span>


Like any other Windows NT kernel-mode higher-level driver, the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine of a storage class driver must do the following:

1.  Allocate a driver object extension of appropriate size by calling [**IoAllocateDriverObjectExtension**](https://msdn.microsoft.com/library/windows/hardware/ff548233).

2.  Copy the input registry path into the driver extension for later use (if necessary) and initialize the driver extension.

3.  Define its dispatch entry points in the input driver object.

For more information about a PnP driver's **DriverEntry** routine, see [Writing a DriverEntry Routine](https://msdn.microsoft.com/library/windows/hardware/ff566402).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Storage%20Class%20Driver's%20DriverEntry%20Routine%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


