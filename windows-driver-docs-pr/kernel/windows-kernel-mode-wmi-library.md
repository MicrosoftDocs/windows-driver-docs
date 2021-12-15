---
title: Windows Kernel-Mode WMI Library
description: Windows Kernel-Mode WMI Library
ms.date: 10/17/2018
---

# Windows Kernel-Mode WMI Library


Windows provides a general mechanism for managing components. This system is called Windows Management Instrumentation (WMI). To satisify Windows Driver Model (WDM) requirements, you should implement WMI for your driver so that your driver can be managed by the system.

For more information on WMI, see [Windows Management Instrumentation](implementing-wmi.md).

Routines that provide a direct interface to the WMI library are prefixed with the letters "**Wmi**"; for a list of WMI routines, see [Windows Management Instrumentation (WMI) Library Routines](/windows-hardware/drivers/ddi/index).

For a list of WMI callbacks, see [WMI library callback routines](/windows-hardware/drivers/ddi/wmilib).

Communication with WMI is done with IRPs. For a list of routines that your driver can use to receive IRPs, see [WMI IRP Processing Routines](/windows-hardware/drivers/ddi/index). For a list of routines that your driver can use to send WMI IRPs, see [WMI IRP Sending Routines](/windows-hardware/drivers/ddi/index). For a list of IRPs that are used with WMI, see [WMI Minor IRPs](./wmi-minor-irps.md).

 

