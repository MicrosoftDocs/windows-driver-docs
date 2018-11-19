---
title: DispatchSystemControl Routines
description: DispatchSystemControl Routines
ms.assetid: b885a4a3-a9b6-423c-83bb-ee502724b0d0
keywords: ["dispatch routines WDK kernel , DispatchSystemControl routine", "system control dispatch routines WDK kernel", "IRP_MJ_SYSTEM_CONTROL I/O function code", "DispatchSystemControl routine"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# DispatchSystemControl Routines





A driver's [*DispatchSystemControl*](https://msdn.microsoft.com/library/windows/hardware/ff543412) routine handles IRPs for the [**IRP\_MJ\_SYSTEM\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550813) I/O function code.

All drivers must provide a *DispatchSystemControl* routine. The purpose of this routine is to provide support for Windows Management Instrumentation (WMI). Regardless of whether a driver supports WMI, this routine must pass the IRP to the next-lower driver.

To learn how to implement a *DispatchSystemControl* routine, and how to support WMI in general, see [Windows Management Instrumentation](implementing-wmi.md).

 

 




