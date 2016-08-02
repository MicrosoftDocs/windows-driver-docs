---
title: Using the DIFx Tools to Uninstall Driver Packages
description: Using the DIFx Tools to Uninstall Driver Packages
ms.assetid: 85f15e3b-f53c-45ff-ab51-104e9b110ad1
---

# Using the DIFx Tools to Uninstall Driver Packages


Driver Install Frameworks (DIFx) includes several tools that can be used to install and uninstall [driver packages](driver-packages.md). These tools include the following:

-   DIFx for Applications (DIFxApp)

-   Driver Package Installer (DPInst)

-   DIFx API (DIFxAPI)

Be aware of the following points when you use the DIFx tools to install or uninstall [driver packages](driver-packages.md):

-   You must use the same DIFx tool to install and uninstall a driver package. For example, you cannot install a driver package by using DIFxApp and then uninstall it by using DPInst.

-   You cannot use the DIFx tools to uninstall devices. To perform this action, you must either use [Device Manager](using-device-manager.md) or a [*device installation application*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application) that calls [SetupAPI](setupapi.md) functions.

    For more information, see [Using Device Manager to Uninstall Devices and Driver Packages](using-device-manager-to-uninstall-devices-and-driver-packages.md) and [Using SetupAPI to Uninstall Devices and Driver Packages](using-setupapi-to-uninstall-devices-and-driver-packages.md).

This section includes the following topics:

[Using DIFxApp to Uninstall Driver Packages](using-difxapp-to-uninstall-driver-packages.md)

[Using DPInst to Uninstall Driver Packages](using-dpinst-to-uninstall-driver-packages.md)

[Using DIFxAPI to Uninstall Driver Packages](using-difxapi-to-uninstall-driver-packages.md)

**Important**  We recommend that you only use the DIFx tools to create driver uninstallers. Applications that use the DIF*x* tools to uninstall drivers are designed to work correctly with future versions of Windows. Although other approaches might be successful with the current versions of Windows, they may not work correctly with future versions.

 

 

 





