---
title: Overview of Windows Components
description: Overview of Windows Components
keywords: ["Windows components WDK", "Windows NT components WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: High
---

# Overview of Windows Components





The following figure shows the major internal components of the Windows operating system.

![diagram illustrating an overview of windows components.](images/ntarch.png)

As the figure shows, the Windows operating system includes both user-mode and kernel-mode components. For more information about Windows user and kernel modes, see [User Mode and Kernel Mode](../gettingstarted/user-mode-and-kernel-mode.md).

Drivers call routines that are exported by various kernel components. For example, to create a device object, you would call the [**IoCreateDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatedevice) routine which is exported by the I/O manager. For a list of kernel-mode routines that drivers can call, see driver support routines.

In addition, drivers must respond to specific calls from the operating system and can respond to other system calls. For a list of kernel mode routines that drivers may need to support, see [Standard Driver Routines](./introduction-to-standard-driver-routines.md).

Not all kernel-mode components are pictured in the figure above. For a list of kernel mode components, see [Kernel-Mode Managers and Libraries](windows-kernel-mode-object-manager.md).

 

