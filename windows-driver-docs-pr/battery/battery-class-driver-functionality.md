---
title: Battery Class Driver Functionality
description: Battery Class Driver Functionality
ms.assetid: cd7536d9-bcf1-4674-8ebf-af2b888a0f0a
keywords: ["battery class drivers WDK , functionality"]
---

# Battery Class Driver Functionality


## <span id="ddk_battery_class_driver_functionality_dg"></span><span id="DDK_BATTERY_CLASS_DRIVER_FUNCTIONALITY_DG"></span>


The kernel-mode battery class driver, battc.sys, provides device-independent battery support and exports support routines for use by all device-specific battery miniclass drivers.

The battery class driver takes care of the following tasks for miniclass drivers:

-   Performing a large part of miniclass driver initialization, including allocating system resources and space for the miniclass driver's class data

-   Handling device control IRPs ([**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744)) that specify battery class IOCTLs. (See the Microsoft Windows SDK for information about these IOCTLs.)

-   Serializing requests to the battery device

-   Administering DC power policy for the operating system

-   Freeing system resources if the miniclass driver is unloaded

-   Handling certain standard battery WMI classes

See [Battery Miniclass Driver Routines](https://msdn.microsoft.com/library/windows/hardware/ff536286) for descriptions of the routines that the battery class driver exports to battery miniclass drivers.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[battery\battery]:%20Battery%20Class%20Driver%20Functionality%20%20RELEASE:%20%286/7/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




