---
title: Driver Role in Power Management
author: windows-driver-content
description: Driver Role in Power Management
ms.assetid: 24b55880-e767-4f18-977e-c4a93332b909
keywords: ["power management WDK kernel , driver roles in", "system power states WDK kernel , driver roles", "device power states WDK kernel", "driver power support roles WDk kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Driver Role in Power Management


## <a href="" id="ddk-driver-role-in-power-management-kg"></a>


Drivers support power management in two ways:

1.  Drivers respond to system-wide power requests issued by the power manager.

2.  Drivers manage power and performance states for their individual devices.

Every driver must have a [*DispatchPower*](https://msdn.microsoft.com/library/windows/hardware/ff543354) routine to handle [**IRP\_MJ\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff550784) requests. The *DispatchPower* routine must inspect each power IRP and either handle it or pass it down to the next-lower driver.

For a device to participate in power management, every driver in the device stack for the device must respond to or pass power IRPs appropriately. Failure of a single driver to act correctly can cause power management to be disabled across the entire system.

One driver for each device [manages power policy](managing-device-power-policy.md) for its device. That driver can send power IRPs to its own device stack to perform power operations on its device. The power policy manager is responsible for issuing device power IRPs that correspond to system power IRPs.

In addition, drivers might perform certain power tasks, such as powering on a device at start-up or powering off a device at removal, without receiving a power IRP. These are considered implicit power requests.

For more information, see [Power Management Responsibilities for Drivers](power-management-responsibilities-for-drivers.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Driver%20Role%20in%20Power%20Management%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


