---
title: Queuing I/O Requests While a Device Is Sleeping
description: Queuing I/O Requests While a Device Is Sleeping
ms.assetid: 8cc0cea0-e5be-4705-ad4d-13a44d536469
keywords: ["I/O WDK power management", "queuing I/O requests", "sleep power management WDK kernel", "asleep devices WDK power management", "queuing IRPs", "power IRPs WDK kernel , queuing I/O requests", "working state returns WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Queuing I/O Requests While a Device Is Sleeping





While a device is asleep, its drivers should queue any I/O requests directed to the device. The [**IoAllocateWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff548276), [**IoQueueWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff549466), and [**IoFreeWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff549133) support routines provide one way of queuing IRPs for delayed processing. For an example, see the queuing mechanism described for PnP drivers in [Holding Incoming IRPs When A Device Is Paused](holding-incoming-irps-when-a-device-is-paused.md).

A driver can access its device only when the device is in the Working (D0) state. A driver cannot touch any device registers when the device is in a sleep state; the device must first be returned to the Working state.

 

 




