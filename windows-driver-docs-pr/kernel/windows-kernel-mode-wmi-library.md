---
title: Windows Kernel-Mode WMI Library
description: Windows Kernel-Mode WMI Library
ms.assetid: ca981f38-8f3b-48cc-969f-ce53b85bba20
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Windows Kernel-Mode WMI Library


Windows provides a general mechanism for managing components. This system is called Windows Management Instrumentation (WMI). To satisify Windows Driver Model (WDM) requirements, you should implement WMI for your driver so that your driver can be managed by the system.

For more information on WMI, see [Windows Management Instrumentation](implementing-wmi.md).

Routines that provide a direct interface to the WMI library are prefixed with the letters "**Wmi**"; for a list of WMI routines, see [Windows Management Instrumentation (WMI) Library Routines](https://msdn.microsoft.com/library/windows/hardware/ff566359).

For a list of WMI callbacks, see [WMI Library Callback Routines](https://msdn.microsoft.com/library/windows/hardware/ff566357).

Communication with WMI is done with IRPs. For a list of routines that your driver can use to receive IRPs, see [WMI IRP Processing Routines](https://msdn.microsoft.com/library/windows/hardware/ff566353). For a list of routines that your driver can use to send WMI IRPs, see [WMI IRP Sending Routines](https://msdn.microsoft.com/library/windows/hardware/ff566355). For a list of IRPs that are used with WMI, see [WMI Minor IRPs](https://msdn.microsoft.com/library/windows/hardware/ff566361).

 

 




