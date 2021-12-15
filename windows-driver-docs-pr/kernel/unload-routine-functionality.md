---
title: Unload Routine Functionality
description: Unload Routine Functionality
keywords: ["Unload routines WDK kernel , functionality"]
ms.date: 06/16/2017
---

# Unload Routine Functionality





The responsibilities of a driver's [*Unload*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload) routine depend on whether the driver supports PnP or not.

Just as the [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routines of PnP drivers are usually simple, so are their *Unload* routines, as described in [A PnP Driver's Unload Routine](pnp-driver-s-unload-routine.md).

A non-PnP driver's *Unload* routine must free device objects and release driver-allocated resources. In short, it must undo the work performed by its corresponding **DriverEntry** and [*Reinitialize*](/windows-hardware/drivers/ddi/ntddk/nc-ntddk-driver_reinitialize) routines in initializing the driver, its devices, and its resources. See [A Non-PnP Driver's Unload Routine](non-pnp-driver-s-unload-routine.md) for details.

 

