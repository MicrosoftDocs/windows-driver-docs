---
title: DispatchShutdown Routines
description: DispatchShutdown Routines
keywords: ["IRP_MJ_SHUTDOWN I/O function code", "dispatch routines WDK kernel , DispatchShutdown routine", "DispatchShutdown routine", "shutdown dispatch routines WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# DispatchShutdown Routines





A driver's [*DispatchShutdown*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine handles IRPs for the [**IRP\_MJ\_SHUTDOWN**](./irp-mj-shutdown.md) I/O function code. Drivers of mass-storage devices that have internal caches for data must handle this request. Drivers of mass-storage devices and intermediate drivers layered over them also must handle this request if an underlying driver maintains internal buffers for data.

 

