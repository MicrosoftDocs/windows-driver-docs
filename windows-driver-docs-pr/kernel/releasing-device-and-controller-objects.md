---
title: Releasing Device and Controller Objects
author: windows-driver-content
description: Releasing Device and Controller Objects
ms.assetid: 35404401-d3a8-4257-b1a3-b16ebe42b181
keywords: ["Unload routines WDK kernel , non-PnP drivers", "non-PnP Unload routine WDK kernel", "releasing devices", "releasing controller objects", "device releases WDK kernel", "controller objects WDK kernel , releasing"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Releasing Device and Controller Objects


## <a href="" id="ddk-releasing-device-and-controller-objects-kg"></a>


Before a driver deletes a device or controller object, it must release its references to external resources, such as pointers to other drivers' objects and/or to interrupt objects, that it stored in the corresponding device or controller extension. It can then call [**IoDeleteDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549083) for each device object that the driver created. A non-WDM driver that previously called [**IoCreateController**](https://msdn.microsoft.com/library/windows/hardware/ff548395) must also call [**IoDeleteController**](https://msdn.microsoft.com/library/windows/hardware/ff549078).

Any Kernel-defined object for which the driver provides storage in a device extension is automatically freed when the [*Unload*](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine calls **IoDeleteDevice** with the corresponding device object. In general, any object that the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) or [*Reinitialize*](https://msdn.microsoft.com/library/windows/hardware/ff561022) routine set up by calling **KeInitialize*Xxx*** can be freed by a call to **IoDeleteDevice** if the driver provided storage for that object in its device extension. For example, if a driver has a [*CustomTimerDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542983) routine and has provided storage for the necessary DPC and timer objects in its device extension, the call to **IoDeleteDevice** releases these system resources.

Similarly, any Kernel-defined object for which the driver provides storage in a controller extension is automatically freed when the *Unload* routine calls **IoDeleteController** with the corresponding controller object.

If the **DriverEntry** or *Reinitialize* routine called [**IoGetConfigurationInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549157) to increment the count for a particular type of device, the *Unload* routine also must call **IoGetConfigurationInformation** and decrement the count for its devices in the I/O manager's global configuration information structure as it deletes the corresponding device objects.

Before it returns control, an *Unload* routine also is responsible for freeing any other driver-allocated resources that have not yet been freed by other driver routines.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Releasing%20Device%20and%20Controller%20Objects%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


