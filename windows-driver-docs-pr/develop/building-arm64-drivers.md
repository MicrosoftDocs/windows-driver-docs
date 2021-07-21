---
title: Building ARM64 Drivers with the WDK
description: This topic describes how to build an ARM64 driver with the Windows Driver Kit (WDK).
ms.date: 01/18/2018
ms.localizationpriority: medium
---

# Building ARM64 Drivers with the WDK

Windows 10 can run on machines that are powered by ARM64 processors.  However, because Windows 10 on ARM does not support emulation of x86 kernel-mode drivers, you must recompile kernel-mode drivers to ARM64 using the instructions below.

## Setup

1. Download [Visual Studio 2017 or 2019](https://visualstudio.microsoft.com/downloads/).  You'll need at minimum version 15.9.
2. On the Windows start menu, type **Visual Studio Installer**.  Then on the **Workloads** tab, select **Desktop development with C++**.  
![Selecting Desktop development with C++ from Windows options on Workloads tile.](images/VS-workloads.png)

2. On the **Individual Components** tab, select the following options:
    *  **Visual C++ compilers and libraries for ARM**
    *  **Visual C++ compilers and libraries for ARM64**  
![Selecting ARM-specific components to install.](images/VS-individual-components.png)

3.	Install and restart Visual Studio.
4.  Download the [Windows SDK](https://developer.microsoft.com/windows/downloads/windows-10-sdk).  Ensure that you have SDK version 16299 (Windows 10, version 1709) or later.
5.	Download the [WDK](../download-the-wdk.md).  Ensure that you have WDK version 16299 or later.

## Building an ARM64 Driver with the WDK

1.	In Visual Studio, open a driver solution.  You can use your own, or one from the [Windows-driver-samples](https://github.com/Microsoft/Windows-driver-samples) repo.
2.	Select Solutions platform and select **Configuration Manager**.  
![Selecting configuration manager from second dropdown on top toolbar.](images/VS-config-mgr.png)
  
3.	Under **Active Solution Platform**, select **New**.  
![Selecting New under Active Solution Platform dropdown.](images/VS-active-solution-platform.png)

4.	From **Type or Select new Platform**, select **ARM64**.  Copy settings from **Win32**.  Select **OK** and **Close**.  
![Selecting ARM64 build target from toolbar-level dropdown.](images/VS-build-ARM64.png)

5.	Select **ARM64** as the target platform and rebuild.

## See Also

* [Debugging ARM64](../debugger/debugging-arm64.md)
* [Windows 10 on ARM](/windows/uwp/porting/apps-on-arm)
* [HLK ARM64 Getting Started Guide](/windows-hardware/test/hlk/getstarted/hlk-arm64-getting-started-guide)