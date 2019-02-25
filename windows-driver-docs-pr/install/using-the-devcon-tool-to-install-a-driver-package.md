---
title: Using the DevCon Tool to Install a Driver Package
description: Using the DevCon Tool to Install a Driver Package
ms.assetid: d77573e0-7866-46a5-88bc-c911bbd2a165
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using the DevCon Tool to Install a Driver Package


The example in this topic uses the *ToastPkg* sample [driver package](driver-packages.md). Within the WDK installation directory, the package's source files are located in the *src\\general\\toaster\\toastpkg\\toastcd* directory. After you have built and digitally-signed this driver package, copy the driver package to the directory *c:\\toaster* on the test computer.

To install the driver package through DevCon, do the following:

1.  To use the DevCon tool, the user must be a member of the Administrators group on the test computer and run DevCon from an elevated command prompt. To open an elevated Command Prompt window, create a desktop shortcut to *Cmd.exe*, right-click the *Cmd.exe* shortcut, and select **Run as administrator**.

2.  From the elevated, Command Prompt window, enter the following:

    ```cpp
    devcon.exe install c:\toaster\toastpkg.inf {b85b7c50-6a01-11d2-b841-00c04fad5171}\mstoaster
    ```

    This command-line specifies the location of the driver package's INF file (*c:\\toaster\\toastpkg.inf*) and the toaster device's hardware identifier (ID), which is specified within the INF file.

 

 





