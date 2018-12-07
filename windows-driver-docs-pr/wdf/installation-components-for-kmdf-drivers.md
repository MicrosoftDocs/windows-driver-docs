---
title: Redistributable Framework Components
description: This topic describes the Microsoft-supplied redistributable framework updates that are included as part of the Windows Driver Kit (WDK) for Windows 8.1, and how to determine which ones to add to your driver package.
ms.assetid: 63fbe66e-fa1b-4a70-a8ea-df4f3df9bad4
keywords:
- framework-based drivers WDK KMDF , installing
- INF files WDK KMDF , about installing KMDF drivers
- installation components for drivers WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Redistributable Framework Components


This topic describes the Microsoft-supplied redistributable framework updates that are included as part of the Windows Driver Kit (WDK) for Windows 8.1, and how to determine which ones to add to your driver package.

To determine if you need to include any framework updates at all in your driver package, see [Building and Loading a WDF Driver](building-and-loading-a-kmdf-driver.md). If you don't, skip this topic.

## Should I include the co-installer or the .msu file?


If your driver installation is triggered by plugging in a new hardware device to a system and you are installing only the driver, include the co-installer in your driver package. Then reference the co-installer in your INF file, as described in [Specifying the KMDF Co-installer in an INF File](installing-the-framework-s-co-installer.md).

If you need to install an application in addition to your driver, you should instead redistribute the relevant MSU package (for example kmdf-1.11-Win.6.0.msu) along with a setup application that calls it. You can find a sample of such an application in the WDK, in the src\\general\\installwdf directory.

In the latter case, no INF entries are needed.

## Where can I find these files, and what's included?


When you build your driver in Visual Studio, MSBuild places the co-installer in the resulting Package directory, along with the driver's .*sys* and INF files.

The full set of redistributable framework update files is located in *%programfiles%*\\windows kits\\*&lt;WDK version&gt;*\\redist\\wdf.

This directory contains the following files, for x86 and x64:

-   *WdfCoinstaller01009.dll*, *wdfcoinstaller01011.dll* (co-installers for KMDF 1.9/1.11).
-   *WUDFUpdate\_01009.dll*, *WUDFUpdate\_01011.dll* (co-installers for UMDF).
-   *winusbcoinstaller.dll*, *winusbcoinstaller2.dll* (co-installers for WinUSB 1.5/1.9).
-   *WinUSB\_1.9.msu* – WinUSB version 1.9 update, also available as [KB971286](http://support.microsoft.com/kb/971286).
-   *kmdf-1.11-Win-6.0.msu*, *kmdf-1.11-Win-6.1.msu* - Windows Update package for KMDF 1.11 for Windows Vista (v6.0) / Windows 7 (v6.1).
-   *umdf-1.11-Win-6.0.msu*, *umdf-1.11-Win-6.1.msu* – Windows Update package for UMDF 1.11 for Windows Vista (v6.0) / Windows 7 (v6.1).

## Co-installer Naming and Versioning


The co-installer is named **WdfCoInstaller**<em>MMmmm</em>**.dll**.

-   *MM* is the major version number.
-   *mmm* is the minor version number.

For example, the filename for version 1.0 of the co-installer is *WdfCoInstaller01000.dll*, and the filename for version 1.11 is *WdfCoInstaller01011.dll*.

The version of the co-installer that you include with your driver package must match the version of the framework library that you use to develop your driver.

Note that the framework library's file name includes only the major version number. For more information about library file names, see [Framework Library Versioning](framework-library-versioning.md).

 

 





