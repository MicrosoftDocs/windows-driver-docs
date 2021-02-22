---
title: Redistributable Framework Components
description: This topic describes the Microsoft-supplied redistributable framework updates that are included as part of the Windows Driver Kit (WDK) for Windows 8.1, and how to determine which ones to add to your driver package.
keywords:
- framework-based drivers WDK KMDF , installing
- INF files WDK KMDF , about installing KMDF drivers
- installation components for drivers WDK KMDF
ms.date: 05/16/2019
ms.localizationpriority: medium
---

# Redistributable Framework Components

This topic describes the Microsoft-supplied redistributable framework updates that are included as part of the Windows Driver Kit (WDK), and how to determine which ones to add to your driver package.

The redistributable framework updates make it possible to run a driver built with a later framework version than the one included in an operating system. For example, KMDF 1.11 is included in Windows 8. But you can run a KMDF 1.11 driver on Windows Vista or Windows 7. Before you can do so, however, you must ensure that the KMDF 1.11 framework library replaces the framework library included in the earlier operating system (in this case, KMDF 1.7 and KMDF 1.9 respectively). You do this by redistributing a Microsoft-supplied co-installer or .msu file with your driver package.

## When do I need to include a co-installer or .msu in my driver package?

First, decide which versions of Windows your driver will support.  Based on that, determine [which framework version to use](building-and-loading-a-kmdf-driver.md#which-framework-version-should-i-use).

If the chosen WDF version is more recent than the version that shipped with the target OS, include the co-installer or .msu file in your driver package.

For example, you want your driver to run on Windows 7.  You can choose to build your driver using either WDF 1.11 or WDF 1.9. If you choose 1.9, which is provided with Windows 7, there is no need to update the system. On the other hand, if you choose 1.11, you would need to include a WDF 1.11 update package with your driver.

## Should I include the co-installer or the .msu file?

If your driver installation is triggered by plugging in a new hardware device to a system and you are installing only the driver, include the co-installer in your driver package. Then reference the co-installer in your INF file, as described in [Specifying the KMDF Co-installer in an INF File](installing-the-framework-s-co-installer.md).

If you need to install an application in addition to your driver, you should instead redistribute the relevant MSU package (for example kmdf-1.11-Win.6.0.msu) along with a setup application that calls it.
In this case, no INF entries are needed.

You never need both the co-installer and the .msu file.


## Where can I find these files, and what's included?

The co-installers are located in `%program files%\Windows Kits\<version>\redist\wdf`.

This directory contains the following files, for x86 and x64:

-   *WdfCoinstaller01007.dll*, *WdfCoinstaller01009.dll*, *WdfCoinstaller01011.dll* (co-installers for KMDF 1.7/1.9/1.11).
-   *WUDFUpdate\_01007.dll*, *WUDFUpdate\_01009.dll*, *WUDFUpdate\_01011.dll* (co-installers for UMDF).
-   *winusbcoinstaller.dll*, *winusbcoinstaller2.dll* (co-installers for WinUSB 1.5/1.9).

If you would like the MSU file, please download and install the package (in MSI format) from [WDK 8 redistributable components](https://go.microsoft.com/fwlink/p/?LinkID=253170).
After installation, the MSU and co-installers can be found in `%program files%\Windows Kits\8.0\redist\wdf`.

## Co-installer Naming and Versioning

The co-installer is named **WdfCoInstaller**<em>MMmmm</em>**.dll**.

-   *MM* is the major version number.
-   *mmm* is the minor version number.

For example, the filename for version 1.0 of the co-installer is *WdfCoInstaller01000.dll*, and the filename for version 1.11 is *WdfCoInstaller01011.dll*.

The version of the co-installer that you include with your driver package must match the version of the framework library that you use to develop your driver.

Note that the framework library's file name includes only the major version number. For more information about library file names, see [Framework Library Versioning](framework-library-versioning.md).
