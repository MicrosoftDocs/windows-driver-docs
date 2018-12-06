---
title: Software-First Installation
description: Software-First Installation
ms.assetid: 2199316d-17d5-463a-8c97-f89c87473f20
keywords:
- installation applications WDK , software-first installations
- device installation applications WDK , software-first installations
- distribution medium WDK device installations , software-first installations
- software-first installations WDK device installations
- AutoRun-enabled installation applications WDK
- device installations WDK , types
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Software-First Installation


A software-first installation involves the staging and preinstallation of your [driver package](driver-packages.md) on the system before the hardware device is plugged in. After the device is plugged in, the driver from the driver package is installed.

If the user inserts your distribution medium before plugging in the device, an AutoRun-enabled installation application can:

-   [Check for in-progress installations](checking-for-in-progress-installations.md), and stop executing if other installation activities are in progress.

-   [Determine whether a device is plugged in](determining-whether-a-device-is-plugged-in.md).

-   [Preinstall driver packages](preinstalling-driver-packages.md)

-   Use Microsoft Installer to [install device-specific applications](installing-device-specific-applications.md).

-   If the device is "hot-pluggable," tell the user to plug it in.

    If the bus does not provide hot-plug notification, initiate reenumeration by calling [**CM_Reenumerate_DevNode**](https://msdn.microsoft.com/library/windows/hardware/ff539763).

-   If the device is not hot-pluggable, tell the user to turn the system off, plug in the device, and turn the system back on.

 

 





