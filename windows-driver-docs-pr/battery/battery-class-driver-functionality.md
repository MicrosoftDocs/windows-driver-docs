---
title: Battery Class Driver Functionality
description: Battery Class Driver Functionality
ms.assetid: cd7536d9-bcf1-4674-8ebf-af2b888a0f0a
keywords:
- battery class drivers WDK , functionality
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




