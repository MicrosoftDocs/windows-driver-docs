---
title: Supporting PnP and Power Management in Software-only Drivers
description: Supporting PnP and Power Management in Software-only Drivers
ms.assetid: bcfca8b2-68d6-4875-8687-27351becd6f4
keywords:
- PnP WDK KMDF , software-only drivers
- Plug and Play WDK KMDF , software-only drivers
- power management WDK KMDF , software-only drivers
- software-only drivers WDK KMDF
- filter drivers WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting PnP and Power Management in Software-only Drivers


*Software-only drivers* are drivers that do not access any hardware. Some software-only drivers reside in a driver stack that does not access hardware. Because these drivers do not access hardware, they typically do not have to perform any PnP or power management operations.

Other software-only drivers are filter drivers: they reside in a stack of drivers that do access hardware, but the filter drivers do not access hardware. When a filter driver receives an I/O request that specifies a PnP or power management operation, the driver typically just passes the request to the next driver. The framework intercepts these requests and passes them on, so framework-based drivers never see the requests.

If you are writing a software-only driver, your driver [creates device objects](creating-a-framework-device-object.md) but you typically do not need to provide any event callback functions to handle PnP or power management events. If the driver uses [framework queue objects](framework-queue-objects.md), you will need to set the **PowerManaged** member of the queue's [**WDF\_IO\_QUEUE\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552359) structure to **WdfFalse** or **WdfUseDefault**.

A few software-only drivers are also [function drivers](supporting-pnp-and-power-management-in-function-drivers.md). In other words, a single driver might act as a software-only driver to support a virtual device that does not access hardware, and as a function driver to support a hardware device.

 

 





