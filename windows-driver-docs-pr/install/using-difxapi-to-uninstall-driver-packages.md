---
title: Using DIFxAPI to Uninstall Driver Packages
description: Using DIFxAPI to Uninstall Driver Packages
ms.assetid: 2a3a9cb8-7418-41dd-b071-a2f25155c2be
---

# Using DIFxAPI to Uninstall Driver Packages


Driver Install Frameworks API (DIFxAPI) version 2.1 is a component of Driver Install Frameworks (DIFx) version 2.1. DIFxAPI makes it simpler to create applications that install and uninstall driver packages. DIFxAPI is available starting with Microsoft Windows 2000. DIFxAPI includes the following components:

-   32-bit components that support x86-based systems.

-   64-bit components that support x64-based systems.

-   64-bit component that support Itanium-based systems.

DIFxAPI also supports uninstalling the [driver packages](driver-packages.md) that it installs. This topic describes how to uninstall driver packages by using DIFxAPI.

For more information about uninstalling driver and driver packages, see [How Devices and Driver Packages are Uninstalled](how-devices-and-driver-packages-are-uninstalled.md).

### <a href="" id="uninstalling-the-device"></a> Uninstalling the Device

You cannot use DIFxAPI to uninstall a device. To perform this action, you must either use [Device Manager](using-device-manager.md) or a [*device installation application*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application) that calls [SetupAPI](setupapi.md) functions.

For more information about how to uninstall device nodes ([*devnodes*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)), see [Using Device Manager to Uninstall Devices and Driver Packages](using-device-manager-to-uninstall-devices-and-driver-packages.md) and [Using SetupAPI to Uninstall Devices and Driver Packages](using-setupapi-to-uninstall-devices-and-driver-packages.md).

### <a href="" id="deleting-a-driver-package-from-the-driver-store"></a> Deleting a Driver Package from the Driver Store

To delete the driver package, call the [**DriverPackageUninstall**](https://msdn.microsoft.com/library/windows/hardware/ff544822) function with the *Flags* parameter set to a value of zero.

If this operation is part of a driver update procedure, first call the [**DriverPackageInstall**](https://msdn.microsoft.com/library/windows/hardware/ff544813) function to install the updated [driver package](driver-packages.md) before you call **DriverPackageUninstall**.

### <a href="" id="deleting-the-binary-files-of-the-installed-driver"></a> Deleting the Binary Files of the Installed Driver

To delete the driver package and the associated driver binaries, call the [**DriverPackageUninstall**](https://msdn.microsoft.com/library/windows/hardware/ff544822) function with the *Flags* parameter set to DRIVER\_PACKAGE\_DELETE\_FILES.

**Note**   Starting with Windows 7, the DRIVER\_PACKAGE\_DELETE\_FILES flag is ignored by **DriverPackageUninstall**. Binary files, which were copied to a system when a driver package was installed, can no longer be deleted by calling this function.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Using%20DIFxAPI%20to%20Uninstall%20Driver%20Packages%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




