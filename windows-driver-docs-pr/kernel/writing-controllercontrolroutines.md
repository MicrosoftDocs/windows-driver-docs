---
title: Writing ControllerControl Routines
description: Drivers that use a controller object must supply a ControllerControl routine to initiate I/O operations.
keywords: ["controller objects WDK kernel , writing ControllerControl routines", "ControllerControl routines, writing"]
ms.date: 07/22/2021
ms.localizationpriority: medium
---

# Writing ControllerControl Routines

Drivers that use a controller object must supply a [*ControllerControl*](controllercontrol-routine-requirements.md) routine to initiate I/O operations.

A lowest-level device driver that must synchronize operations through a physical controller, such as an "AT" disk controller, to similar devices can have a *ControllerControl* routine.

When a driver calls [**IoAllocateController**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ioallocatecontroller), its *ControllerControl* routine is run immediately if the hardware represented by the controller object is available for an I/O operation. Otherwise, the *ControllerControl* routine is queued until the controller is free.

> [!NOTE]
> WDM drivers cannot use controller objects and *ControllerControl* routines.
