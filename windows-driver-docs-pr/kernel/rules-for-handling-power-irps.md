---
title: Rules for Handling Power IRPs
description: Rules for Handling Power IRPs
ms.assetid: ea4a1c57-6184-4160-bf23-b86e3e403388
keywords: ["power management WDK kernel , IRPs", "IRPs WDK power management", "power IRPs WDK kernel", "power IRPs WDK kernel , rules", "I/O request packets WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Rules for Handling Power IRPs





Drivers that support power management must conform to certain rules pertaining to:

* [Calling IoCallDriver versus calling PoCallDriver](calling-iocalldriver-versus-calling-pocalldriver.md) to pass power IRPs

* [Calling PoStartNextPowerIrp](calling-postartnextpowerirp.md) to start the next power IRP

* [Passing power IRPs](passing-power-irps.md) down to the next-lower driver

* [Queuing I/O requests while a device is sleeping](queuing-i-o-requests-while-a-device-is-sleeping.md)

* [Handling unsupported or unrecognized power IRPs](handling-unsupported-or-unrecognized-power-irps.md)

* [Calling ExSetTimerResolution while processing a power IRP](calling-exsettimerresolution-while-processing-a-power-irp.md)

The sections that follow describe how drivers should perform these tasks.

For a list of power management IRPs, see [Power Management Minor IRPs](power-management-minor-irps.md).

 




