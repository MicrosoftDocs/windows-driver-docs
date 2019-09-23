---
title: Using an INF File to Uninstall a File System Filter Driver
description: Using an INF File to Uninstall a File System Filter Driver
ms.assetid: e41deb65-7977-479c-ac42-c550aa6a3f1b
keywords:
- INF files WDK file system , uninstalling filter drivers
- uninstalling filter drivers WDK file system
ms.date: 07/15/2019
ms.localizationpriority: medium
---

# Using an INF File to Uninstall a File System Filter Driver

You can uninstall your driver by using the command line, PowerShell, an INF file together with a batch file, or a user-mode uninstall application.

There is no "right-click uninstall" option.

## Command-Line or Batch File Uninstall

To execute the **DefaultUninstall** and **DefaultUninstall.Services** sections of your INF file on the command line, type the following command at the command prompt, or create and run a batch file that contains this command:

```Command Line
RUNDLL32.EXE SETUPAPI.DLL,InstallHinfSection DefaultUninstall 132 path-to-uninstall-dir\infname.inf
```

**Rundll32** and **InstallHinfSection** are described in the Tools and Setup and System Administration sections, respectively, of the Microsoft Windows SDK documentation.

## Powershell Uninstall

Type the following command at the Powershell command prompt:

```PowerShell
Get-CimInstance Win32_SystemDriver -Filter "name='your_driver_name'" | Invoke-CimMethod -MethodName Delete
```

## Uninstall Application

You can also execute the **DefaultUninstall** and **DefaultUninstall.Services** sections of your INF file from an uninstall application, as shown in the following code example:

```cpp
InstallHinfSection(NULL,NULL,TEXT("DefaultUninstall 132 path-to-uninstall-dir\infname.inf"),0);
```

If you use an application to uninstall your driver, observe the following guidelines:

* To prepare for eventual uninstall, a setup application should copy the driver INF file to an uninstall directory.
* In the **DefaultUninstall.Services** section of the INF file, the **DelService** directive should always specify the 0x200 (SPSVCINST\_STOPSERVICE) flag to stop the service before it is deleted.
* If a user-mode application was installed with the driver, this application should be listed in Add or Remove Programs in Control Panel so that the user can uninstall it if desired. Only one item should be listed, representing both the application and the driver. For more information about how to list your application in Add or Remove Programs, see "Removing an Application" in the Setup and System Administration section of the Microsoft Windows SDK documentation.
* An uninstall application should not delete the INF file (or its associated PNF file) from the Windows INF file directory (*%windir%\\INF*).
* Some filter driver files cannot safely be removed when the application is uninstalled. These files should not be listed in the **DefaultUninstall.Services** section of the INF file.

For more information about uninstall applications, see [Writing a Device Installation Application](https://docs.microsoft.com/windows-hardware/drivers/install/writing-a-device-installation-application).
