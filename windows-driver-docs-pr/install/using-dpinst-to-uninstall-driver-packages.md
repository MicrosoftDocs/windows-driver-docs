---
title: Using DPInst to Uninstall Driver Packages
description: Using DPInst to Uninstall Driver Packages
ms.assetid: 08e4a19c-453f-4ce1-9117-ce290e5f6ef2
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using DPInst to Uninstall Driver Packages


Driver Package Installer (DPInst) version 2.1 is a component of Driver Install Frameworks (DIFx) version 2.1 that simplifies and customizes the installation of [driver packages](https://msdn.microsoft.com/windows-drivers/develop/creating_a_driver_package) for devices that have not yet been installed in a computer (commonly known as a [software-first installation](software-first-installation.md)). DPInst also automatically updates the drivers for any installed devices that are supported by the newly installed driver packages.

DPInst also supports uninstalling the [driver packages](driver-packages.md) that it installs. This topic describes how to uninstall driver packages by using DPInst.

For more information about uninstalling driver and driver packages, see [How Devices and Driver Packages are Uninstalled](how-devices-and-driver-packages-are-uninstalled.md).

### <a href="" id="uninstalling-the-device"></a> Uninstalling the Device

You cannot use DPInst to uninstall a device. To perform this action, you must either use [Device Manager](using-device-manager.md) or a [*device installation application*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application) that calls [SetupAPI](setupapi.md) functions.

For more information about how to uninstall device nodes ([*devnodes*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)), see [Using Device Manager to Uninstall Devices and Driver Packages](using-device-manager-to-uninstall-devices-and-driver-packages.md) and [Using SetupAPI to Uninstall Devices and Driver Packages](using-setupapi-to-uninstall-devices-and-driver-packages.md).

### <a href="" id="deleting-a-driver-package-from-the-driver-store"></a> Deleting a Driver Package from the Driver Store

By default, DPInst adds an entry to **Programs and Features** in Control Panel for each [driver package](driver-packages.md) that it installs. You can remove the driver package by using **Programs and Features** in the following way:

1.  In Control Panel, double-click **Programs and Features**.

2.  Click the entry for the driver package.

3.  Click **Uninstall/Change** to uninstall the package.

**Note**  In versions of Windows earlier than Windows Vista, the **Programs and Features** in Control Panel was named **Add or Remove Programs**.

 

You can also delete the driver package by running DPInst from the command line with the **/u** switch. The following command removes the driver package whose INF file is specified by *InfFilePath:*

```
DPInst.exe /u InfFilePath
```

**Note**  The path that is specified by *InfFilePath* is in relation to the directory that contains *DPInst.exe*.

 

### <a href="" id="deleting-the-binary-files-of-the-installed-driver"></a> Deleting the Binary Files of the Installed Driver

By default, when you uninstall a device by using **Programs and Features** in Control Panel, you remove only the driver package and not the driver's binary files. To have **Programs and Features** also remove the binary files, set the [**deleteBinaries XML element**](https://msdn.microsoft.com/library/windows/hardware/ff541076) in the DPInst descriptor file to ON.

You can also have DPInst delete driver binaries by running DPInst from the command line with the **/d** switch. The following command removes the driver package and associated binaries:

```
DPInst.exe /u InfFilePath /d 
```

**Note**   Starting with Windows 7, both the **deleteBinaries** XML element and the **/d** switch are ignored by the operating system. Binary files, which were copied to a system when a [driver package](driver-packages.md) was installed, can no longer be deleted by using DPInst.

 

 

 





