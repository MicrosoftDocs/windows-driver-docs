---
title: Building a Windows driver
description: Guide to building a Windows Driver
ms.date: 04/28/2020
---

# Building a Windows driver

You can use Microsoft Visual Studio 2019 in conjunction with the [Windows Driver Kit (WDK) Version 2004](../download-the-wdk.md) to build Windows Drivers. You can download kits and tools from the [Windows Hardware Dev Center](https://go.microsoft.com/fwlink/p/?LinkId=524487).

In many cases, you can recompile a legacy kernel-mode driver as a Windows Driver, as long as the driver does not work with any user-mode components. Legacy WDM and KMDF drivers should recompile as Windows Drivers targeting Windows 10 with no conversion required.  While the drivers may compile without any conversion, this does not mean that the driver meets all of the Windows Drivers requirements.  Please see [Getting Started with Windows Drivers](getting-started-with-windows-drivers.md) for details regarding Windows Drivers requirements.  

In contrast, existing user-mode drivers may require modification to compile as Windows drivers. Specifically, your driver package must not have any dependencies outside of UWP. For example, only some of the Win32 APIs are part of UWP.

## Converting an existing driver project to a Windows driver project

1.  In Visual Studio 2019, open the existing driver project.
2.  In the Solution Explorer pane, select and hold (or right-click) the solution and choose **Configuration Manager**. Set the target operating system to Windows 10.
3.  Select and hold (or right-click) the driver project and choose **Properties**. Under **Configuration Properties-&gt;Driver**, verify that **Target Platform** is set to **Windows Drivers**. To build a driver that runs on Windows 10 for Desktop editions only, select **Desktop**.
4.  Build the driver. You might see linker errors.
5.  Fix the errors one by one by going through the error log. Refer to individual reference pages in the documentation for possible alternate APIs. If replacements are not available, you may need to redesign your driver.

## Creating a New Windows Driver Project in Microsoft Visual Studio

1.  Create a new driver from a template (**File->New Project->Create New Project->Project Type->Driver->Select the template of interest**).
2.  After you create the project, in the Solution Explorer pane, select and hold (or right-click) the solution and choose **Configuration Manager**. Set **Active solution configuration** to the desired target Windows version, and set **Active solution platform** to **Win32** or **x64**. If **ARM** is not listed, choose **&lt;New...&gt;** to build for ARM.

    If you choose Windows 10, the driver model defaults to **Universal**.

    To change driver model manually, select and hold (or right-click) the driver project and choose Properties. Under **Configuration Properties->Driver Settings->General**, find the **Target Platform** entry. Choose **Windows Driver**. Microsoft Visual Studio uses this setting to determine what libraries to link against.

    **Note**  You cannot build a Windows Driver for Windows versions earlier than Windows 10 Version 1809.
3.  You might need to modify the .inf file to specify the provider, specified as an %*ManufacturerName*% token that is expanded later in the INF file's [**Strings**](../install/inf-strings-section.md) section. For example:

    ```cpp
    Provider="Contoso"
    ```

4.  You can now build the solution. Visual Studio links against the required libraries and generates a .cat file, an .inf file, and a driver binary.

## Creating a New Universal Application or DLL Project in Microsoft Visual Studio

1.	Create a new driver from a template (**File->New Project->Create New Project->Project Type->Driver->Select the template of interest**) and choose **Empty Desktop Application for Drivers (Universal)** or **Empty Dll for Drivers (Universal)**.
2.	After you create the project, in the Solution Explorer pane, select and hold (or right-click) the solution and choose **Configuration Manager**. Set **Active solution configuration** to the desired target Windows version, and set **Active solution platform** to **Win32** or **x64**. If ARM is not listed, choose **<New...>** to build for ARM.
If you choose Windows 10, the application model defaults to **Universal**.
To change the target platform manually, select and hold (or right-click) the driver project and choose Properties. Under **Configuration Properties->Driver Settings->General**, find the **Target Platform** entry.
3.	Build the solution.

For information about the configuration settings you can use in Visual Studio when building your driver, see [Building a Driver with the WDK](building-a-driver.md).
