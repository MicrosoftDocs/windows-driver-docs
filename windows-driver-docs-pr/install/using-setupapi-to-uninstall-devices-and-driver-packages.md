---
title: Using SetupAPI to Uninstall Devices and Driver Packages
description: Using SetupAPI to Uninstall Devices and Driver Packages
ms.assetid: e170961b-5d12-43d5-b502-3b37e6421f6e
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using SetupAPI to Uninstall Devices and Driver Packages


[SetupAPI](setupapi.md) is a system component that provides two sets of functions:

-   [General Setup functions](https://msdn.microsoft.com/library/windows/hardware/ff544985)

-   [Device installation functions](https://msdn.microsoft.com/library/windows/hardware/ff541299)

[*Device installation applications*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application), [*co-installers*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-co-installer), and [*class installers*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-class-installer) can use these functions to perform custom operations for device installation. SetupAPI also supports uninstalling the devices and [driver packages](driver-packages.md) that it installs.

This topic describes the procedures that you can follow to uninstall devices and driver packages by using the SetupAPI functions.

For more information about uninstalling driver and driver packages, see [How Devices and Driver Packages are Uninstalled](how-devices-and-driver-packages-are-uninstalled.md).

### <a href="" id="uninstalling-the-device"></a> Uninstalling the Device

[SetupAPI](setupapi.md) allows you to uninstall a device and remove the device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) from the system by using the following methods:

-   A device installation application can request that a device be uninstalled by calling the [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922) function. When the application calls this function to uninstall a device, it must set the *InstallFunction* parameter to the [**DIF_REMOVE**](https://msdn.microsoft.com/library/windows/hardware/ff543717) code.  For a list of all DIF codes, see [Device Installation Functions](https://msdn.microsoft.com/library/windows/hardware/ff541307).

    If [**SetupDiRemoveDevice**](https://msdn.microsoft.com/library/windows/hardware/ff552097) is called during the processing of the DIF_REMOVE request, the function removes the device's devnode from the system. It also deletes the device's hardware and software registry keys, together with any hardware-profile-specific registry keys (configuration-specific registry keys).

    **Note**  **SetupDiRemoveDevice** must only be called by a class installer and not by a device installation application.

    For more information about DIF codes, see [Handling DIF Codes](handling-dif-codes.md).

-   Starting with Windows 7, a device installation application can uninstall a device by calling the [**DiUninstallDevice**](https://msdn.microsoft.com/library/windows/hardware/ff544754) function. This function is similar to calling [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922) with the *InstallFunction* parameter set to [**DIF_REMOVE**](https://msdn.microsoft.com/library/windows/hardware/ff543717). However, in addition to removing the devnode of the specified device, this function attempts to remove all child devnodes of the device that are present on the system at the time of the call.

### <a href="" id="deleting-a-driver-package-from-the-driver-store"></a> Deleting a Driver Package from the Driver Store

Starting with Windows XP, a device installation application can call the [SetupUninstallOEMInf](http://go.microsoft.com/fwlink/p/?linkid=169503) function to remove a specified [INF file](inf-files.md) from the system INF file directory.

Starting with Windows Vista, this function also removes the [driver package](driver-packages.md), which contains the specified INF file, from the [driver store](driver-store.md).

### <a href="" id="deleting-the-binary-files-of-the-installed-driver"></a> Deleting the Binary Files of the Installed Driver

SetupAPI cannot be used to perform this action.

 

 





