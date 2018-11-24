---
title: Using Kernel-Mode Driver Framework with Non-PnP Drivers
description: Using Kernel-Mode Driver Framework with Non-PnP Drivers
ms.assetid: b4b6add2-0e27-4af7-b6bf-5e47db7db560
keywords:
- non-PnP drivers WDK KMDF
- kernel-mode drivers WDK KMDF , PnP
- KMDF WDK , PnP
- Kernel-Mode Driver Framework WDK , PnP
- Plug and Play WDK KMDF , non-PnP drivers
- PnP WDK KMDF , non-PnP drivers
- framework-based drivers WDK KMDF , PnP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Kernel-Mode Driver Framework with Non-PnP Drivers





If you are writing a driver for a device that does not support Plug and Play (PnP), the driver must:

-   Set the [**WdfDriverInitNonPnpDriver**](https://msdn.microsoft.com/library/windows/hardware/ff551303) flag in the [**WDF\_DRIVER\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551300) structure's **DriverInitFlags** member.

-   Provide an [*EvtDriverUnload*](https://msdn.microsoft.com/library/windows/hardware/ff541694) event callback function.

-   Create framework device objects that only represent [control device objects](using-control-device-objects.md).

If your device does not support PnP, your driver does *not* provide an [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function. Instead, the driver must determine if its device is present.

 

 





