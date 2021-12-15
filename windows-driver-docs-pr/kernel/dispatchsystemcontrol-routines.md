---
title: DispatchSystemControl Routines
description: DispatchSystemControl Routines
keywords: ["dispatch routines WDK kernel , DispatchSystemControl routine", "system control dispatch routines WDK kernel", "IRP_MJ_SYSTEM_CONTROL I/O function code", "DispatchSystemControl routine"]
ms.date: 06/16/2017
---

# DispatchSystemControl Routines





A driver's [*DispatchSystemControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine handles IRPs for the [**IRP\_MJ\_SYSTEM\_CONTROL**](./irp-mj-system-control.md) I/O function code.

All drivers must provide a *DispatchSystemControl* routine. The purpose of this routine is to provide support for Windows Management Instrumentation (WMI). Regardless of whether a driver supports WMI, this routine must pass the IRP to the next-lower driver.

To learn how to implement a *DispatchSystemControl* routine, and how to support WMI in general, see [Windows Management Instrumentation](implementing-wmi.md).

 

