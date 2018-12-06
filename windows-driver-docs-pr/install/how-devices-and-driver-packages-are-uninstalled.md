---
title: How Devices and Driver Packages are Uninstalled
description: How Devices and Driver Packages are Uninstalled
ms.assetid: 0f4f0bbf-ca8f-47ef-b70b-d023bba9b842
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How Devices and Driver Packages are Uninstalled


This section provides an overview of what you need to do to uninstall a device and [driver package](driver-packages.md). Perform these actions by running one of the following:

-   [Device Manager](using-device-manager.md).

-   A device installation application that calls the [SetupAPI](setupapi.md) and [device installation](https://msdn.microsoft.com/library/windows/hardware/ff541299) functions.

These actions include the following:

-   [Uninstalling the Device](#uninstalling-the-device)

-   [Deleting a Driver Package from the Driver Store](#deleting-a-driver-package-from-the-driver-store)

-   [Deleting the Binary Files of the Installed Driver](#deleting-the-binary-files-of-the-installed-driver)

**Note**  These actions do not need to be performed in sequential order.

 

### <a href="" id="uninstalling-the-device"></a> Uninstalling the Device

This uninstall action removes the device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) that represents the physical instance of the device in the system. Devnodes are removed by using one of the following methods:

-   Device Manager. For more information, see [Using Device Manager](using-device-manager.md).

-   A device installation application that calls the [SetupAPI](setupapi.md) [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922) function with a request of [**DIF_REMOVE**](https://msdn.microsoft.com/library/windows/hardware/ff543717). For more information, see [Using General Setup Functions](using-general-setup-functions.md).

-   A device installation application that calls the SetupAPI [**DiUninstallDevice**](https://msdn.microsoft.com/library/windows/hardware/ff544754) function (Windows 7 and later versions of Windows). For more information, see [Using Device Installation Functions](using-device-installation-functions.md).

When a device is uninstalled by using one of these methods, the Plug and Play (PnP) manager removes a subset of the system states that were created during device installation. For example, it removes the association between the driver binary files and the device. This association is used by the Service Control Manager (SCM) to load the appropriate driver for the device.

This uninstall action does not undo all the actions that were performed during the installation process. For example, the [driver package](driver-packages.md) and the driver's binary files remain where they were copied to the local hard disk. Some registry keys that were created by a [*class installer*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-class-installer) or [*co-installer*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-co-installer) (together with some other registry operations) are not changed.

**Note**  After this uninstall action is finished, the devnode for the device no longer exists, however, the [driver package](driver-packages.md) is still present in the [driver store](driver-store.md). If the PnP manager re-enumerates the device (such as when the device is unplugged and then plugged in again), the PnP manager treats it as a new device instance and installs the driver package from the driver store.

 

### <a href="" id="deleting-a-driver-package-from-the-driver-store"></a> Deleting a Driver Package from the Driver Store

This uninstall action deletes the files that are associated with the [driver package](driver-packages.md) from the [driver store](driver-store.md) and removes the associated metadata from the PnP manager's internal database. This action also deletes the [INF files](inf-files.md), which are associated with the driver package, from the system INF directory.

After the driver package has been removed from the driver store, it is no longer available to be installed on a device. The driver package must be restaged and installed to the [driver store](driver-store.md) from the original source, such as optical media, a network share, or Windows Update.

Before deleting a driver package from the driver store, be sure to uninstall all devices that are using it.

**Important**  You must not manually delete the [driver package](driver-packages.md) from the [driver store](driver-store.md). Doing so can cause an inconsistency between the INF fie, the driver store catalog, and the driver in the driver store. You might also be unable to stage the same driver package to the driver store.

 

### <a href="" id="deleting-the-binary-files-of-the-installed-driver"></a> Deleting the Binary Files of the Installed Driver

[Device Manager](using-device-manager.md) and the PnP manager do not support deleting driver binaries from the target destinations where they were installed. 

When you uninstall a driver package, the associated driver binaries might still be used by devices or applications. Removing the binaries can lead to system failures. Before you remove any driver binaries, make sure that the binaries are not still being used by any other component on the system and can be safely removed.



 

 





