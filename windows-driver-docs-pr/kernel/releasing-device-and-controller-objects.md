---
title: Releasing Device and Controller Objects
description: Releasing Device and Controller Objects
ms.assetid: 35404401-d3a8-4257-b1a3-b16ebe42b181
keywords: ["Unload routines WDK kernel , non-PnP drivers", "non-PnP Unload routine WDK kernel", "releasing devices", "releasing controller objects", "device releases WDK kernel", "controller objects WDK kernel , releasing"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Releasing Device and Controller Objects





Before a driver deletes a device or controller object, it must release its references to external resources, such as pointers to other drivers' objects and/or to interrupt objects, that it stored in the corresponding device or controller extension. It can then call [**IoDeleteDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549083) for each device object that the driver created. A non-WDM driver that previously called [**IoCreateController**](https://msdn.microsoft.com/library/windows/hardware/ff548395) must also call [**IoDeleteController**](https://msdn.microsoft.com/library/windows/hardware/ff549078).

Any Kernel-defined object for which the driver provides storage in a device extension is automatically freed when the [*Unload*](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine calls **IoDeleteDevice** with the corresponding device object. In general, any object that the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) or [*Reinitialize*](https://msdn.microsoft.com/library/windows/hardware/ff561022) routine set up by calling **KeInitialize*Xxx*** can be freed by a call to **IoDeleteDevice** if the driver provided storage for that object in its device extension. For example, if a driver has a [*CustomTimerDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542983) routine and has provided storage for the necessary DPC and timer objects in its device extension, the call to **IoDeleteDevice** releases these system resources.

Similarly, any Kernel-defined object for which the driver provides storage in a controller extension is automatically freed when the *Unload* routine calls **IoDeleteController** with the corresponding controller object.

If the **DriverEntry** or *Reinitialize* routine called [**IoGetConfigurationInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549157) to increment the count for a particular type of device, the *Unload* routine also must call **IoGetConfigurationInformation** and decrement the count for its devices in the I/O manager's global configuration information structure as it deletes the corresponding device objects.

Before it returns control, an *Unload* routine also is responsible for freeing any other driver-allocated resources that have not yet been freed by other driver routines.

 

 




