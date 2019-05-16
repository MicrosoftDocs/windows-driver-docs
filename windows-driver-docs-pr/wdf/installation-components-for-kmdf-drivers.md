---
title: Redistributable Framework Components
description: This topic describes the Microsoft-supplied redistributable framework updates that are included as part of the Windows Driver Kit (WDK) for Windows 8.1, and how to determine which ones to add to your driver package.
ms.assetid: 63fbe66e-fa1b-4a70-a8ea-df4f3df9bad4
keywords:
- framework-based drivers WDK KMDF , installing
- INF files WDK KMDF , about installing KMDF drivers
- installation components for drivers WDK KMDF
ms.date: 05/16/2019
ms.localizationpriority: medium
---

# Redistributable Framework Components

This topic describes the Microsoft-supplied redistributable framework updates that are included as part of the Windows Driver Kit (WDK), and how to determine which ones to add to your driver package.

## When do I need to include a co-installer or .msu in my driver package?

* If your driver must work on Windows XP and later versions of Windows, use KMDF or UMDF version 1.9, and include Microsoft-supplied framework updates in your driver package.

* If your driver must work on Windows Vista and later versions of Windows, use KMDF or UMDF version 1.11, and include Microsoft-supplied framework updates in your driver package.

* If your driver must work on Windows 8.1 and later versions of Windows, you do not need to include a co-installer, custom installer, or reference in the INF file.

The framework updates make it possible to run a driver built with a later framework version than the one included in an operating system. For example, KMDF 1.11 is included in Windows 8. But you can run a KMDF 1.11 driver on Windows Vista or Windows 7. Before you can do so, however, you must ensure that the KMDF 1.11 framework library replaces the framework library included in the earlier operating system (in this case, KMDF 1.7 and KMDF 1.9 respectively). You do this by redistributing a Microsoft-supplied co-installer or .msu file with your driver package.

## Should I include the co-installer or the .msu file?

If your driver installation is triggered by plugging in a new hardware device to a system and you are installing only the driver, include the co-installer in your driver package. Then reference the co-installer in your INF file, as described in [Specifying the KMDF Co-installer in an INF File](installing-the-framework-s-co-installer.md).

If you need to install an application in addition to your driver, you should instead redistribute the relevant MSU package (for example kmdf-1.11-Win.6.0.msu) along with a setup application that calls it.
In this case, no INF entries are needed.

You never need both the co-installer and the .msu file.


## Where can I find these files, and what's included?

The full set of redistributable framework update files is located in `%program files%\Windows Kits\8.0\redist\wdf`.

This directory contains the following files, for x86 and x64:

-   *WdfCoinstaller01007.dll*, *WdfCoinstaller01009.dll*, *WdfCoinstaller01011.dll* (co-installers for KMDF 1.7/1.9/1.11).
-   *WUDFUpdate\_01007.dll*, *WUDFUpdate\_01009.dll*, *WUDFUpdate\_01011.dll* (co-installers for UMDF).
-   *winusbcoinstaller.dll*, *winusbcoinstaller2.dll* (co-installers for WinUSB 1.5/1.9).

When you install the WDK for Windows 8 (KMDF/UMDF 1.11), the installer offers an option to **Download WDF co-installers**.  Select this option and the installer opens the browser to download an MSI package that installs co-installer DLL and MSU files under `%program files%\Windows Kits\8.0\redist\wdf`.

If you install the WDK for Windows 8.1 or later, the installer automatically places the co-installer DLLs in `%program files%\Windows Kits\8.0\redist\wdf`.
You must download the MSU file separately from [WDK 8 redistributable components](https://go.microsoft.com/fwlink/p/?LinkID=253170).

## Co-installer Naming and Versioning

The co-installer is named **WdfCoInstaller**<em>MMmmm</em>**.dll**.

-   *MM* is the major version number.
-   *mmm* is the minor version number.

For example, the filename for version 1.0 of the co-installer is *WdfCoInstaller01000.dll*, and the filename for version 1.11 is *WdfCoInstaller01011.dll*.

The version of the co-installer that you include with your driver package must match the version of the framework library that you use to develop your driver.

Note that the framework library's file name includes only the major version number. For more information about library file names, see [Framework Library Versioning](framework-library-versioning.md).
