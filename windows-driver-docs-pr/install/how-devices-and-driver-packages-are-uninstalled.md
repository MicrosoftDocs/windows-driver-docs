---
title: How Devices and Driver Packages are Uninstalled
description: How Devices and Driver Packages are Uninstalled
ms.assetid: 0f4f0bbf-ca8f-47ef-b70b-d023bba9b842
ms.date: 10/07/2020
ms.localizationpriority: medium
---

# How Devices and Driver Packages are Uninstalled

This page describes how a driver uninstalls a device and removes a driver package from the [driver store](driver-store.md).

## Uninstalling the Device

To remove the device node (*devnode*) that represents a physical device, use one of the following:

* A device installation application that calls the [SetupAPI](setupapi.md) [**SetupDiCallClassInstaller**](/windows/win32/api/setupapi/nf-setupapi-setupdicallclassinstaller) function with a request of [**DIF_REMOVE**](./dif-remove.md). For more information, see [Using General Setup Functions](using-general-setup-functions.md).

* A device installation application that calls the [**DiUninstallDevice**](/windows/win32/api/newdev/nf-newdev-diuninstalldevice) function. For more information, see [Using Device Installation Functions](using-device-installation-functions.md).

When a device is uninstalled using one of these methods, the Plug and Play (PnP) manager removes the association between the driver binary files and the device.

The device remains in the kernel PnP tree and the [driver package](driver-packages.md) remains in the [driver store](driver-store.md). If the PnP manager re-enumerates the device (for example if the device is unplugged and then plugged in again), the PnP manager treats it as a new device instance and installs the driver package from the driver store.

For info on how an end user can uninstall a device, see  [Using Device Manager to Uninstall Devices and Driver Packages](using-device-manager-to-uninstall-devices-and-driver-packages.md).

## Deleting a Driver Package from the Driver Store

Before deleting a driver package from the driver store, be sure to uninstall all devices that are using it.

To delete a [driver package](driver-packages.md) from the [driver store](driver-store.md), use one of these options:

* `pnputil /delete-driver <blah.inf> /uninstall`
* Use DevCon to [remove devices by device instance ID pattern](../devtest/devcon-examples.md#ddk_example_35_remove_devices_by_device_instance_id_pattern_tools)

Deleting the [driver package](driver-packages.md) from the [driver store](driver-store.md) removes associated metadata from the PnP manager's internal database and deletes related INF files from the system INF directory.

After the driver package has been removed from the driver store, it is no longer available to be installed on a device. To reinstall, download the driver again from the original source, such as Windows Update.

Manually deleting the [driver package](driver-packages.md) from the [driver store](driver-store.md) may result in unpredictable behavior.

