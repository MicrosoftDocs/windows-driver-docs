---
title: The Changer Class Driver
author: windows-driver-content
description: The Changer Class Driver
ms.assetid: c1c2330c-9cfc-432f-945c-630dc16aa54d
keywords: ["changer drivers WDK storage , class drivers", "storage changer drivers WDK , class drivers", "class drivers WDK storage , changer drivers"]
---

# The Changer Class Driver


## <span id="ddk_the_changer_class_driver_kg"></span><span id="DDK_THE_CHANGER_CLASS_DRIVER_KG"></span>


The changer class driver performs operating system-specific, device-independent services for a changer miniclass driver provided by the hardware vendor. For more information about the changer miniclass driver, see [Vendor-Supplied Changer Drivers](vendor-supplied-changer-drivers.md).

The changer class driver:

-   Provides memory allocation routines that a miniclass driver calls to allocate and free pool memory.

-   Provides an operating system-independent means of sending synchronous SRBs to the port driver in Microsoft Windows XP and later operating systems (see [Differences in Changer Class Driver Versions](differences-in-changer-class-driver-versions.md) for an explanation of the differences between Windows 2000 and Windows XP).

-   Helps initialize the class/miniclass driver pair.

-   Calls **Changer***Xxx* miniclass driver routines to determine the amount of space to allocate for device-specific information and to prepare the changer to receive other requests.

-   Performs device-independent preprocessing for [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) requests, calls the appropriate **Changer***Xxx* miniclass routines, and completes the requests.

-   Performs device-independent preprocessing for errors and calls the miniclass driver's [**ChangerError**](https://msdn.microsoft.com/library/windows/hardware/ff551418) routine for device-specific processing.

-   Calls **Changer***Xxx* miniclass driver routines to get product data, change element status, or query inquiry or volume tags data.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20The%20Changer%20Class%20Driver%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


