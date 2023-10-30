---
title: Using the DevCon tool to install a driver package
description: Provides information about using the DevCon tool to install a driver package.
ms.date: 07/26/2022
---

# Using the DevCon tool to install a driver package

> [!IMPORTANT]
> PnPUtil ships with every release of Windows and makes use of the most reliable and secure APIs available and its use is recommended. For more information on using PnPutil instead of devcon, see [PnPUtil](../devtest/pnputil.md).

To install the driver package through DevCon, do the following:

1. To use the DevCon tool, the user must be a member of the Administrators group on the test computer and run DevCon from an elevated command prompt. To open an elevated Command Prompt window, create a desktop shortcut to *Cmd.exe*, select and hold (or right-click) the *Cmd.exe* shortcut, and select **Run as administrator**.

1. From the elevated Command Prompt window, enter the following:

    ```console
    devcon.exe update <path to INF file> <ID match from INF file>
    ```

> [!NOTE]
> While you may have seen some instructions recommending using the *install* parameter to Devcon, Devcon's *install* command creates a root enumerated device with the hardware ID that you specify before attempting to install the driver package. If the system already has hardware that the driver package is intended to install on, Devcon's *update* command should be used instead.
