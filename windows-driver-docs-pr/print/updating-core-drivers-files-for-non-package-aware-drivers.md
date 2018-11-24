---
title: Updating Core Drivers Files for Non-Package-Aware Drivers
description: Updating Core Drivers Files for Non-Package-Aware Drivers
ms.assetid: ce5da376-edac-4cd1-8750-9981bb5b709d
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Updating Core Drivers Files for Non-Package-Aware Drivers


Core driver components for Windows operating systems earlier than Windows Vista, including Windows Server 2003, Windows XP, and Windows 2000, are available on the Microsoft [Connect](http://go.microsoft.com/fwlink/p/?linkid=133880) Web site as separate packages for the XPSDrv, UniDrv, and PostScript drivers. Each package has a different redistribution agreement. The files in the packages are, in fact, identical to their counterparts in Windows Vista. To unpack the driver files, follow the steps listed in [Get the Updated Core Driver Package](getting-the-updated-core-driver-package.md). Once you have expanded the core driver package, include the core driver files you need in your own driver package as if they were part of your driver. In other words, copy the driver binary files from the core package to the main directory of your driver package. This will break the integrity of the digitally signed core driver package, but it will enable Windows XP (and the other Windows operating systems earlier than Windows Vista) and drivers that are not package aware to take advantage of the core driver updates.

Note that the unaltered core driver package can still be stored in a separate subdirectory in your driver package to enable package-aware installation in Windows Vista. That is, you can release one driver package for both Windows Vista and Windows XP. The INF file in the package should choose the appropriate source for the core driver files based on the operating system on which you are installing the package. For Windows Vista, your INF file should install the unaltered core driver package from a subdirectory in your driver package. For Windows XP, the INF file should install the redistributable core driver file from your package's main directory.

For Windows Vista, avoid breaking up the core driver package and do not reference the core driver files directly as part of your driver package. Otherwise, the package might appear to install correctly in Windows Vista, but the result might be print system instability and regressions in functionality. To avoid such problems, test your driver update package extensively to verify that it installs correctly on both Windows Vista and Windows XP.

For more information, see [Creating a Single Driver Package for Windows XP and Windows Vista](creating-a-single-driver-package-for-windows-xp-and-windows-vista.md).

 

 




