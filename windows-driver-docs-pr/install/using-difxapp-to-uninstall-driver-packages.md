---
title: Using DIFxApp to Uninstall Driver Packages
description: Using DIFxApp to Uninstall Driver Packages
ms.assetid: 4bf6ba68-8e81-48aa-87b3-fbeb79f4ec26
---

# Using DIFxApp to Uninstall Driver Packages


Driver Install Frameworks for Applications (DIFxApp) version 2.1 is a component of Driver Install Frameworks (DIFx) version 2.1. With DIFxApp, Microsoft Windows Installer can be used to install signed [driver packages](driver-packages.md) that are associated with applications in a Windows Installer installation package. DIFxApp is designed for vendors who either already have a Windows Installer installation package for their applications or plan to create one.

DIFxApp supports many installation scenarios, and also supports uninstalling the [driver packages](driver-packages.md) that it installs. This topic describes how to uninstall driver packages by using DIFxApp.

For more information about uninstalling driver and driver packages, see [How Devices and Driver Packages are Uninstalled](how-devices-and-driver-packages-are-uninstalled.md).

### <a href="" id="uninstalling-the-device"></a> Uninstalling the Device

You cannot use DIFxApp to uninstall a device. To perform this action, you must either use [Device Manager](using-device-manager.md) or a [*device installation application*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application) that calls [SetupAPI](setupapi.md) functions.

For more information about how to uninstall device nodes ([*devnodes*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)), see [Using Device Manager to Uninstall Devices and Driver Packages](using-device-manager-to-uninstall-devices-and-driver-packages.md) and [Using SetupAPI to Uninstall Devices and Driver Packages](using-setupapi-to-uninstall-devices-and-driver-packages.md).

### <a href="" id="deleting-a-driver-package-from-the-driver-store"></a> Deleting a Driver Package from the Driver Store

By default, DIFxApp adds an entry to **Programs and Features** in Control Panel for each driver package that it installs. Use the following steps to remove the driver package:

1.  In Control Panel, double-click **Programs and Features**.

2.  Click the entry for the driver package.

3.  Click **Uninstall/Change** to uninstall the package.

**Note**  In versions of Windows earlier than Windows Vista, **Programs and Features** in Control Panel was named **Add or Remove Programs**.

 

### <a href="" id="deleting-the-binary-files-of-the-installed-driver"></a> Deleting the Binary Files of the Installed Driver

By default, when you uninstall a driver package with the **Programs and Features** in Control Panel, you remove the driver package from the DIFx driver store, but you do not remove the driver's binary files. There are two ways to have **Programs and Features** remove the binary files:

-   Set the corresponding DIFxApp configuration flag to remove installed files.

-   Use the Windows Installer XML (WiX) tools to create an installation package. In the corresponding WiX XML source file, set the **DriverDeleteFiles** attribute to *yes* for the component that represents the driver package.

**Note**  Starting with Windows 7, the DIFxApp configuration flag to remove installed files, together with the **DriverDeleteFiles** attribute, are ignored by the operating system. Binary files, which were copied to a system when a driver package was installed, can no longer be deleted by using DIFxApp.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Using%20DIFxApp%20to%20Uninstall%20Driver%20Packages%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




