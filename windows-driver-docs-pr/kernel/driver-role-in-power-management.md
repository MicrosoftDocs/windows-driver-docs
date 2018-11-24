---
title: Driver Role in Power Management
description: Driver Role in Power Management
ms.assetid: 24b55880-e767-4f18-977e-c4a93332b909
keywords: ["power management WDK kernel , driver roles in", "system power states WDK kernel , driver roles", "device power states WDK kernel", "driver power support roles WDk kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Driver Role in Power Management





Drivers support power management in two ways:

1.  Drivers respond to system-wide power requests issued by the power manager.

2.  Drivers manage power and performance states for their individual devices.

Every driver must have a [*DispatchPower*](https://msdn.microsoft.com/library/windows/hardware/ff543354) routine to handle [**IRP\_MJ\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff550784) requests. The *DispatchPower* routine must inspect each power IRP and either handle it or pass it down to the next-lower driver.

For a device to participate in power management, every driver in the device stack for the device must respond to or pass power IRPs appropriately. Failure of a single driver to act correctly can cause power management to be disabled across the entire system.

One driver for each device [manages power policy](managing-device-power-policy.md) for its device. That driver can send power IRPs to its own device stack to perform power operations on its device. The power policy manager is responsible for issuing device power IRPs that correspond to system power IRPs.

In addition, drivers might perform certain power tasks, such as powering on a device at start-up or powering off a device at removal, without receiving a power IRP. These are considered implicit power requests.

For more information, see [Power Management Responsibilities for Drivers](power-management-responsibilities-for-drivers.md).

 

 




