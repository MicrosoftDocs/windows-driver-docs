---
title: Windows Kernel-Mode Plug and Play Manager
description: Windows Kernel-Mode Plug and Play Manager
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Windows Kernel-Mode Plug and Play Manager


Plug and Play (PnP) is a combination of hardware technology and software techniques that enables a PC to recognize when a device is added to the system. With PnP, the system configuration can change with little or no input from the user. For example, when a USB thumb drive is plugged in, Windows can detect the thumb drive and add it to the file system automatically. However, to do this, the hardware must follow certain requirements and so must the driver.

For more information about PnP for drivers, see [Plug and Play](introduction-to-plug-and-play.md).

The PnP manager is actually a subsystem of the I/O manager. For more information about the I/O manager, see [Windows Kernel-Mode I/O Manager](windows-kernel-mode-i-o-manager.md).

For lists of PnP routines, see [Plug and Play Routines](/windows-hardware/drivers/ddi/_kernel/#plug-and-play-routines).

Note that there are no routines that provide a direct interface to the PnP manager; that is, there are no "**Pp**" routines.

The Windows Driver Frameworks (WDF) provide a set of libraries to make PnP management much easier. For more information about WDF, see [Kernel-Mode Driver Framework Overview](../wdf/index.md).

 

