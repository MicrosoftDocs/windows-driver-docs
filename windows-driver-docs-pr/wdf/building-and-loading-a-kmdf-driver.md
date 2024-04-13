---
title: Building and Loading a WDF Driver
description: This topic describes how to select a target operating system and framework version for a driver project in Visual Studio. It also describes the co-installer and how to determine if you should include this component in your driver package.
keywords:
- kernel-mode drivers WDK KMDF , building drivers
- KMDF WDK , building drivers
- Kernel-Mode Driver Framework WDK , building drivers
- kernel-mode drivers WDK KMDF , loading drivers
- KMDF WDK , loading drivers
- Kernel-Mode Driver Framework WDK , loading drivers
- building drivers WDK , KMDF
- loading drivers WDK KMDF
- Build utility WDK , KMDF
- KMDF drivers WDK KMDF , building
- KMDF drivers WDK KMDF , loading
ms.date: 05/16/2019
---

# Building and Loading a WDF Driver


This topic describes how to select a target operating system and framework version for a driver project in Visual Studio.

To determine if you need to include redistributable framework components in your driver package, see [Redistributable Framework Components](installation-components-for-kmdf-drivers.md).


## Which framework version should I use?

*   To target Windows XP, use WDF 1.9 or earlier.
*   To target Windows Vista, Windows 7, or Windows 8, use WDF 1.11 or earlier.
*   To target Windows 8.1, use KMDF 1.13 or earlier, or UMDF 1.x, or UMDF 2.0.
*   To target Windows 10 version 1507, use KMDF 1.15 or earlier, or UMDF 1.x, or UMDF 2.15 or earlier.

For detailed information about KMDF and UMDF versions, see [KMDF Version History](kmdf-version-history.md) and [UMDF Version History](umdf-version-history.md).

* [KMDF Version History](kmdf-version-history.md)
* [UMDF Version History](umdf-version-history.md)

## How do I set the versions in Visual Studio?


If you're building your driver project for the latest version of Windows and the most recent KMDF or UMDF version, you can keep the defaults and skip this step.

Otherwise, follow these steps:

-   Right-click the solution and select **Configuration Manager**.  Set **Project Configuration** to the desired value (for example **Debug**).
-   Right-click the driver project and select **Properties**.  Open **Configuration Properties->Driver Settings->Driver Model**.  Change the **KMDF Version Minor (Target Version)** or **UMDF Version Minor (Target Version)** value in the [Driver Model Settings](../develop/driver-model-settings-properties-for-driver-projects.md) to the desired value.  For info about **KMDF Version Minor (Minimum Required)** and **UMDF Version Minor (Minimum Required)**, see [Specifying Minimum Required](./building-a-wdf-driver-for-multiple-versions-of-windows.md#specifying-minimum-required).

You can use the Windows Driver Kit (WDK) that ships with Windows 10 to build KMDF 1.9-1.29 drivers, as well as UMDF 1.9-2.29 drivers.

For detailed information about KMDF and UMDF versions, see [KMDF Version History](kmdf-version-history.md) and [UMDF Version History](umdf-version-history.md).

* [KMDF Version History](kmdf-version-history.md)
* [UMDF Version History](umdf-version-history.md)

## Linking and loading


When you build a Windows Driver Frameworks (WDF) project in Microsoft Visual Studio, MSBuild links your driver to the appropriate framework library, the library's loader, and a stub file, all of which are included in the WDK. (The library and loader are also included in the framework's [co-installer](installing-the-framework-s-co-installer.md) so that if necessary, you can distribute them with your driver package.)

The stub file contains a special entry point routine: **FxDriverEntry**. MSBuild sets the stub's **FxDriverEntry** routine as the initial entry point for framework-based drivers.

When the operating system loads a framework-based driver, it also loads the stub file and the library's loader. Next, the system calls the stub file's **FxDriverEntry** routine. This routine then calls the loader. The loader determines the version of the framework library that the driver requires and then loads the correct [version of the library](framework-library-versioning.md) as a kernel-mode service (if it is not already loaded). Finally, the library calls the driver's [**DriverEntry**](./driverentry-for-kmdf-drivers.md) routine.
