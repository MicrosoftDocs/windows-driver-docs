---
title: Using the UMDF Co-installer
description: Using the UMDF Co-installer
ms.assetid: e5ec2122-1602-487b-baad-4a3d9e47cf58
keywords:
- UMDF coinstallers WDK
- coinstallers WDK UMDF
- CoInstallers section WDK UMDF
- configurable coinstallers WDK UMDF
- system-supplied UMDF coinstallers WDK UMDF
- redistributable coinstallers WDK UMDF
- update coinstallers WDK UMDF
- INF files WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using the UMDF Co-installer


A co-installer updates the framework version stored on the machine and processes framework-specific INF file sections. This topic describes the two UMDF co-installers and when you need to include one with your [driver installation package](https://msdn.microsoft.com/windows-drivers/develop/creating_a_driver_package) or reference a co-installer in your INF file.

## Getting the Co-installer Package


In Windows 8.1, the Microsoft-supplied redistributable framework updates are included as part of the Windows Driver Kit (WDK).

For a complete list of the contents of the co-installer directory, see [Installation Components for KMDF Drivers](installation-components-for-kmdf-drivers.md).

Among other components, the co-installer directory contains an *update co-installer*, called WUDFUpdate\_*MMmmm*.dll, where *MM* is the major version number, and *mmm* is the minor version number.

The update co-installer updates the UMDF framework version that is on the computer. For example, if the computer has UMDF version 1.9 and the co-installer contains version 1.11, the co-installer updates the computer's framework version to 1.11.

The operating system includes another co-installer, called the *configuration co-installer*, or WudfCoinstaller.dll. The configuration co-installer processes the UMDF-specific sections of the driver's INF file and makes any necessary updates to the registry.

## Referencing Co-installers from your INF File


If you are writing a UMDF 2.0 driver for Windows 8.1, your INF file must reference the configuration co-installer. Because the configuration co-installer is included in the operating system, you do not need to redistribute it.

If you are writing a UMDF 1.11 driver that targets operating systems prior to Windows 8.1, you must ensure that version 1.11 of the framework is installed on machines that use your driver. Here are three ways to do this:

-   Reference the update co-installer in your INF file, and include the update co-installer in your [driver installation package](https://msdn.microsoft.com/windows-drivers/develop/creating_a_driver_package). When the operating system installs your driver, it runs the co-installer. If your driver will be distributed via Windows Update, you must choose this option.

-   Redistribute the relevant MSU package (for example umdf-1.11-Win-6.0.msu) along with a setup application that calls it. You can find a sample of such an application in the src\\general\\wdkinstall subdirectory of your WDK installation. You might choose this option if you are writing a setup program that ships with the device and must be run before the device can be used. If you choose this option, your INF file must reference the configuration co-installer.

-   Rely on Windows Update to install the required framework version on machines that use your driver. Starting with version 1.11 of the framework, new versions of UMDF are distributed via Windows Update. If you choose this option, your INF file must reference the configuration co-installer.

In your INF file, you must always reference either the update co-installer or the configuration co-installer. However, referencing both co-installers in the INF will lead to installation errors.

## INF File Sections for the Co-installer


Your driver's INF file must include an [**INF DDInstall.CoInstallers section**](https://msdn.microsoft.com/library/windows/hardware/ff547321). If you redistribute the update co-installer, your **DDInstall.CoInstallers** section must include both an [**INF AddReg directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320) and an [**INF CopyFiles directive**](https://msdn.microsoft.com/library/windows/hardware/ff546346), as the following example shows.

```cpp
[MyDriver_Install.CoInstallers]
AddReg = MyDriver_Install.CoInstallers_AddReg
CopyFiles = MyDriver_CoInstallers_CopyFiles
```

The INF **AddReg** directive identifies an INF section that creates a **CoInstallers32** registry entry.

```cpp
[MyDriver_Install.CoInstallers_AddReg]
HKR,,CoInstallers32,0x00010000,"WudfUpdate_01011.dll"
```

The INF **CopyFiles** directive identifies an INF section that copies the co-installer from the installation device to the system device.

```cpp
[MyDriver_CoInstallers_CopyFiles]
WudfUpdate_01011.dll
```

If you redistribute an MSU package, your **DDInstall.CoInstallers** section must specify an **AddReg** directive that references the configuration co-installer.

```cpp
[Echo_Install.NT.CoInstallers]
AddReg=CoInstallers_AddReg
[CoInstaller.AddReg]
HKR,,CoInstallers32,0x00010000,WudfCoinstaller.dll
```

Your driver's INF file must always contain a **DDInstall.Wdf** section that the co-installer reads after it has been installed. For information about directives that your driver can specify in **DDInstall.Wdf**, see [Specifying WDF Directives in INF Files](specifying-wdf-directives-in-inf-files.md).

You can avoid creating multiple INF files for multiple versions of the framework by using INX files and the [Stampinf](https://msdn.microsoft.com/library/windows/hardware/ff552786) tool. For more information about INX files, see [Using INX Files to Create INF Files](using-inx-files-to-create-inf-files.md).

 

 





