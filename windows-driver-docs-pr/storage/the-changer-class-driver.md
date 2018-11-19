---
title: The Changer Class Driver
description: The Changer Class Driver
ms.assetid: c1c2330c-9cfc-432f-945c-630dc16aa54d
keywords:
- changer drivers WDK storage , class drivers
- storage changer drivers WDK , class drivers
- class drivers WDK storage , changer drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




