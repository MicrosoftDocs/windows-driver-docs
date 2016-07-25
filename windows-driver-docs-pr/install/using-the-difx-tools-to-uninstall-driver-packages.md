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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Using%20the%20DIFx%20Tools%20to%20Uninstall%20Driver%20Packages%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




