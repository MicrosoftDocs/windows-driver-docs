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

-   A device installation application that calls the [SetupAPI](setupapi.md) and [device installation](https://docs.microsoft.com/previous-versions/ff541299(v=vs.85)) functions.

These actions include the following:

-   [Uninstalling the Device](#uninstalling-the-device)

-   [Deleting a Driver Package from the Driver Store](#deleting-a-driver-package-from-the-driver-store)

**Note**  These actions do not need to be performed in sequential order.

 

### <a href="" id="uninstalling-the-device"></a> Uninstalling the Device

This uninstall action removes the device node (*devnode*) that represents the physical instance of the device in the system. Devnodes are removed by using one of the following methods:

-   Device Manager. For more information, see [Using Device Manager](using-device-manager.md).

-   A device installation application that calls the [SetupAPI](setupapi.md) [**SetupDiCallClassInstaller**](https://docs.microsoft.com/windows/desktop/api/setupapi/nf-setupapi-setupdicallclassinstaller) function with a request of [**DIF_REMOVE**](https://docs.microsoft.com/windows-hardware/drivers/install/dif-remove). For more information, see [Using General Setup Functions](using-general-setup-functions.md).

-   A device installation application that calls the SetupAPI [**DiUninstallDevice**](https://docs.microsoft.com/windows/desktop/api/newdev/nf-newdev-diuninstalldevice) function (Windows 7 and later versions of Windows). For more information, see [Using Device Installation Functions](using-device-installation-functions.md).

When a device is uninstalled by using one of these methods, the Plug and Play (PnP) manager removes a subset of the system states that were created during device installation. For example, it removes the association between the driver binary files and the device. This association is used by the Service Control Manager (SCM) to load the appropriate driver for the device.

This uninstall action does not undo all the actions that were performed during the installation process. For example, the driver package or *co-installer* (together with some other registry operations) are not changed.

**Note**  After this uninstall action is finished, the devnode for the device no longer exists, however, the [driver package](driver-packages.md) is still present in the [driver store](driver-store.md). If the PnP manager re-enumerates the device (such as when the device is unplugged and then plugged in again), the PnP manager treats it as a new device instance and installs the driver package from the driver store.

 

### <a href="" id="deleting-a-driver-package-from-the-driver-store"></a> Deleting a Driver Package from the Driver Store

This uninstall action deletes the files that are associated with the [driver package](driver-packages.md) from the [driver store](driver-store.md) and removes the associated metadata from the PnP manager's internal database. This action also deletes the [INF files](overview-of-inf-files.md), which are associated with the driver package, from the system INF directory.

After the driver package has been removed from the driver store, it is no longer available to be installed on a device. The driver package must be restaged and installed to the [driver store](driver-store.md) from the original source, such as optical media, a network share, or Windows Update.

Before deleting a driver package from the driver store, be sure to uninstall all devices that are using it.

**Important**  You must not manually delete the [driver package](driver-packages.md) from the [driver store](driver-store.md). Doing so can cause an inconsistency between the INF fie, the driver store catalog, and the driver in the driver store. You might also be unable to stage the same driver package to the driver store.

 


 

 





