---
title: Using SetupAPI to Uninstall Devices and Driver Packages
description: Using SetupAPI to Uninstall Devices and Driver Packages
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using SetupAPI to Uninstall Devices and Driver Packages


[SetupAPI](setupapi.md) is a system component that provides two sets of functions:

-   [General Setup functions](/previous-versions/ff544985(v=vs.85))

-   [Device installation functions](/previous-versions/ff541299(v=vs.85))

*Device installation applications*, *co-installers*, and *class installers* can use these functions to perform custom operations for device installation. SetupAPI also supports uninstalling the devices and [driver packages](driver-packages.md) that it installs.

This topic describes the procedures that you can follow to uninstall devices and driver packages by using the SetupAPI functions.

For more information about uninstalling driver and driver packages, see [How Devices and Driver Packages are Uninstalled](how-devices-and-driver-packages-are-uninstalled.md).

### <a href="" id="uninstalling-the-device"></a> Uninstalling the Device

[SetupAPI](setupapi.md) allows you to uninstall a device and remove the device node (*devnode*) from the system by using the following methods:

-   A device installation application can request that a device be uninstalled by calling the [**SetupDiCallClassInstaller**](/windows/win32/api/setupapi/nf-setupapi-setupdicallclassinstaller) function. When the application calls this function to uninstall a device, it must set the *InstallFunction* parameter to the [**DIF_REMOVE**](./dif-remove.md) code.  For a list of all DIF codes, see [Device Installation Functions](/previous-versions/ff541307(v=vs.85)).

    If [**SetupDiRemoveDevice**](/windows/win32/api/setupapi/nf-setupapi-setupdiremovedevice) is called during the processing of the DIF_REMOVE request, the function removes the device's devnode from the system. It also deletes the device's hardware and software registry keys, together with any hardware-profile-specific registry keys (configuration-specific registry keys).

    **Note**  **SetupDiRemoveDevice** must only be called by a class installer and not by a device installation application.

    For more information about DIF codes, see [Handling DIF Codes](handling-dif-codes.md).

-   Starting with Windows 7, a device installation application can uninstall a device by calling the [**DiUninstallDevice**](/windows/win32/api/newdev/nf-newdev-diuninstalldevice) function. This function is similar to calling [**SetupDiCallClassInstaller**](/windows/win32/api/setupapi/nf-setupapi-setupdicallclassinstaller) with the *InstallFunction* parameter set to [**DIF_REMOVE**](./dif-remove.md). However, in addition to removing the devnode of the specified device, this function attempts to remove all child devnodes of the device that are present on the system at the time of the call.

### <a href="" id="deleting-a-driver-package-from-the-driver-store"></a> Deleting a Driver Package from the Driver Store

Starting with Windows XP, a device installation application can call the [SetupUninstallOEMInf](/windows/win32/api/setupapi/nf-setupapi-setupuninstalloeminfa) function to remove a specified [INF file](overview-of-inf-files.md) from the system INF file directory.

Starting with Windows Vista, this function also removes the [driver package](driver-packages.md), which contains the specified INF file, from the [driver store](driver-store.md).

### <a href="" id="deleting-the-binary-files-of-the-installed-driver"></a> Deleting the Binary Files of the Installed Driver

SetupAPI cannot be used to perform this action.

