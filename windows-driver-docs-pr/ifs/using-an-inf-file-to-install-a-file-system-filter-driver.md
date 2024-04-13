---
title: Using an INF File to Install a File System Filter Driver
description: Using an INF File to Install a File System Filter Driver
keywords:
- INF files WDK file system filter driver, installation steps
ms.date: 12/06/2023
---

# Using an INF File to Install a File System Filter Driver

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

This article describes how a legacy file system filter driver developer can use an INF file for driver installation.

After you create an INF file, you can use it to install, upgrade, and uninstall your file system filter driver. You can use the INF file alone or together with a batch file or a user-mode setup application.

## Right-Click Install

To execute the [**DefaultInstall**](../install/inf-defaultinstall-section.md) and [**DefaultInstall.Services**](../install/inf-defaultinstall-services-section.md) sections of your INF file, do the following:

1. In Windows Explorer, select and hold (or right-click) the INF file name. A shortcut menu appears.

2. Select **Install**.

> [!NOTE]
> The shortcut menu appears only if the INF file contains a **DefaultInstall** section.

## Command-Line or Batch File Install

To execute the **DefaultInstall** and **DefaultInstall.Services** sections of your INF file on the command line or by using a batch file installation, type the following command at the command prompt, or create and run a batch file that contains this command:

``` console
RUNDLL32.EXE SETUPAPI.DLL,InstallHinfSection DefaultInstall 132 path-to-inf\infname.inf
```

"Rundll32" and "InstallHinfSection" are described in the Tools and Setup and System Administration sections, respectively, of the Microsoft Windows SDK documentation.

## Setup Application

[**InstallHinfSection**](/windows/win32/api/setupapi/nf-setupapi-installhinfsectiona) can also be called from a setup application, as shown in the following code example:

```cpp
InstallHinfSection(NULL,NULL,TEXT("DefaultInstall 132 path-to-inf\infname.inf"),0); 
```

If you use a setup application to install your driver, observe the following guidelines:

* To prepare for eventual uninstall, the setup application should copy the driver INF file to an uninstall directory.

* If the setup application installs a user-mode application with the driver, this application should be listed in Add or Remove Programs in Control Panel so that the user can uninstall it if desired. Only one item should be listed, representing both the application and the driver. For more information about how to list your application in Add or Remove Programs, see "Removing an Application" in the Setup and System Administration section of the Windows SDK documentation.

* Setup applications should never copy driver INF files to the Windows INF file directory (*%windir%\\INF*). SetupAPI copies the files there automatically as part of the [**InstallHinfSection**](/windows/win32/api/setupapi/nf-setupapi-installhinfsectiona) call.

For more information about setup applications, see [Writing a Device Installation Application](../install/writing-a-device-installation-application.md).
