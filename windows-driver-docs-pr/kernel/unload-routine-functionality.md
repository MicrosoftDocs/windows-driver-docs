---
title: Unload Routine Functionality
description: Unload Routine Functionality
ms.assetid: a36b4687-df1d-498f-b9f3-d13ae2a9a3cd
keywords: ["Unload routines WDK kernel , functionality"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Unload Routine Functionality





The responsibilities of a driver's [*Unload*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload) routine depend on whether the driver supports PnP or not.

Just as the [**DriverEntry**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routines of PnP drivers are usually simple, so are their *Unload* routines, as described in [A PnP Driver's Unload Routine](pnp-driver-s-unload-routine.md).

A non-PnP driver's *Unload* routine must free device objects and release driver-allocated resources. In short, it must undo the work performed by its corresponding **DriverEntry** and [*Reinitialize*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/nc-ntddk-driver_reinitialize) routines in initializing the driver, its devices, and its resources. See [A Non-PnP Driver's Unload Routine](non-pnp-driver-s-unload-routine.md) for details.

 

 




