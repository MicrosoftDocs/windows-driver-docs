---
title: Using an INF File to Uninstall a File System Filter Driver
description: Describes various ways to uninstall a file system filter driver
keywords:
- INF files WDK file system , uninstalling filter drivers
- uninstalling filter drivers WDK file system
ms.date: 02/23/2023
---

# Using an INF file to uninstall a file system filter driver

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

Starting with Windows 10 version 1903, the **DefaultUninstall** and **DefaultUninstall.Services** INF sections are prohibited [(with exception)](../develop/creating-a-primitive-driver.md#legacy-compatibility).

In Windows 10 prior to version 1903, the **DefaultUninstall** and **DefaultUninstall.Services** sections were optional but recommended if the driver could be uninstalled. For these OS versions, you can uninstall your filter driver by using the command line, PowerShell, or a batch file to execute these INF file sections, or a user-mode uninstall application.

There's no "right-click uninstall" option.

## Command-Line or Batch File Uninstall

To execute the **DefaultUninstall** and **DefaultUninstall.Services** sections of your INF file on the command line, type the following command at the command prompt, or create and run a batch file that contains this command:

```Command Line
RUNDLL32.EXE SETUPAPI.DLL,InstallHinfSection DefaultUninstall 132 path-to-uninstall-dir\infname.inf
```

For more information, see [**Rundll32**](/windows-server/administration/windows-commands/rundll32) and [**InstallHinfSection**](/windows/win32/api/setupapi/nf-setupapi-installhinfsectiona).

## PowerShell Uninstall

Type the following command at the PowerShell command prompt:

```PowerShell
Get-CimInstance Win32_SystemDriver -Filter "name='your_driver_name'" | Invoke-CimMethod -MethodName Delete
```

Fore more information, see [CimCmdlets](/powershell/module/cimcmdlets).

## Uninstall Application

You can also execute the **DefaultUninstall** and **DefaultUninstall.Services** sections of your INF file from an uninstall application, as shown in the following code example:

```cpp
InstallHinfSection(NULL,NULL,TEXT("DefaultUninstall 132 path-to-uninstall-dir\infname.inf"),0);
```

If you use an application to uninstall your driver, observe the following guidelines:

* To prepare for eventual uninstall, a setup application should copy the driver INF file to an uninstall directory.
* In the **DefaultUninstall.Services** section of the INF file, the **DelService** directive should always specify the 0x200 (SPSVCINST\_STOPSERVICE) flag to stop the service before it's deleted.
* If a user-mode application was installed with the driver, this application should be listed in Add or Remove Programs in Control Panel so that the user can uninstall it if desired. Only one item should be listed, representing both the application and the driver. For more information about how to list your application in Add or Remove Programs, see "Removing an Application" in the Setup and System Administration section of the Microsoft Windows SDK documentation.
* An uninstall application shouldn't delete the INF file (or its associated PNF file) from the Windows INF file directory (*%windir%\\INF*).
* Some filter driver files can't safely be removed when the application is uninstalled. These files shouldn't be listed in the **DefaultUninstall.Services** section of the INF file.

For more information about uninstall applications, see [Writing a Device Installation Application](../install/writing-a-device-installation-application.md).
