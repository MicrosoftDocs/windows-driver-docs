---
title: Unload Routine Functionality
description: Unload Routine Functionality
ms.assetid: a36b4687-df1d-498f-b9f3-d13ae2a9a3cd
keywords: ["Unload routines WDK kernel , functionality"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Unload Routine Functionality





The responsibilities of a driver's [*Unload*](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine depend on whether the driver supports PnP or not.

Just as the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routines of PnP drivers are usually simple, so are their *Unload* routines, as described in [A PnP Driver's Unload Routine](pnp-driver-s-unload-routine.md).

A non-PnP driver's *Unload* routine must free device objects and release driver-allocated resources. In short, it must undo the work performed by its corresponding **DriverEntry** and [*Reinitialize*](https://msdn.microsoft.com/library/windows/hardware/ff561022) routines in initializing the driver, its devices, and its resources. See [A Non-PnP Driver's Unload Routine](non-pnp-driver-s-unload-routine.md) for details.

 

 




